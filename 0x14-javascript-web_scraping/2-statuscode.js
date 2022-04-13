#!/usr/bin/node

const request = require('request');

const { argv } = require('process');

if (argv[2]) {
  request(argv[2], function (error, response, body) {
    if (error) { console.error('error:', error); } else { console.log('code:', response && response.statusCode); }
  }
  );
}
