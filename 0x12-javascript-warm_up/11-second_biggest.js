#!/usr/bin/nodejs

var myArray = [];
process.argv.forEach(function (element, index) {
  if (index > 1) {
    myArray.push(element);
  }
});

myArray.sort(function (a, b) { return a - b; });

console.log(myArray[myArray.length - 2]);
