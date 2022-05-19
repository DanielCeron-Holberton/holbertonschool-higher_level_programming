#!/usr/bin/env bash

curl -sI "$1" | grep -i Content-Length | cut -d ":" -f 2 | cut -d " " -f2
