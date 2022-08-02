#!/bin/bash

cd scriptps || cd source/scriptps
source venv/bin/activate || source ~/.bash_profile

python psa/cli/psa_cli.py