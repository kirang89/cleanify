#!/usr/bin/env bash

#
# Script to install js beautifier module for python
#

git clone https://github.com/einars/js-beautify.git
cd js-beautify/python
sudo python setup.py install
