#!/usr/bin/node


function factorial(num) {
    if (num < 0) {
        return (-1);
    }
    else if (num == 0) {
        return (1);
    }
    else {
        return (num * factorial(num - 1));
    }
}

const { argv } = require('process');

let myResult;

if (argv[2]) {
    myResult = factorial(parseInt(argv[2]));
}
else{
    myResult = 1;
}
console.log(myResult);
