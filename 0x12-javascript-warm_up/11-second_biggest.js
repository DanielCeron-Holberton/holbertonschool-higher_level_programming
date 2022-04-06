#!/usr/bin/node

//const que hace aqui joven aún entre las verdes ramas http://sedemargaritas.blogspot.com/2012/11/un-poema-de-epifanio-mejia.html

const { argv } = require('process');

if (!argv[2] || !argv[3]) {
    console.log(0)
}
else {
    let sortedArgs = argv.sort();
    sortedArgs = argv.reverse();

    console.log(sortedArgs[1]);
}
