import requests
import bs4
base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
for i in range(1, 51):
    # print(base_url.format(i))
    res = requests.get(base_url.format(i))
    soup = bs4.BeautifulSoup(res.text, "lxml")
    # print(len(soup.select('.product_pod')))
    products = soup.select('.product_pod')
    for product in products:
        if product.select('.star-rating.Two'):
            print(product.select('h3 > a')[0]['title'])
