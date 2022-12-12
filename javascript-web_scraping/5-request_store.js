#!/usr/bin/node
const r = require('request');
const f = require('fs');

r(process.argv[2], function (error, response, body) {
  if (error) return;

  f.writeFile(process.argv[3], body, function (err, data) {
    if (error) console.log(err);
  });
});
