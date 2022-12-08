#!/usr/bin/node
const argv = require('process').argv;

if (!argv[2] || !argv[3]) {
  console.log(0);
} else {
  console.log(argv.slice(2).sort().reverse()[1]);
}
