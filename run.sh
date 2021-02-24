#!/bin/bash
cd $(dirname ${BASH_SOURCE[0]})
./setting.sh "$@"
python3 ./main.py

