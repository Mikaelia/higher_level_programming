#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let elem of list) {
    if (searchElement === elem) {
      count += 1;
    }
  }
  return count;
};
