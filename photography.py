import requests
from bs4 import BeautifulSoup
import os

"""url = 'https://id.carousell.com/categories/photography-6/'
response = requests.get(url, headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'})

try:
    os.mkdir('htmls')
except FileExistsError:
    pass

with open('htmls/phography.html', 'w') as outfile:
    outfile.write(response.text)"""

"""soup = BeautifulSoup(response.text, 'html.parser')
print(soup)"""

soup = None
with open('htmls/phography.html', 'r') as inputfile:
    soup = BeautifulSoup(inputfile, 'html.parser')

#print(soup)


camera_area = soup.find('div', attrs={'class': 'D_um M_ry D_CZ'})
#print(camera_area)

cameras = camera_area.find_all('div', attrs={'class':'D_ut D_nZ'})
for camera in cameras:
    #print(camera)

    # find nama produk
    pages = camera.find_all('p')

    # print nama toko
    #print(pages[0].text)

    # print nama produck
    #print(pages[2].text)

    # print harga
    #print(pages[3].text)

    # print image link
    #print(camera.find('img')['src'])

    # nama toko
    #print(camera.find(attrs={'data-testid':'listing-card-text-seller-name'}).text)

