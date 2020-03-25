from github import Github
import urllib3
import requests
# from datetime import datetime
# from datetime import timedelta, date


import My_token


from My_token import token

g = Github(token)

repos = g.get_user().get_repos()
for repo in repos:
    print(repo.name)