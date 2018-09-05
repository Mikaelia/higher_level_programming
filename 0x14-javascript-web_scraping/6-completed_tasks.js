#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let taskCount = {};
    const taskList = JSON.parse(body);
    for (const task of taskList) {
      if (task.completed === true) {
        let id = task.userId;
        if (taskCount[id] === undefined) {
          taskCount[id] = 1;
        } else {
          taskCount[id] += 1;
        }
      }
    }
    console.log(taskCount);
  }
});
