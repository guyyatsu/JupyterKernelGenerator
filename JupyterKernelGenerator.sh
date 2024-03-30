#!/bin/bash
TRASH=/dev/null

# Create the python virtual environment.
echo "Creating $2 Virtual Environment, please wait...";
python3 -m venv $1;
echo "ipykernel" >>  $1/requirements.txt;
source $1/bin/activate;

# Install dependencies and upload kernel.
echo "Installing dependencies; this may take a while.";
pip install -r $1/requirements.txt 2> $TRASH;
python3 -m ipykernel install --user --name=$2;