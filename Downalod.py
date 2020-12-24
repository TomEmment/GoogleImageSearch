from bs4 import BeautifulSoup
import requests
import re
import urllib
from urllib.request import Request, urlopen
import os
import cookiejar
import json



query = input("query image: ")


url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
print(url)




header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}

req = Request(url, headers=header)

soup = urlopen(req).read()

soup = BeautifulSoup(soup.decode('utf-8'),features="html.parser")

links = soup.find_all('img', {'class': 'rg_i Q4LuWd'})
Number = 0 
for i in links:
    try:
        print(i["data-src"])
        response = requests.get(i["data-src"])

        file = open(query+str(Number)+".png", "wb")
        file.write(response.content)
        file.close()
        Number = Number + 1
    except:
        print("Unretrivable")
