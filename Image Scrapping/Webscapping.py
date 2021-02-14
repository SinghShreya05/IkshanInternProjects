from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests
url = "https://www.bighaat.com/sitemap_products_1.xml?from=389135657&to=4493170868247"
response=requests.get(url)
soup1= soup(response.text,"xml")
links = soup1.findAll('image:loc')
print(len(links))
count = 0
for link in links:
    temp = link.string
    temp = requests.get(temp)
    temp_file = open(str(count)+".jpg","wb")
    temp_file.write(temp.content)
    temp_file.close()
    print(count,'done')
    count+=1

