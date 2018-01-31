import requests
from bs4 import BeautifulSoup
url="https://www.huzursayfasi.com/namaz-vakitleri/istanbul-sultanbeyli-namaz-vakitleri.html"
response= requests.get(url)
html_icerigi=response.content
soup=BeautifulSoup(html_icerigi,"html.parser")

tarih=soup.find_all("td",{"data-th":"Tarih"})
imsak=soup.find_all("td", {"data-th": "�msak"})
gunes=soup.find_all("td",{"data-th":"G�ne�"})
ogle=soup.find_all("td", {"data-th": "��le"})
ikindi=soup.find_all("td",{"data-th":"�kindi"})
aksam=soup.find_all("td", {"data-th": "Ak�am"})
yatsi=soup.find_all("td",{"data-th":"Yats�"})

print("  Tarih     �msak  G�ne�  ��le   �kindi Ak�am  Yats�")
print("----------------------------------------------------")

for tarih,imsak,gunes,ogle,ikindi,aksam,yatsi in zip(tarih,imsak,gunes,ogle,ikindi,aksam,yatsi):
    print(tarih.text,"",imsak.text,"",gunes.text,"",ogle.text,"",ikindi.text,"",aksam.text,"",yatsi.text,"")
print("----------------------------------------------------")