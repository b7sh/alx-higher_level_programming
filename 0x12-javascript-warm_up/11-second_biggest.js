#!/usr/bin/node
if (process.argv.length < 4) {
  console.log('0');
} else {
  const firstArray = process.argv.slice(2).map(Number);
  const secondArray = firstArray.sort((a, b) => b - a)[1];
  console.log(secondArray);
}
