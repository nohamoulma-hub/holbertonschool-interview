#!/usr/bin/node
const request = require('request'); // module pour faire des appels HTTP

const movieId = process.argv[2]; // ID du film passé en argument (ex: "3")
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';

// 1er appel: on récupère les infos du film
request(`${baseUrl}${movieId}/`, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const film = JSON.parse(body); // body est du texte JSON -> objet JS
  const characterUrls = film.characters; // tableau d'URLs de personnages

  const names = new Array(characterUrls.length); // tableau vide, taille fixe
  let count = 0; // compte le nombre de réponses déjà reçues

  // pour chaque URL de personnage, on lance un appel HTTP
  characterUrls.forEach((url, index) => {
    request(url, (err, res, charBody) => {
      if (err) {
        console.error(err);
        return;
      }

      const character = JSON.parse(charBody);
      names[index] = character.name; // on range le nom à sa position d'origine
      count += 1; // une réponse de plus est arrivée

      // quand toutes les réponses sont arrivées, on affiche dans l'ordre
      if (count === characterUrls.length) {
        names.forEach((name) => console.log(name));
      }
    });
  });
});
