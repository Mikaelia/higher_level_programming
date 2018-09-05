#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    const data = JSON.parse(body);
    const movieList = (data.results);
    for (let movie of movieList) {
      const list = movie.characters;
      for (let character of list) {
        if (character === 'https://swapi.co/api/people/18/') {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
