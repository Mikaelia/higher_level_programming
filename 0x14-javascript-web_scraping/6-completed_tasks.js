#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let taskCount = {
      '1': 0,
      '2': 0,
      '3': 0,
      '4': 0,
      '5': 0,
      '6': 0,
      '7': 0,
      '8': 0,
      '9': 0,
      '10': 0
    };
    const taskList = JSON.parse(body);
    for (const task of taskList) {
      if (task.completed === true) {
        taskCount[task.userId] += 1;
      }
    }
    console.log(taskCount);
  }
});
