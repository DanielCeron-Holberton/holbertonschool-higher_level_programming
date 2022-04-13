#!/usr/bin/node

const { argv } = require('process');

const request = require('request');


if (argv[2]){
    id = argv[2];
    request("https://swapi-api.hbtn.io/api/films/" + id, function (error, response, body){
    if(error){
        console.log('error:', error);
    }
    else
        console.log(JSON.parse(body).title);
    })
}
