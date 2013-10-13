import json 
d = open('lawrences.json', 'rb')
data= d.read()
lines = data.split("\n")
import pprint
pp = pprint.PrettyPrinter(indent=4)
import traceback 

users={}

for line in lines[3:] :

    try:
        pos = line.find("{u'") 
        if  pos > -1 :
#            print "read: %d : %s" % (pos,line)
#            print "at: %s" % (line[pos:])
            tweet = eval(line)
 
            
            if u'geo' in tweet :
                if tweet[u'geo'] is not None :
#                    print "geo :%s" % tweet[u'geo']
                    if u'coordinates' in tweet[u'geo']:
#                        print "coords: %s" % tweet[u'geo'][u'coordinates']
                        coords= tweet[u'geo'][u'coordinates']
#                        print "coords2: %s" % coords
                        lat = coords[0]
                        lon = coords[1]
                        # u'geo': {   u'coordinates': [38.5754414, -97.6394557], u'type': u'Point'},
                        if lat <= 39.03 and lat >= 38.85 :
                            if lon <= -95.09 and lon >= -95.49 :
                                #print tweet
                                #pp.pprint(tweet)
                                users[tweet[u'user'][u'screen_name']]=1

    except Exception, e:
        #print "problem read %s" % line
        traceback.print_exc()
        print e
        #raise e
 
for x in users.keys():
     print "<a href=https://twitter.com/%s>%s</a>" % (x,x)
