#!/usr/bin/node
const Square1 = require('./5-square');
class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let square = '';
      for (let j = 0; j < this.width; j++) {
        square += c;
      }
      console.log(square);
    }
  }
}
module.exports = Square;
