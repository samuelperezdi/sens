#!/bin/bash

DATA_PATH="output"
STACK_IDS_FILE="stack_ids.txt"

# Get the last ID from stack_ids.txt (skipping the first line)
LAST_ID=$(tail -n 1 "$STACK_IDS_FILE")

# Find the last .tar file by sorting numerically
LAST_TAR=$(ls "$DATA_PATH"/package.*.tar | sort -V | tail -n1)

if [ -z "$LAST_TAR" ]; then
    echo "No package.*.tar files found in $DATA_PATH"
    exit 1
fi

# Extract the ID from the filename
LAST_TAR_ID=$(basename "$LAST_TAR" .tar | cut -d. -f2)

# Untar only the last package
tar -xf "$LAST_TAR"

echo "untared $LAST_TAR"
echo "does it has stack_id $LAST_ID?"