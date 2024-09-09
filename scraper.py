import requests
from bs4 import BeautifulSoup

url = "https://id.carousell.com/u/carousell_id/"
response = requests.get(url)

soup = BeautifulSoup(response.text,'html.parser')
#print(page_content)

list_barang = soup.find('div','D_um M_ry D_CZ')
print(list_barang)
