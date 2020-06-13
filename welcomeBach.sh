#!/bin/bash
cd $PWD;
venv=$PWD/venv/bin/activate;
. $venv;
python3 bach.py;
deactivate;
