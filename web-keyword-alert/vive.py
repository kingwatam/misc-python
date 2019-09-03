import urllib.request, re, time, random, time, winsound, webbrowser
 
TARGET="April"
URL="https://store.htcvivecart.com/store/htcus/en_US/quickcart/ThemeID.40533800/OfferID.48383057001"
isFound=False
 
def check():
   f=urllib.request.urlopen(URL)
   source=f.read()
   res=re.match(".*"+TARGET,str(source),re.DOTALL)
   if res != None:
      print(TARGET + " found!")
      winsound.Beep(1000, 400)
      if isFound==False:
         global isFound
         isFound=True
         webbrowser.open(URL)
   else:
      print(TARGET + " not found.")
while True:
   check()
   time.sleep(10)
