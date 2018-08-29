#!/usr/bin/nodejs

const number = parseInt(process.argv[2]);
number ? console.log('My number: ' + number) : console.log('Not a number');
