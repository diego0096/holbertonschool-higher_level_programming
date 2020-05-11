#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const nlist = list.map((a, b) => a * b);
console.log(nlist);
