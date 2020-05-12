#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response) {
<<<<<<< HEAD
    if (error) throw err;
    console.log('code: ' + response.statusCode);
=======
  if (error == null) {
    console.log('code: ' + response.statusCode);
  }
>>>>>>> 7c546f23b18497d3a2519f119412753c78834ad2
});
