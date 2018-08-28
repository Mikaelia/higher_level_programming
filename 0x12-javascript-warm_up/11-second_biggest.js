#!/usr/bin/nodejs

let myArray = [];
process.argv.forEach(function (element, index) {
  if (index > 1) {
    myArray.push(element);
  }
});

if (myArray.length === 0 || myArray.length === 1) {
  console.log(0);
} else {
  myArray.sort(function (a, b) { return a - b; });
  console.log(myArray[myArray.length - 2]);
}
