#!/usr/bin/nodejs

const myString = 'C is fun';

let i;
while (i < process.argv[2]) {
  console.log(myString);
  i++;
}
