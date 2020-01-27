#import mechanize
#import BeautifulSoup
import re
#from BeautifulSoup import BeautifulSoup
import lxml
from lxml import etree
#import StringIO

SHOW_COOKIES = True

#br = mechanize.Browser()

if SHOW_COOKIES:
    cj = mechanize.CookieJar()
    br.set_cookiejar(cj)

response = br.open("http://192.168.178.193")

#if SHOW_COOKIES:
#    for cookie in cj:
#        print cookie

assert br.viewing_html()
#print '\n-----> Website title <-----'
#print br.title()
#print '\n-----> Website url <-----'
#print br.geturl()
#print '\n-----> Website header <-----'
#print response.info()  # headers
#print '\n-----> Website body <-----'
#print response.read()  # body

websitehtmlinhalt=br.response()