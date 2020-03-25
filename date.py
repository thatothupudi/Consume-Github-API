from github import Github
import urllib3
import requests
import json
from datetime import datetime
from datetime import timedelta, date
from api import repos

from secrets import username
from secrets import password
from secrets import token

r = requests.get("https://api.github.com/repos/thatothupudi/pulls")
len(r.json()) == 13
print(r)

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2020, 8, 20)
end_date = date(2020, 3, 17)

for single_date in daterange(start_date,end_date):
    date_obj = datetime.combine(single_date,datetime.min.time())
    print(single_date.strftime('%Y-%m-%d:'), 'repo.name')