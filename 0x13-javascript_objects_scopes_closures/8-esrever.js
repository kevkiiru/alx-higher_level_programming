#!/usr/bin/node

exports.esrever = function (list) {
  const reverseList = [];
  for (let a = list.length - 1; a >= 0; a--) {
    reverseList.push(list[a]);
  }
  return reverseList;
};
