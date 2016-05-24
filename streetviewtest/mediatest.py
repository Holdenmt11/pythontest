import urllib, os, sys, time
from secret import *
import tweepy
from streets import address

#argfile = str(sys.argv[1])

myloc = r"C:\Users\Matthew\pythontest\streetviewtest\pics" #replace with your own location
key1 = "&key=" + streetview

#fn = r"C:\Anaconda\streetviewtest\441 4th Street NW, Washington DC.jpg"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

#filename=open('C:\Users\Matthew\pythontest\streetviewtest\streets.txt', 'r')
#f=filename.readlines()
#filename.close() 


#for line in f:
#    api.update_status(status=line)
#    time.sleep(120)



#api.update_with_media(fn, "441 4th St NW")

#os.remove(fn)
    


def GetStreet(Add,SaveLoc):
  base = "https://maps.googleapis.com/maps/api/streetview?size=1000x1000&location="
  MyUrl = base + Add +'Washington DC'+ key1
  fi = Add + ".jpg"
  urllib.urlretrieve(MyUrl, os.path.join(SaveLoc, fi))

#Tests = ["1600 t st nw, washington dc"]

#for i in address:   
	
	
def streetupload(Add2):
	base2 = Add2 + ".jpg"
	base3 = os.path.join(myloc, base2)
	api.update_with_media(base3, Add2)
	
for i in address:
	GetStreet(Add=i,SaveLoc=myloc)
	streetupload(Add2=i)
	time.sleep(60)
