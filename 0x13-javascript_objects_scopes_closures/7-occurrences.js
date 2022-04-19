#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;

  for (let index = 0; index < list.length; index++) {
    if (list[index] === searchElement) {
      counter += 1;
    }
  }
  return counter;
};
