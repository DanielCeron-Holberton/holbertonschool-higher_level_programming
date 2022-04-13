#!/usr/bin/node

const { argv } = require('process');

const request = require('request');

if (argv[2]) {
  let counter = 0;
  request(argv[2], function (error, response, body) {
    const toFind = '18/';
    if (error) { console.log('error:', error); } else {
      const characterID = JSON.parse(body).results;
      for (let index = 0; index < characterID.length; index++) {
        const listCharacters = Object.values(characterID[index].characters);
        listCharacters.forEach(element => {
          if (element.slice(-3) === toFind) {
            counter += 1;
          }
        });
      }
      console.log(counter);
    }
  });
}
