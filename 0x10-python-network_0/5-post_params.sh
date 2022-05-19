#!/bin/bash
# Script that sents a data for post method
curl -sX POST -d email=test@gmail.com -d subject="I will always be here for PLD" "$1"
