#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w && h) {
      this.height = h;
      this.width = w;
    }
  }
};
