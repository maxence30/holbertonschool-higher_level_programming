#!/usr/bin/node

const languages = [
  'C is fun',
  'Python is cool',
  'JavaScript is amazing'
];

let i = 0;
let result = '';

while (i < languages.length) {
  result += languages[i] + '\n';
  i++;
}

console.log(result.trim());