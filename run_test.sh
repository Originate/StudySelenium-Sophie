#!/bin/bash

# Import global variables
source script/global_var.sh

# Set driver path to system PATH for current test
cwd=$(pwd)
export PATH=$PATH:"$cwd/$DRIVER_DIR"

# Activate python virtual environment
source "$PYTHON_VIR_ENV_DIR/bin/activate"

# Run test
py.test

# Deactivate python virtual environment when test is finished
deactivate
