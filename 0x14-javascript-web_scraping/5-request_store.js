#!/usr/bin/node

const request = require('request');
let fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const content = body;
    fs.writeFile(filePath, content, function (err, file) {
      if (err) {
        console.log(err);
      }
    });
  }
});
