#!/usr/bin/env python
# -*- coding: utf-8 -

###
# run command
# $ watch ./web-statsroyale-tournaments.py
#
# that can get now free to join tournaments
###

import urllib.request
import lxml.html
from lxml.cssselect import CSSSelector
from bs4 import BeautifulSoup

url = "https://statsroyale.com/tournaments"
request_headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
}

request = urllib.request.Request(url, headers=request_headers)
contents = urllib.request.urlopen(request).read()

root = lxml.html.fromstring(contents)
sel = CSSSelector("div .challenges__rowContainer")
results = sel(root)

for result in results:
    trimContent = lxml.html.tostring(result)
    soup=BeautifulSoup(trimContent, "lxml")
    text = soup.get_text(" | ", strip=True)
    infos = text.split(" | ")
    infos.pop(1)
    infos.pop(-1)
    infos.pop(-1)
    infos.pop(-1)

    players = infos[1]
    if players != "50/50":
        info = " | "
        print(info.join(infos))

