#!/bin/bash

cd scriptps || cd source/scriptps || echo 'Error: Cant find `scriptps/` directory'
git pull

printf "\nUpdate Successful! \n\n"