#!/usr/bin/node
let request = require('request');
request.get('http://swapi.co/api/films/' + process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    let charList = [];
    for (let chars of JSON.parse(body).characters) {
      charList.push(new Promise(function (resolve, reject) {
        request.get(chars, function (error, response, body) {
          if (error) {
            console.log(error);
          } else if (response.statusCode === 200) {
            resolve(JSON.parse(body).name);
          } else {
            reject(Error('It broke'));
          }
        });
      }));
    }
    Promise.all(charList).then(function (names) {
      names.forEach(function (name) {
        console.log(name);
      });
    });
  }
});
