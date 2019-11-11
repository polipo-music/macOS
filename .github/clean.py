#!/usr/bin/env python3
import json
import requests
import subprocess

session = requests.Session()
proc = subprocess.run(['git', 'for-each-ref', '--format=%(refname:short)', 'refs/remotes/origin/??????????????????????????????????'],
    stdout=subprocess.PIPE,
    check=True,
)
to_delete = []
for ref in proc.stdout.decode().strip().split('\n'):
    branch = ref.split('/', 1)[-1]
    product = json.loads(subprocess.run(['git', 'show', f'{ref}:product.json'],
        stdout=subprocess.PIPE,
        check=True,
    ).stdout)
    rsp = session.head(product['DistributionURL'], allow_redirects=False)
    if rsp.status_code == 200:
        continue
    if rsp.status_code != 404:
        print(f'[WARNING] {branch} {rsp.status_code} {rsp.reason}')
    to_delete.append(ref)
    print(f'[INFO] purge {branch}')
if to_delete:
    subprocess.run(['git', 'push', '--delete', 'origin'] + to_delete, check=True)
