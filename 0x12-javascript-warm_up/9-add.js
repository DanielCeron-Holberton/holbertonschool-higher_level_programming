#!/usr/bin/node

function add(a, b)
{
    let c = a + b;
    console.log(c);
}

const { argv } = require('process');

add(parseInt(argv[2]), parseInt(argv[3]));
