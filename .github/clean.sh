#!/bin/bash
set -ex

git config --global http.extraheader "Authorization: Basic $(echo -n "x-access-token:${GITHUB_TOKEN}" | base64 --wrap=0)"
pip3 install -r .github/requirements.txt

exec .github/clean.py
