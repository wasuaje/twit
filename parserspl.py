# -*- coding: utf-8 -*-
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import urllib
import urllib2

# h1
#    attr: ('class', 'clear txt38 color000 MB10')

datosfin={}
atribs=[]

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
		if tag in ("h1","h2"):		
#			print "Start tag:", tag
			for attr in attrs:
				atribs.append(attr)
			datosfin[tag]={'att':atribs,'data':''}
			#print "     attr:", attr
#    def handle_endtag(self, tag):
#        print "End tag  :", tag
    def handle_data(self, data):
		if self.lasttag in ("h1","h2"):
			print "lastStart tag:", self.lasttag
#			print "lastag====",dir(self)
			print "Data     :", data
			datosfin[self.lasttag]['data']+=data
#    def handle_comment(self, data):
#        print "Comment  :", data
#    def handle_entityref(self, name):
#        c = unichr(name2codepoint[name])
#        print "Named ent:", c
#    def handle_charref(self, name):
#        if name.startswith('x'):
#            c = unichr(int(name[1:], 16))
#        else:
#            c = unichr(int(name))
#        print "Num ent  :", c
#    def handle_decl(self, data):
#        print "Decl     :", data

parser = MyHTMLParser()

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
#url='http://www.eluniversal.com/caracas/120824/no-te-engoriles-recopilo-su-trabajo-en-un-video'
url='http://www.eluniversal.com/nacional-y-politica/120824/evacuaron-a-80-personas-de-zonas-vulnerables-de-yaracuy'
req = urllib2.Request(url)
req.add_header('User-Agent', user_agent)
response = urllib2.urlopen(req)
data1 =response.read()
#print data1

a= parser.feed(data1)
#print a
print datosfin

