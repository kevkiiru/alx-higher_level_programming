#!/usr/bin/node

const { argv } = require('process');
const number = parseInt(argv[2]);
for (let a = 0; a < number; a++) {
  console.log('C is fun');
}
