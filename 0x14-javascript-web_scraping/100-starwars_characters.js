#!/usr/bin/node
// prints all characters of a Star Wars movie
// using a movie ID

const process = require('process');
const request = require('request');
const movieId = process.argv[2];
const movieUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(movieUrl, (error, response, body) => {
  if (error) console.log(error);
  const obj = JSON.parse(body);
  for (const x of obj.characters) {
    const cId = x.split('/')[5];
    const charUrl = `https://swapi-api.hbtn.io/api/people/${cId}/`;
    request(charUrl, (err, response, body) => {
      if (err) console.log(err);
      const char = JSON.parse(body);
      console.log(char.name);
    });
  }
});
