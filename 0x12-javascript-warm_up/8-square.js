#!/usr/bin/nodejs

const size = parseInt(process.argv[2]) || 'Missing size';

for (let i = 0; i < size; i++) {
  let myString = '';
  for (let j = 0; j < size; j++) {
    myString += 'X';
  }
  console.log(myString);
}
