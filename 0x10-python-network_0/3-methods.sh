#!/bin/bash
# Script that generates the methods allowed
curl -sI "$1" | grep -i "Allowed:" | cut -d' ' -f2-
