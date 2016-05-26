# -*- coding: utf-8 -*-
"""
Created on Wed May 25 19:13:57 2016

@author: Matthew
"""

import urllib, os 
from secret import *
import tweepy
import sqlite3

#argfile = str(sys.argv[1])

#place to temporarily store google street view images
myloc = r"C:\arcgis\streetviewtest" 


#builds streetview API key
key1 = "&key=" + streetview


#authorizes twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

#connects to the address database
conn = sqlite3.connect(r'C:\arcgis\resources\database.sqlite')



#query to get first nontweeted record
Query = """Select * FROM lots7
where tweet =' ' 
ORDER BY OBJECTID ASC 
LIMIT 1"""



#function that builds the streetview url with XY if no House Number, downloads the image, then posts to twitter
def GetStreetXY(Add,Add2,Add3,SaveLoc):
  base = "https://maps.googleapis.com/maps/api/streetview?size=1000x1000&location="
  MyUrl = base + Add+','+Add2 +key1
  fi = Add3 + ".jpg"
  urllib.urlretrieve(MyUrl, os.path.join(SaveLoc, fi))
  fi2= os.path.join(SaveLoc, fi)
  api.update_with_media(fi2, Add3)
  os.remove(fi2)

#function that builds the streetview url with House Number, downloads image, then posts to twitter
def GetStreetAdd(Add3,SaveLoc):
  base = "https://maps.googleapis.com/maps/api/streetview?size=1000x1000&location="
  MyUrl = base + Add3+' '+'Washington DC' +key1
  fi = Add3 + ".jpg"
  urllib.urlretrieve(MyUrl, os.path.join(SaveLoc, fi))
  fi2= os.path.join(SaveLoc, fi)
  api.update_with_media(fi2, Add3)
  os.remove(fi2)
  
  
#function that marks an address as tweeted
def mark_as_tweeted(robot):
   conn.execute("UPDATE lots7 SET tweet ='yes' where id2=" + robot)
   conn.commit()


#sends query to database
cursor = conn.execute(Query)


#calls the two functions
for row in cursor: 
    if row[4]==' ':
        GetStreetXY(Add=row[14],Add2=row[15], Add3=row[11],SaveLoc=myloc)
    else:
        GetStreetAdd(Add3=row[11],SaveLoc=myloc)    
    test2 = row[16]   
    mark_as_tweeted(robot=test2)


    
#closes connection to database    
conn.close()
