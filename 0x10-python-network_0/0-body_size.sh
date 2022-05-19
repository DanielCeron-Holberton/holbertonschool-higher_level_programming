#!/usr/bin/bash

curl -sI "$2" | grep -i Content-Length | cut -d ":" -f 2 | cut -d " " -f2
