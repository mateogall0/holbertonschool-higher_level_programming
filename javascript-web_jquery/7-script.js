#!/usr/bin/node
const ch = document.getElementById('character');
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function(data, status) {
  if (!status) return console.log('error')
  ch.innerHTML = data['name']
})
