#!/usr/bin/node
const list = document.getElementsByClassName('my_list')[0]
const btn = document.getElementById('add_item')
btn.addEventListener("click", function() {
  list.innerHTML += ('<li>Item</li>')
});
