# -*- coding: utf-8 -*-
import twitter
import random    
import os
import sys
import time
import random
import sqlite3
import datetime
#duermo la ejecucion un nro de segundos para evitar filtro de twiter
ran=random.randint(1, 30)
#print ran
#time.sleep(ran)
 
twit_ids=[]
conn = sqlite3.connect('twitter.db')
c = conn.cursor()
cur=c.execute("select * from id_procs")
#es una lista#
data=cur.fetchall()
for i in data:
	twit_ids.append(i[0])
	

api = twitter.Api(consumer_key='0qh20h7S10FqTlJmn0diQ',consumer_secret='aRc4yptfWuFAT88G5Und6dOcA0ZyY50pIxCjZ5mKg', access_token_key='51176833-lTYUt1C6S0ibOh5cgWpoXhwZyzHh8oLvhOCUdP0', access_token_secret='YhRlBxO8MVEWfGDoa6lgFXo1DDaicYeEZtj4i3s') 

mylist=("metro_caracas","rhm1947", "EUtrafico","la_iguanatv",
"muyinteresante","UNoticias","ActualidadRT","IzarraDeVerdad" ,
"pascual_serrano","FUNVISIS", "Eduardo15Varela","WalterDossier","robertomalaver",
"maperezpirela","wikileaks","chavezcandanga","MMFlint","ElUniversal",
"MeridianoTV","liderendeportes","ElNacionalWeb","Diario_Vea","DiarioTalCual","diariopanorama",
"aporrea","CNNEE","lvbp_oficial","PresidencialVen", "globovision"

)

mylist_extended=("metro_caracas","Inspirulina","DeepakChopra","BlackberryVzla","QueLeer","Addictd2Success","rhm1947","trasnochocult", "EUtrafico","NUNEZML","la_iguanatv","muyinteresante","UNoticias","ActualidadRT","prodavinci","IzarraDeVerdad" ,"BorgesJorgeL",
"pascual_serrano","FUNVISIS","fragacarlos","MisionEmilio","QuinoTerapia","Asodepa","casciari","revistaorsai","maickelmelamed",
"MafaldaQuotes","sumitoestevez","elibravo", "Eduardo15Varela","WalterDossier","robertomalaver","AngelMendezM",
"maperezpirela","wikileaks","chavezcandanga","MMFlint","paulocoelho","MensajesDeBuda","DalaiLama_Citas","ElUniversal",
"MeridianoTV","liderendeportes","ElNacionalWeb","Diario_Vea","DiarioTalCual","diariopanorama","carvajalinop","El_Mostacho",
"aporrea","CNNEE","lvbp_oficial","PresidencialVen"

)
#print twit_ids

for tm in api.GetFriendsTimeline():
	if tm.user.screen_name in  mylist and tm.id not in twit_ids  :		
		#print tm.user.name,tm.user.screen_name,tm.text
		lafrase="RT @"+tm.user.screen_name
		lafrase+=" "+tm.text
		lafrase=lafrase[0:138]
		fecha=datetime.datetime.today()
		print "len: %s - frase: %s - id: %s" % (len(lafrase),lafrase.encode('utf8'),  tm.id)
		try:				
			#status = api.PostUpdate(lafrase)			
			#print "si inserta"
			#print "(%s,%s,%s)" % (tm.id,lafrase.encode('utf8'), fecha )
			c.execute("insert into id_procs (id,text,date) values (%s,'%s','%s')" % (tm.id,lafrase.encode('utf8'), fecha ))			
		except :
			print "Twitter error: ",  sys.exc_info()[1]
		#print lafrase
conn.commit()
