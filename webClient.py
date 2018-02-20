#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2

class Client(object):

    def get_web():
        f = urllib2.urlopen("http://www.eps.udl.cat")
        html = f.read()
        f.close()
        return html

    def run(self):
        html = self.get_web("http://www.eps.udl.cat")
        #parse
        #exec

        print html

if __name__ == "__main__":
    client = Client()
    client.run()
