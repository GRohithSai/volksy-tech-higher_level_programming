#!/usr/bin/node
const request = require('request');
const baseUrl = 'https://swapi-api.hbtn.io/api/films/';
const filmId = process.argv[2];
request.get(baseUrl + filmId, (err, response, body) => {
  if (err === null) {
    const data = JSON.parse(body);
    console.log(data.title);
  } else {
    console.log(err);
  }
});
