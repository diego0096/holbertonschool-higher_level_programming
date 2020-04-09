#!/bin/bash
# Bash script to display the size of the body
curl -sI "$1" | grep 'Allow' | cut -d " " -f2-
