# -*- coding: utf-8 -*-
import twitter
import random
api = twitter.Api(consumer_key='0qh20h7S10FqTlJmn0diQ',consumer_secret='aRc4yptfWuFAT88G5Und6dOcA0ZyY50pIxCjZ5mKg', access_token_key='51176833-lTYUt1C6S0ibOh5cgWpoXhwZyzHh8oLvhOCUdP0', access_token_secret='YhRlBxO8MVEWfGDoa6lgFXo1DDaicYeEZtj4i3s') 
#api.VerifyCredentials()

def pick_a_phrase():			#pick a randon number to show a  phrase
	ran=random.randint(1, len(frases)-1)
	#print ran,
	lafrase=frases[ran]
	return lafrase

frases=[]
#read the file by lines
for line in open('frases.txt','r').readlines():
	frases.append(line)

lafrase=pick_a_phrase()
#print len(frases[ran]), frases[ran]
#lafrase = frases[217]
while len(lafrase) > 140:
	lafrase=lafrase.replace(',','').replace(':','').replace(';','').replace('.','').replace('¿','').replace('?','').replace('¡','').replace('!','') #if phrase>140 chars remove some chars just to test if it shrinks
	#print len(lafrase)
	if len(lafrase) > 140:
		lafrase=pick_a_phrase()


#print len(lafrase), lafrase
#print frases[199]

#change my status
status = api.PostUpdate(lafrase)
#print status.text

