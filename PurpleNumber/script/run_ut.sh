#!/bin/bash

SRC=src
UT=test

export PYTHONPATH=$PYTHONPATH:$PWD/$SRC
python -m unittest discover -s $UT/ -p *_test.py -v 
