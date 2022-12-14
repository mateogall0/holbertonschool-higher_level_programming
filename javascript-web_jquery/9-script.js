#!/usr/bin/node

$.get('https://stefanbohacek.com/hellosalut/?lang=fr', function(data, status) {
  if (!status) return console.log('error')
  document.getElementById('hello').innerText = data['hello']
})
