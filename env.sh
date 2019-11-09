#!/bin/bash

# get installation location
SCRIPT=$(readlink -f "$BASH_SOURCE")
INSTALL_LOC=$(dirname "$SCRIPT")

echo "Installation location :" $INSTALL_LOC

export PYTHONPATH=$PYTHONPATH:$INSTALL_LOC/src
export PATH=$PATH:$INSTALL_LOC/tests
