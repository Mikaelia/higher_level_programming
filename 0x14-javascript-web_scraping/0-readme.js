#!/usr/bin/node

let textFile = process.argv[2];
let fs = require('fs');

fs.readFile(textFile, "utf-8", function (err, file) {
    if (err) {
        console.log(err);
    } else {
    console.log(file)
    }
});