#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response) {
    if (error) throw err;
    console.log('code: ' + response.statusCode);
});
