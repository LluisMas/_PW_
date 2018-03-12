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
import sys

class Client(object):
    """
    @param url: url where we are going to get the information
    @return: Returns the HTML of the URL
    """
    def get_web(self, url):

        try:
            f = urllib2.urlopen(url)
        except Exception as e:
            print "Something wrong happened with the URL"
            sys.exit(0)

        html = f.read()
        f.close()
        return html
    """
    @param html: html where we want to find the information.
    @return: Header that contains the title of the Book.
    """
    def parser(self, html ):
        soup = bs4.BeautifulSoup(html, "lxml")
        title = soup.find("div", "dotd-title")

        if title == None: return "No Book today"

        title_header = title.find("h2")

        if title_header == None: return "No Book today"
        if title_header.text == None: return "No Book today"

        return title_header.text

    """
    @return: Title of the daily book.
    """
    def run(self):
        url = "https://www.packtpub.com/packt/offers/free-learning?from=block"
        html = self.get_web(url)

        book = self.parser(html)

        if book == None: return

        return book.strip()


if __name__ == "__main__":
    client = Client()
    result = client.run()
    if result: print result
