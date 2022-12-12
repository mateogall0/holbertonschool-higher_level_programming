#!/usr/bin/node
const argv = require('process').argv;

const f = require('fs');
f.readFile(argv[2], 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
