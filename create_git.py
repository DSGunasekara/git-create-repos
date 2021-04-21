#!/usr/bin/env python3
import requests
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--name", "-n", type=str, dest="name", required=True)
parser.add_argument("--private", "-p", dest="is_private", action="store_true")
args = parser.parse_args()

repo_name = args.name
is_private = args.is_private
URL = 'https://api.github.com/user/repos'
TOKEN = 'put your token here'

headers = {
    "Authorization": "token " + TOKEN,
    "Accept": "application/vnd.github.v3+json"
    }
if is_private:
    payload = '{"name": "' + repo_name +'", "private": true}'
else:
    payload = '{"name": "' + repo_name +'", "private": false}'

r = requests.post(URL, data=payload, headers=headers)

y = r.json()
# print(y)
os.system("git clone " + y["clone_url"])
pwd = os.getcwd()
print(pwd)
os.chdir(pwd + "/" + repo_name)
os.system("echo '# " + repo_name + "' >> README.md")
os.system("git add . && git commit -m 'Initial Commit' && git push origin master")
