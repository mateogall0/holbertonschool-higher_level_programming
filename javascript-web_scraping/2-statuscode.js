#!/usr/bin/node
const r = require('request');

r(process.argv[2], function (error, response, body) {
  if (error || !error) console.log('code:', response.statusCode);
});
