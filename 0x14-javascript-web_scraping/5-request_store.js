#!/usr/bin/node

const { argv } = require('process');
const fs = require('fs');
const request = require('request');

if (argv[3]) {
  request(argv[2], function (error, response, body) {
    if (error) { console.log(error); } else {
      fs.writeFile(argv[3], body, (err) => {
        if (err) { console.log(err); }
      });
    }
  });
}
