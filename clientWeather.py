#!/usr/bin/env python
# -*- coding: utf-8 -*-


import urllib2
import bs4

class Client(self):
    def get_web(self, url):
        f = urllib2.urlopen(url)
        html = f.read()
        f.close()
        return html


    def run(self):
        url =

            

    if __name__ == "__main__":
        client = Client()
        client.run()
