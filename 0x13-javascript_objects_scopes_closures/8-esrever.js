#!/usr/bin/node

exports.esrever = function (list) {
  const reverseList = [];
  for (let a = list.lenght - 1; a >= 0; a--) {
    reverseList.push(list[a]);
  }
  return reverseList;
};
