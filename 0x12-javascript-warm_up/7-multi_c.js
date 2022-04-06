#!/usr/bin/node

const { argv } = require('process');

const MyNumber = parseInt(argv[2]);

if (!MyNumber) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 1; index <= MyNumber; index++) {
    console.log('C is fun');
  }
}
