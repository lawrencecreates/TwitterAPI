from secret import consumer_key, consumer_secret, access_token_key, access_token_secret

from TwitterAPI import TwitterAPI
api = TwitterAPI(
    consumer_key(), 
    consumer_secret(), 
    access_token_key(), 
    access_token_secret())

# south park
#lat=38.96194491354418
#lng=-95.23592948913574
#location = '%s,%s' % (lat,lng)


#38.85174028464973, -95.4873275756836 # SW
#39.03278609790772, -95.0925064086914 # NE
bbox = '-95.49, 38.85,-95.09,39.03'

#bbox = '38.85174028464973,-95.4873275756836, 39.03278609790772, -95.0925064086914'



print bbox

r = api.request('statuses/filter', {'locations': bbox})
for item in r.get_iterator():
    print item
