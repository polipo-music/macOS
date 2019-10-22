#!/bin/bash
set -ex

pip3 install -r requirements.txt
./sync.py
