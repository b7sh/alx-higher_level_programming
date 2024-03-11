#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  let num = process.argv[2];
  num = Number(num);
  console.log(`My number: ${num}`);
}
