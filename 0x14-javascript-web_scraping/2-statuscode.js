#!/usr/bin/node
cont request = require('request');
request(procees.argv[2], function (eror, response) {
    if (error == null) {
        console.log('code: ' + response.statusCode);
    }
});
