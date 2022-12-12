#!/usr/bin/node
const r = require('request');

r(process.argv[2], function (error, response, body) {
  if (error) return;
  const dict = JSON.parse(body);
  const final = {};
  dict.forEach(element => {
    if (element.completed) {
      if (final[element.userId]) final[element.userId] += 1;
      else final[element.userId] = 1;
    }
  });
  console.log(final);
});
