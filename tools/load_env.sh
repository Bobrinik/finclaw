#!/bin/bash


if [ ! -f .env ]; then
    echo ".env file not found"
    exit 1
fi

# Export the variables in the .env file
export $(cat .env | sed 's/#.*//g' | xargs)

echo "Environment variables loaded successfully"
