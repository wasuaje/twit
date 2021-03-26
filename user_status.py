# -*- coding: utf-8 -*-
import twitter
import random
api = twitter.Api(consumer_key='0qh20h7S10FqTlJmn0diQ',consumer_secret='aRc4yptfWuFAT88G5Und6dOcA0ZyY50pIxCjZ5mKg', access_token_key='51176833-lTYUt1C6S0ibOh5cgWpoXhwZyzHh8oLvhOCUdP0', access_token_secret='YhRlBxO8MVEWfGDoa6lgFXo1DDaicYeEZtj4i3s') 
#api.VerifyCredentials()

#userid=api.GetFriendIDs()
#for i in userid['ids']:
#	user=api.GetUser(i)
#	userdict=user.AsDict()
#	print userdict['id'],userdict['name'],
#	if 'status' in userdict:
#		print userdict['status']['text']
#	else:
#		print "NO HA ACTUALIZADO SU STATUS"

statuses=api.GetFriends()
print len(statuses)
for s in statuses:
	users=s.AsDict()
	print users['name'],
	if 'status' in users:
		print users['status']['text']

