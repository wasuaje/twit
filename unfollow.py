# -*- coding: utf-8 -*-
import twitter
import random
api = twitter.Api(consumer_key='0qh20h7S10FqTlJmn0diQ',consumer_secret='aRc4yptfWuFAT88G5Und6dOcA0ZyY50pIxCjZ5mKg', access_token_key='51176833-lTYUt1C6S0ibOh5cgWpoXhwZyzHh8oLvhOCUdP0', access_token_secret='YhRlBxO8MVEWfGDoa6lgFXo1DDaicYeEZtj4i3s') 
#api.VerifyCredentials()
# para serializar, es decir guardar en disco la lista de seguidores
try:  
    import cPickle as pickle  
except ImportError:  
    import pickle  

#Diccionario con direcciones de correo
dirs={}
dirs["sysadmin"]="wasuaje@eluniversal.com"

def send_mail():
	import smtplib
	# Import the email modules we'll need
	from email import MIMEText
	# Open a plain text file for reading.  For this example, assume that
	# the text file contains only ASCII characters.
	fp = open("ratas.txt", 'rb')
	# Create a text/plain message
	msg = MIMEText.MIMEText(fp.read())
	fp.close()

	for mail in dirs.keys():
		msg['Subject'] = "Resumen de unfollow"
		msg['From'] = "wasuaje@hotmail.com"
		msg['To'] = dirs[mail]
		prueba = dirs[mail]
		# Send the message via our own SMTP server, but don't include the envelope header.
		s = smtplib.SMTP('10.3.0.130')		
		s.sendmail(msg['From'], msg['To'],  msg.as_string())
		s.quit()

#obtengo los datos actuales, es decir hasta la ves anterior que guarde,  ayer normalmente
fichero = file("followers.dat")  
gente = pickle.load(fichero)  
fichero.close() 
ayer=len(gente['ids'])

#actualizo la data con los nuevos valores
fls=api.GetFollowerIDs()
hoy=len(fls['ids'])
fichero = file("followers.dat", "w")  
#escribo en el dump
pickle.dump(fls, fichero, 2)  
fichero.close() 
 
#comparo para ejecutar acciones segun se necesite
 
if hoy > ayer: #si aumento el numero de seguidores
	sta=1
	msg="Ayer me seguian: %s personas, hoy me siguen: %s - %s Nuevos seguidores - Followers.py - @wasuaje" % (ayer ,  hoy,  int(hoy-ayer))
elif hoy==ayer: #si todo esta igual
	sta=0
	msg="Me siguen el mismo numero de personas que ayer: %s personas - Followers.py - @wasuaje" % (ayer)
else: #si perdi seguidores
	sta=-1
	msg="Ayer me seguian: %s personas, hoy me siguen: %s - Perdi %s seguidores -  Followers.py - @wasuaje" % (ayer ,  hoy,  int(hoy-ayer))
print msg

#al final publico en el timeline de twiter
status = api.PostUpdate(msg)

#gente=ayer, fls=hoy

if sta==1:
	msg="Nuevos seguidores: \n"
	for i in fls:
		if i not in gente['ids']:
			h=api.GetUser(i)
			msg+=h.GetScreenName()+"\t"+h.GetName()+"\n"	
	print msg
elif sta==-1:
	msg="Te dejaron de seguir: \n"
	for i in gente:
		if i not in fls['ids']:
			h=api.GetUser(i)
			msg+=h.GetScreenName()+"\t"+h.GetName()+"\n"
	print msg
fichero = file("ratas.txt", "w") 
fichero.write(msg)
fichero.close()
send_mail()
	
	
	
	
	
	

