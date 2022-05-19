#!/usr/bin/bash
# Used curl to get the body size


if [$# -lt 2]:
	echo "Not enough args"
	


curl -sI {$2} | grep -i Content-Length | cut -d ":" -f 2 | cut -d " " -f2
