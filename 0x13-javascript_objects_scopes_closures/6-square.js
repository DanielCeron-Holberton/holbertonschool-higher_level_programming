#!/usr/bin/node

const Rectangle = require("./4-rectangle");

class Square extends Rectangle {
  constructor(size) {
    super(size, size);
    this.name = "Square";
  }
  charPrint(char) {
	if (!char) {
		char = 'X';
	}
	const stringPrint = `${char.repeat(this.width)}\n`.repeat(this.height);
    console.log(stringPrint.substring(0, stringPrint.length - 1));
  }
}
module.exports = Square;
