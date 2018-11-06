#!/bin/bash

git config --global user.email "you@example.com"
git config --global user.name "Your Name"

~/.local/bin/pip install pwntools
export TERM=linux
echo 'Password?'
./dec.sh 

cd solutions
ipython $1
