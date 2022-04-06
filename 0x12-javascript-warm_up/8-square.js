#!/usr/bin/node

const { argv } = require('process');

const squareSize = parseInt(argv[2]);

let newString = '';

if (!squareSize) {
  console.log('Missing size');
} else {
  for (let index = 0; index < squareSize; index++) {
    newString = newString + 'X';
  }
  for (let index = 0; index < squareSize; index++) {
    console.log(newString);
  }
}
