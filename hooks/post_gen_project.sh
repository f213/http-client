#!/bin/bash -e

echo -ne "Running with "

python --version

echo Creating and populating virtualenv..

python -m venv venv
. venv/bin/activate

pip install --upgrade pip wheel
pip install -r requirements.txt

isort .

make lint test

echo Done
