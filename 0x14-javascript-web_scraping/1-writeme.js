#!/usr/bin/node


const fs = require('fs');

const { argv } = require('process');



if (argv[3]){
    let data = argv[3];
    fs.writeFile(argv[2], data, (err) =>{
        if (err)
            console.log(err);
    })
}