#!/usr/bin/node
const argv = require('process').argv

console.log(factorial(+argv[2]))

function factorial(n) {
  if (isNaN(n) || n == 1) {
    return (1);
  }
  if (n < 0) {
    return (-1);
  }
  return (n * factorial(n - 1));
}
