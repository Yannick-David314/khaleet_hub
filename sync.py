import os
import sys
import time

from dotenv import load_dotenv
import requests

LANG_EXT_REF = {
    'c': 'c',
    'cpp': 'cpp',
    'csharp': 'cs',
    'java': 'java',
    'python': 'py',
    'python3': 'py',
    'pythondata': 'py',   # pandas problems
    'javascript': 'js',
    'typescript': 'ts',
    'php': 'php',
    'swift': 'swift',
    'kotlin': 'kt',
    'dart': 'dart',
    'golang': 'go',
    'ruby': 'rb',
    'scala': 'scala',
    'rust': 'rs',
    'racket': 'rkt',
    'erlang': 'erl',
    'elixir': 'ex',
    'mysql': 'sql',
    'mssql': 'sql',
    'oraclesql': 'sql',
    'postgresql': 'sql',
    'bash': 'sh',
}
PAGE_SIZE = 20
SOLUTIONS_DIR = 'solutions'



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
user_data = lc_request(login_query)
user_info = user_data['userStatus']
for status in user_info:
    print(user_info[status])
if not user_info['isSignedIn']:
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
    page_data = lc_request(page_query, page_vars) # so page_data contains only one key, submissionList
    page_info = page_data['submissionList']
    # so page_info contains three keys: hasNext, lastKey and submissions (which is a
    # list of dictionaries, and each dictionary has the six keys listed in page_query)
    all_submissions.extend(page_info['submissions'])
    offset += PAGE_SIZE
    hasNext = page_info['hasNext']
    time.sleep(1)

newest_submissions = {}
for submission in all_submissions:
    if submission['statusDisplay'] != 'Accepted':
        continue
    if submission['titleSlug'] not in newest_submissions:
        newest_submissions[submission['titleSlug']] = submission 
# by the end of this loop every entry in newest_submissions should have a
# title slug as a key, and the submission associated with that slug as a value



# GETTING SUBMISSION DETAILS
sub_query = '''query ($id: Int!) {
                    submissionDetails(submissionId: $id) {
                        code
                        question { questionFrontendId }
                    }
                }'''
for submission in newest_submissions.values():
    sub_var = {'id': int(submission['id'])}
    lc_submission_details = lc_request(sub_query, sub_var) # lc_submission_details contains only one key
    lc_submission_data = lc_submission_details['submissionDetails'] # lc_submission_data contains two keys: code and question
    lc_question_info = lc_submission_data['question'] 
    submission['my_code'] = lc_submission_data['code']
    submission['question_number'] = lc_question_info['questionFrontendId']
    print(f"Question #{submission['question_number']}, {submission['titleSlug']} added!")
    time.sleep(1)



# WRITING SOLUTIONS TO FILE
for submission in newest_submissions.values():
    file_extension = LANG_EXT_REF.get(submission['lang'], 'txt')
    folder_name = f"{submission['question_number'].zfill(4)}-{submission['titleSlug']}"
    folder_path = os.path.join(SOLUTIONS_DIR, folder_name)
    file_path = os.path.join(folder_path, f"solution.{file_extension}")
    os.makedirs(folder_path, exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(submission['my_code'])
    print(f"Wrote {file_path}.")
    






