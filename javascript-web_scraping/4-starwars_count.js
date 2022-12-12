#!/usr/bin/node
const r = require('request');

r(process.argv[2], function (error, response, body) {
  if (error) return;
  console.log(body.split('people/18/').length - 1);
});
