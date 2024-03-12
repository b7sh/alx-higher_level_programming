#!/usr/bin/node
const saverList = [];
exports.logMe = function (item) {
  saverList.push(item);
  if (saverList.length >= 3) {
    for (let i = 0; i < saverList.length; i++) {
      console.log(`${i}: ${saverList[i]}`);
    }
  }
};
