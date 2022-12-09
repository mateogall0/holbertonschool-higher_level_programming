#!/usr/bin/node
const Sq = require('./5-square');

module.exports = class Square extends Sq {
  charPrint (c) {
    if (!c) c = 'X';
    for (let i = 0; i < this.width; i++) {
      for (let j = 0; j < this.height; j++) {
        process.stdout.write(c);
      }
      console.log();
    }
  }
};
