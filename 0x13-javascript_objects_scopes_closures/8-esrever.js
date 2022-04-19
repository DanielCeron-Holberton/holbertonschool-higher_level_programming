#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  let sizeList = list.length - 1;

  for (let index = 0; index < list.length; index++, sizeList--) {
    newList[index] = list[sizeList];
  }

  return newList;
};
