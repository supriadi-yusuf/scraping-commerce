import os
import requests
from bs4 import BeautifulSoup

soup = None
with open('htmls/phography.html', 'r') as inputfile:
    soup = BeautifulSoup(inputfile, 'html.parser')

#print(soup)

# create folder extract
try:
    os.mkdir('images')
except FileExistsError:
    pass


camera_area = soup.find('div', attrs={'class': 'D_um M_ry D_CZ'})
#print(camera_area)

cameras = camera_area.find_all('div', attrs={'class':'D_ut D_nZ'})
for camera in cameras:
    #print(camera)

    # find nama produk
    pages = camera.find_all('p')

    # nama produck
    product_name = pages[2].text.replace(' ', '_').replace('/', '').replace('|', '').replace('(','').replace(')','')


    # get image link
    image_link = camera.find_all('a')[1].find('img')['src']

    #print('name : ' + product_name)
    #print('link : ' + image_link)

    response = requests.get(image_link)

    with open('images/' + product_name + '.jpg', 'wb') as image_file:
        image_file.write(response.content)
