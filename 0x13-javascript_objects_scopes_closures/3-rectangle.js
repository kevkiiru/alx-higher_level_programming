#!/usr/bin/node

// class rectangle

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
  for (let a = 1; a <= this.height; a++) {
    let row = '';
    for (let b = 1; b <= this.width; b++) row += 'X';
    console.log(row);
  }
 }
}

module.exports = Rectangle;
