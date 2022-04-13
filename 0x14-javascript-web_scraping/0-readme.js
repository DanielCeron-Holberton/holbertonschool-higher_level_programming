#!/usr/bin/node



const fs = require('fs');
const { argv } = require('process');

if (argv[2]) {
    fs.readFile(argv[2], 'utf8', function (err, data) {
        if (err)
            console.log(err);
        else
            console.log(data);
    });
}