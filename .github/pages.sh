#!/bin/bash
set -ex

mkdir gh-pages
cd gh-pages
../pages.py >index.html

git config --global user.name 'GitHub Actions'
git config --global user.email "$(whoami)@$(hostname --fqdn)"
git init
git add --all
git commit --all --message 'automatic commit'
git push --force "https://${GITHUB_PERSONAL_ACCESS_TOKEN}@github.com/${GITHUB_REPOSITORY}.git" HEAD:gh-pages
