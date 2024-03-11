#!/usr/bin/node
if (process.argv.length < 4) {
  console.log('NaN');
} else {
  const sum;
  sum = Number(process.argv[2]) + Number(process.argv[3]);
  console.log(sum);
}
