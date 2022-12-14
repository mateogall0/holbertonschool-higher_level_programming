#!/usr/bin/node
const btn = document.getElementById('update_header')
const h = document.getElementsByTagName('header')[0]
btn.addEventListener("click", function() {
  h.innerHTML = ('New Header!!!')
});
