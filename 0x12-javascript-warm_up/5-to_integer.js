#!/usr/bin/node

const { argv } = require('process');

const MyNumber = parseInt(argv[2]);

if (MyNumber) {
  console.log('My number: ' + MyNumber);
} else {
  console.log('Not a number');
}
