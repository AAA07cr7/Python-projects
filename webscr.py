

from pathlib import Path
from selenium import webdriver
from bs4 import BeautifulSoup
driver=r'C:\Users\HP\AppData\Local\Temp\Rar$EXa18176.42998\chromedriver.exe'
def get_html(url):
    browser=webdriver.Chrome(executable_path=driver)
    browser.get(url)
    return browser.page_source
    
def main():
    url='https://in.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck=bjmtuc.club'
    html=get_html(url)

    
    
    soup=BeautifulSoup(html,'lxml')
    cards=soup.find_all('div',class_='d-flex d-flex-row')
    for card in cards:
        
        
        price=card.find('span',class_='text-nowrap d-inline-block').text
        print(price)

if __name__ =='__main__':
    main()
