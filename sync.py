import sys
import os

from dotenv import load_dotenv
import requests


load_dotenv()
lc_session = os.environ.get("LEETCODE_SESSION")
csrf = os.environ.get("LEETCODE_CSRF")
if not lc_session or not csrf:
    sys.exit("COOKIES MISSING FROM .env JAR 👎.")
else:
    print("Loaded OK 👍!")

url = "https://leetcode.com/graphql"
body = {"query": "{ userStatus { username isSignedIn } }"}
cookies = {"LEETCODE_SESSION": lc_session, "csrftoken": csrf}
headers = {"x-csrftoken": csrf, "referer": "https://leetcode.com"}

response = requests.post(url, json=body, cookies=cookies, headers=headers, timeout=10)
response.raise_for_status()
userData = response.json()["data"]
userStatus = userData["userStatus"]
for status in userStatus:
    print(userStatus[status])
if not userStatus["isSignedIn"]:
    sys.exit("SIGN IN UNSUCCESSFUL ❌. COOKIES HAVE GONE STALE. GET FRESH ONES.")


