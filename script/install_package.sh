#!/bin/bash

# Import global variables
source script/global_var.sh

# Activate the virtual environment of python
source "$PYTHON_VIR_ENV_DIR/bin/activate"

# Install selenium
python -c "import selenium"
seleniumInstalled=$?
if [ "$seleniumInstalled" == 1 ]; then
    echo -e "\nselenium is not installed"
    echo -e "\ninstalling selenium..\n"
    pip install selenium
else
    echo -e "\nselenium is already installed in current virtual environment at $PYTHON_VIR_ENV_DIR"
fi

# Install pytest
python -c "import pytest"
pytestInstalled=$?
if [ "$pytestInstalled" == 1 ]; then
    echo -e "\npytest is not installed"
    echo -e "\ninstalling pytest..\n"
    pip install pytest
else
    echo -e "\npytest is already installed in current virtual environment at $PYTHON_VIR_ENV_DIR\n"
fi

# Deactivate python virtual environment
deactivate
