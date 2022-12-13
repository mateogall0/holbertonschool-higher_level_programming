#!/usr/bin/node
const btn = document.getElementById('red_header')
btn.addEventListener("click", function() {
  document.getElementsByTagName('header')[0].style.color = 'red'
});
