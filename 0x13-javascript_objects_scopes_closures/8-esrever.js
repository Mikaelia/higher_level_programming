#!/usr/bin/node
exports.esrever = function (list) {
  let newList = [];
  let rIndex = list.length - 1;
  for (let i = 0; i < list.length; i++) {
    newList[i] = list[rIndex];
    rIndex--;
  }
  return newList;
};
