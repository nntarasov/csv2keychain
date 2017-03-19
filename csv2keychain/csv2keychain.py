# -*- coding: utf-8 -*-

"""csv2keychain.csv2keychain: primary module within the csv2keychain package."""

from urllib.parse import urlparse
from subprocess import call
from sys import argv
import csv


class Csv2Keychain:

    def addkey(self, params, update):
        name, url, username, password = params
        url = urlparse(url)
        domain = url.netloc
        path = url.path

        syscall = ['security', 'add-internet-password',
              '-l', domain + ' (' + username + ')',
              '-s', domain,
              '-p', path,
              '-a', username,
              '-t', 'form',
              '-r', "{:<4}".format(url.scheme[0:4]),
              '-T', '/Applications/Safari.app',
              '-w', password]
        if update:
            syscall.append('-U')
        call(syscall)

    def __init__(self):
        script, csvpath = argv[:2]
        params = argv[2:]

        overwrite = '-u' in params
        displayrow = '-s' in params

        with open(csvpath, newline='') as csvfile:
            reader = csv.reader(csvfile)
            print('File opened')
            counter = 1
            next(reader)  # Skip heading
            for row in reader:
                print('Copying item #%s...' % str(counter))
                if displayrow:
                    print(row)

                self.addkey(row, overwrite)
                print('#%s complete' % str(counter))
                counter += 1
