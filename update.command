#!/bin/bash

# Change to the script directory
cd "$(dirname "$BASH_SOURCE")" || {
    echo "Error getting script directory" >&2
    exit 1
}

python bin/upload.py

echo "Complete!"
echo "You may not close this window."
