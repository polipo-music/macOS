#!/usr/bin/env python3
import json
import requests
import subprocess

session = requests.Session()
proc = subprocess.run(['git', 'for-each-ref', '--format=%(refname:lstrip=3)', 'refs/remotes/origin/??????????????????????????????????'],
    stdout=subprocess.PIPE,
    check=True,
)
to_delete = []
for branch in proc.stdout.decode().strip().split('\n'):
    product = json.loads(subprocess.run(['git', 'show', f'refs/remotes/origin/{branch}:product.json'],
        stdout=subprocess.PIPE,
        check=True,
    ).stdout)
    rsp = session.head(product['DistributionURL'], allow_redirects=False)
    if rsp.status_code == 200:
        continue
    if rsp.status_code != 404:
        print(f'[WARNING] {branch} {rsp.status_code} {rsp.reason}')
    to_delete.append('refs/heads/'+branch)
if to_delete:
    subprocess.run(['git', 'push', '--delete', 'origin'] + to_delete, check=True)
