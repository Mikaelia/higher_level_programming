#!/usr/bin/node

let textFile = process.argv[2];
let text = process.argv[3];
let fs = require('fs');

fs.writeFile(textFile, text, "utf-8", function (err, file) {
    if (err) {
        console.log(err);
    } 
});