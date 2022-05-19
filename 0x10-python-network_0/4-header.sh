#!/bin/bash
# Script that generates a get request with header
curl -sI -X GET "$1" -H "X-HolbertonSchool-User-Id:98"
