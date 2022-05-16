
import requests,webbrowser
from bs4 import BeautifulSoup

userinput=input("Enter something to search")

google_search=requests.get("https://www.google.com/search?q="+userinput)

soup=BeautifulSoup(google_search.text,'html.parser')

search_results=soup.select('.BNeawe a')

for link in search_results[:5]:
    Lnk=(link.get('href'))
    webbrowser.open('https://www.google.com/'+Lnk)
