#!/usr/bin/node
const argv = require('process').argv;

const f = require('fs');
f.readFile(argv[2], 'utf8', function (err, data) {
  console.log(data || err);
});
