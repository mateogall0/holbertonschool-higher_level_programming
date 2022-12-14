#!/usr/bin/node
const list = document.getElementById('list_movies')

$.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data, status) {
  if (!status) return console.log('error')
  for (const [key, value] of Object.entries(data['results'])) {
    list.innerHTML += '<li>'+ value['title'] +'</li>'
  }
})
