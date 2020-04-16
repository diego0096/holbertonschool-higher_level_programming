#!/usr/bin/python3
# Script that fetches an url
import urllib.request as ur

with ur.urlopen('https://intranet.hbtn.io/status') as r:
    r = r.read()

print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(r), r))
print('\t- utf8 content: {}'.format(str(r, 'utf-8')))
