import os
import sys
import time

from dotenv import load_dotenv
import requests

PAGE_SIZE = 20



# SETTING UP
load_dotenv()
lc_session = os.environ.get('LEETCODE_SESSION')
csrf = os.environ.get('LEETCODE_CSRF')
if not lc_session or not csrf:
    sys.exit('COOKIES MISSING FROM .env JAR 👎.')
else:
    print('Loaded OK 👍!')



# LEETCODE REQUEST FUNCTION
def lc_request(query, variables: dict | None = None):
    url = 'https://leetcode.com/graphql'
    body = {'query': query, 'variables': variables}
    cookies = {'LEETCODE_SESSION': lc_session, 'csrftoken': csrf}
    headers = {'x-csrftoken': csrf, 'referer': 'https://leetcode.com'}

    response = requests.post(url, json=body, cookies=cookies, headers=headers, timeout=10)
    response.raise_for_status()
    rjson = response.json()
    if rjson.get('errors'):
        sys.exit(f"GraphQL error: {rjson['errors']}")
    return rjson['data']



# SIGNING IN
login_query = '{ userStatus { username isSignedIn } }'
userData = lc_request(login_query)
userStatus = userData['userStatus']
for status in userStatus:
    print(userStatus[status])
if not userStatus['isSignedIn']:
    sys.exit('SIGN IN UNSUCCESSFUL ❌. COOKIES HAVE GONE STALE. GET FRESH ONES.')



# GETTING PAGE DATA
all_submissions = []
offset = 0
page_query = '''query ($offset: Int!, $limit: Int!) {
                    submissionList(offset: $offset, limit: $limit) {
                        hasNext
                        lastKey
                        submissions { id title titleSlug statusDisplay lang timestamp }
                    }
                } ''' # Note to self: 'lastKey' is pretty much useless since you're using 'offset'.
hasNext = True
while hasNext:
    page_vars = {'offset': offset, 'limit': PAGE_SIZE}
    pageData = lc_request(page_query, page_vars)
    submission_list = pageData['submissionList']
    all_submissions.extend(submission_list['submissions'])
    offset += PAGE_SIZE
    hasNext = submission_list['hasNext']
    time.sleep(1)

newest_submissions = {}
for submission in all_submissions:
    if submission['statusDisplay'] != 'Accepted':
        continue
    if submission['titleSlug'] not in newest_submissions:
        newest_submissions[submission['titleSlug']] = submission
print(len(all_submissions))
print(len(newest_submissions))
for submission in newest_submissions:
    print(submission)




