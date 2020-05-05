#!/usr/bin/node
// JS to print an array of string
'use strict';
const languages = ['C is fun', 'Python is cool', 'Javascript is amazing'];
for (const language in languages) {
  console.log(languages[language]);
}
