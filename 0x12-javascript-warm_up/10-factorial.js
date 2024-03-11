#!/usr/bin/node
function factorial (number) {
  if (number < 0) {
    return (-1);
  } else if (number === 0 || isNaN(number)) {
    return (1);
  } else {
    return (number * factorial(number - 1));
  }
}
const num = process.argv[2];
const fac = factorial(num);
console.log(fac);
