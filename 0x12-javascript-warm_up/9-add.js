#!/usr/bin/node
// js to print the addition of two integers
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
add(process.argv[2], process.argv[3]);
