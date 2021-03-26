# -*- coding: utf-8 -*-
import twitter
import sqlite3
import datetime
import math
import time
import sys

print "Hora de inicio: %s" % datetime.datetime.today()
#conexion y autenticacion
api = twitter.Api(consumer_key='0qh20h7S10FqTlJmn0diQ',consumer_secret='aRc4yptfWuFAT88G5Und6dOcA0ZyY50pIxCjZ5mKg', access_token_key='51176833-lTYUt1C6S0ibOh5cgWpoXhwZyzHh8oLvhOCUdP0', access_token_secret='YhRlBxO8MVEWfGDoa6lgFXo1DDaicYeEZtj4i3s') 
#nro de twits disponibles
TOTAL=1000
HOURS=13
#_perhour=TOTAL/HOURS #83 
#modificiacion para hacerlo cada 10 min con info mas actual
_perhour=10
_permin=_perhour/60  #1.3
#_sleep=3600/_perhour #43 secs
_sleep=60
twits=[]
conn = sqlite3.connect('twitter.db')
c = conn.cursor()
cur=c.execute('''  SELECT text from id_procs  where  date > datetime('now' ,'-10 minutes','localtime')  order by random() limit %s ; ''' % _perhour )
#es una lista#
data=cur.fetchall()
_count=len(data)
_persec=float(_count)/float(60)
_persec=math.ceil(_persec)

for i in data:
	twits.append(i[0])
	
print "Total twits: %s - T/minuto: %s" % (_count, _permin)
#del minuto 1 al minuto 60

for t in range(0, _count-1):
	try:
		#print twits[t]	
		status = api.PostUpdate(twits[t])
		#print "Pausa de %s segundos" % (60/int(_persec))
		time.sleep(_sleep)
	except :
		print "Twitter error: ",  sys.exc_info()[1]	
		
print "Hora de Fin: %s" % datetime.datetime.today()

