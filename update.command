#!/bin/bash

# Change to the script directory
cd "$(dirname "$BASH_SOURCE")" || {
    echo "Error getting script directory" >&2
    exit 1
}

# install python dependencies
echo -e "\n***********************************"
echo "Checking for python dependencies..."
echo "***********************************"

# Module included in Python Standard Library as of 2.7.9 (Dec. 10, 2014) and 3.4 (March 17, 2014)
# --upgrade flag ensures pip is at least as new as the one bundled with ensurepip (i.e. that version of python)

python -m ensurepip --upgrade || {

  # If the module is missing, which should be extremely rarely, prompt user to install newer python, and exit.
  echo -e "\n Unable to ensure pip, which is required to verify dependencies."
  echo "Please update python before trying again."
  echo "See https://www.python.org/downloads/ for more info."
  exit 1;

}

python -m pip install --user ampy
python -m pip install --user esptool # tentatively required

echo -e "***********************************\n"

python bin/upload.py

echo "Complete!"
echo "You may now close this window."
