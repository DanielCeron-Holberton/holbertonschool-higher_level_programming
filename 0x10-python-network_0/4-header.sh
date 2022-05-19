#!/bin/bash
# Script that generates a get request with header
curl -s -X GET -H "X-HolbertonSchool-User-Id: 98" "$1"
