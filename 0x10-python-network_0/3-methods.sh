#!/bin/bash
# Script that generates the methods allowed
curl -sI "$1" | grep "Allow:" | cut -d' ' -f2-
