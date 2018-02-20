#!/usr/bin/env python
# -*- coding: utf-8 -*-# vim: set fileencoding=utf8 :
# vim: set fileencoding=utf8 :

'''
Packtpub's daily day name

Created on 02/20/2018

@author LluisMas
'''

import urllib2
import bs4

class Client(object):

    def get_web(self, url):
        f = urllib2.urlopen(url)
        html = f.read()
        f.close()
        return html

    def parser(self, html ):
        soup = bs4.BeautifulSoup(html, "lxml")
        title = soup.find("div", "dotd-title")

        if title == None: return

        title_header = title.find("h2")

        if title_header == None: return
        if title_header.text == None: return

        return title_header.text


    def run(self):
        url = "https://www.packtpub.com/packt/offers/free-learning?from=block"
        html = self.get_web(url)

        book = self.parser(html)

        if book == None: return

        print book.strip()


if __name__ == "__main__":
    client = Client()
    client.run()
