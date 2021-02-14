from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests
import pandas as pd
url = "https://www.bighaat.com/sitemap_products_1.xml?from=389135657&to=4493170868247"
response=requests.get(url)
soup1= soup(response.text,"xml")
links = soup1.findAll('image:title')
print(len(links))
count = 0
Image_Name=[]
Image_Titles=[]

""""
for link in links:
    temp = link.string
    Image_Titles.append(temp)
    print(temp)


for i in range(0,1754):
    Image_Name.append((str(i)+'.jpg'))
for i in range(1754,1999):
    Image_Name.append((str(i) + '.jpg'))
Image_Titles.pop()
Image_Titles.pop()

print(len(Image_Name))
print(len(Image_Titles))

d={'Image1':Image_Titles,'Image2':Image_Name}
da=pd.DataFrame(d)
da.to_csv("Final.csv")
"""
