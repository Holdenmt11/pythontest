import urllib, os, sys, time
from secret import *
import tweepy

#argfile = str(sys.argv[1])

myloc = r"C:\Anaconda\streetviewtest\pics" #replace with your own location
key1 = "&key=" + streetview

#fn = r"C:\Anaconda\streetviewtest\441 4th Street NW, Washington DC.jpg"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

filename=open('C:\Anaconda\streetviewtest\streets.txt', 'r')
f=filename.readlines()
filename.close() 


#for line in f:
#    api.update_status(status=line)
#    time.sleep(120)



#api.update_with_media(fn, "441 4th St NW")

#os.remove(fn)
    


def GetStreet(Add,SaveLoc):
  base = "https://maps.googleapis.com/maps/api/streetview?size=1000x1000&location="
  MyUrl = base + Add + key1
  fi = Add + ".jpg"
  urllib.urlretrieve(MyUrl, os.path.join(SaveLoc, fi))

#Tests = ["1600 t st nw, washington dc"]

for i in f:    
    GetStreet(Add=i,SaveLoc=myloc)
  
  
