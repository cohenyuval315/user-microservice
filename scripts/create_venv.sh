#!/bin/bash

# source does not persist, bash run in subshell , so activate venv in terminal. 

# Configuration
PYTHON=python3.11
VENV_DIR="venv"
FOLDER="backend"
REQUIREMENTS_FILE="./.requirements/requirements.base.txt"
EXPORT_PYTHON_PATH=$(pwd)/..:$(pwd)/../server
SLEEP_AFTER_VENV=5


# Ensure the script is run from the backend folder
if [ "$(basename "$PWD")" != $FOLDER ]; then
    echo "This script must be run from the $FOLDER folder."
    exit 1
fi

# Check if Python 3.11 is installed, if not install it
if ! command -v $PYTHON &> /dev/null; then
    echo "$PYTHON not found, installing..."
    sudo apt update
    sudo apt install -y software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install -y $PYTHON
    sudo apt-get install -y $PYTHON-venv
    echo "$PYTHON installed successfully."
else
    echo "$PYTHON is already installed."
fi

# Check if virtual environment exists, if not create it
if [ ! -d "$VENV_DIR" ]; then
    $PYTHON -m venv $VENV_DIR || { echo "Failed to create virtual environment"; exit 1; }
    echo "Virtual environment created. sleeping $SLEEP_AFTER_VENV"
    sleep $SLEEP_AFTER_VENV
else
    echo "Virtual environment already exists."
    # exit 1
fi



# Activate the virtual environment and install requirements if successful

if source $VENV_DIR/bin/activate; then
    echo "Virtual environment activated."

    # Check if requirements file exists before installing
    if [ -f "$REQUIREMENTS_FILE" ]; then
        pip install -r $REQUIREMENTS_FILE || { echo "Failed to install requirements"; exit 1; }
    else
        echo "Requirements file not found: $REQUIREMENTS_FILE"
        exit 1
    fi

    # Set PYTHONPATH
    export PYTHONPATH=$PYTHONPATH:$EXPORT_PYTHON_PATH
    echo "PYTHONPATH is set to: $PYTHONPATH"
else
    echo "Failed to activate virtual environment."
    exit 1
fi
