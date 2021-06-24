#Usage

# Imported requests library
import requests

# after that, Imported requests_random_user_agent library
import requests_random_user_agent

# than create object of 'requests.Session()' as 's'
s = requests.Session()

# First it's print your default user-agent on pc or laptop
print(s.headers['User-Agent'])

# Without a session
resp = requests.get('https://httpbin.org/user-agent')

# Secondly it's print your changed user-agent on pc or laptop
print(resp.json()['user-agent'])
