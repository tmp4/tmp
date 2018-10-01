#!/bin/bash

pip install pwntools
export TERM=linux
echo 'Password?'
./dec.sh 

cd solutions
~/.local/bin/pip2.7 install ipython --user
~/.local/bin/ipython $1
