import urllib, os
from secret import *

myloc = r"C:\Anaconda\streetviewtest" #replace with your own location
key = streetview

def GetStreet(Add,SaveLoc):
  base = "https://maps.googleapis.com/maps/api/streetview?size=1200x800&location="
  MyUrl = base + Add + key
  fi = Add + ".jpg"
  urllib.urlretrieve(MyUrl, os.path.join(SaveLoc,fi))

Tests = ["441 4th Street NW, Washington DC"]

for i in Tests:
  GetStreet(Add=i,SaveLoc=myloc)