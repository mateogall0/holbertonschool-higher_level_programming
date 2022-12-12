#!/usr/bin/node
const r = require('request');

r('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, response, body) {
  if (error) return;
  console.log(JSON.parse(body).title);
});
