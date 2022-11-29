#!/usr/bin/node

const { argv } = require('process');
const number = parseInt(argv[2]);
if (!number) {
  console.log('Missing size');
} else {
  for (let a = 0, a < number; a++) {
    let concat = '';
    for (let b = 0; b < number; b++) {
      concat += 'X';
    }
    console.log(concat);
  }
}
