#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print() {
    const stringPrint = `${"X".repeat(this.width)}\n`.repeat(this.height);
    console.log(stringPrint.substring(0, stringPrint.length - 1));
  }
  rotate() {
    [this.height, this.width] = [this.width, this.height];
  }
  double() {
    [this.height, this.width] = [this.height * 2, this.width * 2];
  }
}

module.exports = Rectangle;
