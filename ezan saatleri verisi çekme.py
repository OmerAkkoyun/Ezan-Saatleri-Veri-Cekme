import requests
from bs4 import BeautifulSoup
url="https://www.huzursayfasi.com/namaz-vakitleri/istanbul-sultanbeyli-namaz-vakitleri.html"
response= requests.get(url)
html_icerigi=response.content
soup=BeautifulSoup(html_icerigi,"html.parser")

tarih=soup.find_all("td",{"data-th":"Tarih"})
imsak=soup.find_all("td", {"data-th": "Ýmsak"})
gunes=soup.find_all("td",{"data-th":"Güneþ"})
ogle=soup.find_all("td", {"data-th": "Öðle"})
ikindi=soup.find_all("td",{"data-th":"Ýkindi"})
aksam=soup.find_all("td", {"data-th": "Akþam"})
yatsi=soup.find_all("td",{"data-th":"Yatsý"})

print("  Tarih     Ýmsak  Güneþ  Öðle   Ýkindi Akþam  Yatsý")
print("----------------------------------------------------")

for tarih,imsak,gunes,ogle,ikindi,aksam,yatsi in zip(tarih,imsak,gunes,ogle,ikindi,aksam,yatsi):
    print(tarih.text,"",imsak.text,"",gunes.text,"",ogle.text,"",ikindi.text,"",aksam.text,"",yatsi.text,"")
print("----------------------------------------------------")