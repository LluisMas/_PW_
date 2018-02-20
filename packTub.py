#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
        activitats = soup.find_all("div", "dotd-title")

        for activitat in activitats:
            titol_html = activitat.find("span", "flink-title")
            titol = titol_html.text
            link_html = activitat.find("a")
            link = link_html["href"]

            print titol, "--", link

        return activitats

    def run(self):
        url = "https://www.packtpub.com/packt/offers/free-learning?from=block"
        html = self.get_web(url)
        activitats = self.parser(html)

        #exec

if __name__ == "__main__":
    client = Client()
    client.run()
