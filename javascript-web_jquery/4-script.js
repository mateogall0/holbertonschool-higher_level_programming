#!/usr/bin/node
const btn = document.getElementById('toggle_header')
btn.addEventListener("click", function() {
  document.getElementsByTagName('header')[0].classList.toggle(document.getElementsByTagName("header")[0].classList.contains('red') ? 'green': 'red')
});
