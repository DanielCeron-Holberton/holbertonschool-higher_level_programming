#!/usr/bin/node


const request = require('request');
const { argv } = require('process');


if (argv[2]) {
    request(argv[2], function (body, error, response) {
        const userToCheck = JSON.parse(body).userId;

        console.log(userToCheck);

    }
}