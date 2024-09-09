import os
import csv
from bs4 import BeautifulSoup


soup = None
with open('htmls/phography.html', 'r') as inputfile:
    soup = BeautifulSoup(inputfile, 'html.parser')

#print(soup)

camera_area = soup.find('div', attrs={'class': 'D_um M_ry D_CZ'})
#print(camera_area)

cameras = camera_area.find_all('div', attrs={'class':'D_ut D_nZ'})

# create folder extract
try:
    os.mkdir('extract')
except FileExistsError:
    pass

# write csv header
with open('extract/products.csv', 'w', newline='') as csv_file:
    # newline='' berarti setelah data pertama tidak ada baris kosong
    # tapi akan langsung diisi data berikutnya
    writer = csv.writer(csv_file)
    headers = ['Nama Toko', 'Nama Produk', 'Harga']
    writer.writerow(headers)

for camera in cameras:
    # find nama produk
    pages = camera.find_all('p')

    # nama toko
    nama_toko = pages[0].text

    # nama produck
    nama_product = pages[2].text

    # print harga
    harga = pages[3].text

    with open('extract/products.csv', 'a', newline='', encoding='utf-8') as csv_file:
        # encoding = 'utf-8' untuk data dari web
        writer = csv.writer(csv_file)
        writer.writerow([nama_toko, nama_product, harga])