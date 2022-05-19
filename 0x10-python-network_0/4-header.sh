#!/bin/bash
HEADEVAR="X-HolbertonSchool-User-Id:98"
curl -sI -X GET "$1" -H "$HEADERVAR"
