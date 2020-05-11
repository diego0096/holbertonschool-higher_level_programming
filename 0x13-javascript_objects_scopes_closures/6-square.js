#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
}

Square.prototype.charPrint = function (c) {
  if (!c) {
    c = 'X';
  }
  for (let i = 0; i < this.width; i++) {
    console.log(c.repeat(this.width));
  }
};

module.exports = Square;
