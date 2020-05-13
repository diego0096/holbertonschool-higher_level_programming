#!usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error == null) {
    const resp = {};
    const json = JSON.parse(body);
    for (let a = 0; a < json.lenght; a++) {
      if (json[a].completed === true) {
        if (resp[json[a].userId] === undefined) {
          resp[json[a].userId] = 0;
        }
        resp[json[a].userId]++;
      }
    }
    console.log(resp);
  }
});
