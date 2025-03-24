import requests
from bs4 import BeautifulSoup

def haber_linklerini_getir(sayfa_url):
    r = requests.get(sayfa_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    haber_listesi = soup.find_all("div", {"class": "f-cat f-item"})

    for i in haber_listesi:
        print("===================================")
        for b in i.findAll("ul", {"class": "list underline"}):
            for link in b.findAll('a'):
                my_link = link.get('href')
                tam_link = f"https://www.milligazete.com.tr{my_link}"
                print(tam_link)
                with open('ist.txt', 'a', encoding="utf-8") as file:
                    file.write(tam_link + "\n")

listem=['https://www.milligazete.com.tr/arsiv/2025-03-22','https://www.milligazete.com.tr/arsiv/2025-03-23','https://www.milligazete.com.tr/arsiv/2025-03-24']
for s in listem:
    haber_linklerini_getir(s)
