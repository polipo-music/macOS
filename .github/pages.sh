#!/bin/bash
set -ex

pip3 install -r .github/requirements.txt

mkdir gh-pages
cd gh-pages
../.github/pages.py >index.html

[ -z "$(git status --porcelain)" ] && exit 0

git config --global user.name 'GitHub Actions'
git config --global user.email "$(whoami)@$(hostname --fqdn)"
git init
git add --all
git commit --all --message 'automatic commit'
git push --force "https://${GITHUB_PERSONAL_ACCESS_TOKEN}@github.com/${GITHUB_REPOSITORY}.git" HEAD:gh-pages
