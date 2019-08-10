#!/bin/bash

# Change to the script directory
cd "$(dirname "$BASH_SOURCE")" || {
    echo "Error getting script directory" >&2
    exit 1
}

# install python dependencies
echo -e "\n\n***********************************"
echo "Checking for python dependencies..."
echo "***********************************"

pip install ampy
pip install esptool
echo -e "***********************************\n\n"

python bin/upload.py

echo "Complete!"
echo "You may now close this window."
