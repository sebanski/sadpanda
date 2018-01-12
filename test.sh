#!/bin/bash

# clear the screen and leave some space
clear
echo 🐼 💦🐼 💦🐼 💦🐼 💦🐼 💦🐼 💦🐼 💦🐼 💦🐼 💦🐼 💦🐼 💦🐼 💦🐼 💦🐼 💦🐼 💦🐼 💦🐼 💦🐼 💦🐼 💦 
for i in {0..8}; do echo 🐼 💦                                          🐼 💦 ; done
echo 🐼 💦🐼 💦🐼 💦🐼 💦🐼 💦🐼 💦🐼 💦🐼 💦🐼 💦🐼 💦🐼 💦🐼 💦🐼 💦🐼 💦🐼 💦🐼 💦🐼 💦🐼 💦🐼 💦 

# install the sadpanda library with pip **(this is required when testing currently.)
pip3 install . --upgrade

# run tests against python-3.5
tox -e py35 tests/ -v

