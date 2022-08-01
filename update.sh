#!/bin/bash

source ~/.bash_profile
cd scriptps || cd source/scriptps || echo 'Error: Cant find `scriptps/` directory'
git pull

python setup.py install --force

printf "\nUpdate Successful! \n\n"