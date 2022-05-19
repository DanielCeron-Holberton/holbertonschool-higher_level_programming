#!/bin/bash
# Script that generates the methods allowed
curl -sI "$1" | grep "Allowed:" | cut -d' ' -f2-
