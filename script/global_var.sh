#!/bin/bash

# Define the path of python virtual environment

# NOTE: if `VIR_ENV_DIR` is changed, `PYTHON VIRTUAL ENV:` in `python/.gitignore` need to be changed to the same value
export VIR_ENV_DIR=".seleniumVirtualEnvPy"
export PYTHON_VIR_ENV_DIR="$VIR_ENV_DIR/python3.7"
export DRIVER_DIR="drivers"
