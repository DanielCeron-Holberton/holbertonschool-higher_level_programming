#!/usr/bin/node

exports.logMe = (function () {
  let times = 0;

  return (item) => {
    console.log(times + ':', item);
    times += 1;
  };
})();
