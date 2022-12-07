#!/usr/bin/node
const argv = require('process').argv;

if (!argv[2] || !argv[3]) {
  console.log(0);
} else {
  let tmp = +argv[2];
  for (let i = 2; i < argv.length; i++) {
    if (tmp < +argv[i]) {
      tmp = +argv[i];
    }
  }
  console.log(tmp);
}
