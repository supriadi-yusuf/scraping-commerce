from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/kamera-populer')
def kamera_populer():
    soup = None
    with open('htmls/phography.html', 'r') as inputfile:
        soup = BeautifulSoup(inputfile, 'html.parser')

    #print(soup)


    camera_area = soup.find('div', attrs={'class': 'D_um M_ry D_CZ'})
    #print(camera_area)

    products=[]
    cameras = camera_area.find_all('div', attrs={'class':'D_ut D_nZ'})
    for camera in cameras:

        product={}

        # find nama produk
        pages = camera.find_all('p')

        # nama toko
        product['shop'] = pages[0].text

        # nama produck
        product['name'] = pages[2].text

        # print harga
        product['price'] = pages[3].text

        # print image link and product link
        item = camera.find_all('a')[1]
        product['image'] = item.find('img')['src']
        product['url'] = item['href']

        products.append(product)


    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
