#!/bin/bash

# Import global variables
source script/global_var.sh

if [ ! -d "$PYTHON_VIR_ENV_DIR" ]; then
    echo -e "\nSetting up virtual environment for python 3.7.."
    mkdir "$VIR_ENV_DIR"
    python3.7 -m venv "$PYTHON_VIR_ENV_DIR"
    if [ -d "$PYTHON_VIR_ENV_DIR" ]; then
        echo -e "\nFinished setting up virtual environment at \"$PYTHON_VIR_ENV_DIR\".\n"
    fi
else
    echo -e "\nVirtual environment is already set up at \"$PYTHON_VIR_ENV_DIR\".\n"
fi
