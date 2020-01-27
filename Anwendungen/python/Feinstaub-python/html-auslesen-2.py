import mechanize
import ClientForm
import lxml
import lxml.html
from lxml import html
from lxml import etree
from lxml.html import parse
from lxml.cssselect import CSSSelector

br = mechanize.Browser()
response = br.open("http://www.bergfex.at/oberoesterreich/wetter/stationen/linz/")
websitehtmlinhalt=br.response()

doc = html.parse(websitehtmlinhalt)
root = doc.getroot()
Temperatur = root.cssselect(('td'))[3]
TemperaturText = Temperatur.text

print (TemperaturText)