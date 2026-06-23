#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';

request(`${baseUrl}${movieId}/`, (error, response, body) => {
  const film = JSON.parse(body);
  const characterUrls = film.characters;
  const names = new Array(characterUrls.length);
  let count = 0;

  characterUrls.forEach((url, index) => {
    request(url, (err, res, charBody) => {
      const character = JSON.parse(charBody);
      names[index] = character.name;
      count += 1;

      if (count === characterUrls.length) {
        names.forEach((name) => console.log(name));
      }
    });
  });
});
