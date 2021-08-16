import requests
import bs4

result = requests.get(
    'https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
# print(type(result))
# print(result.text)

soup = bs4.BeautifulSoup(result.text, "lxml")
print(soup.select('.thumbimage')[0]['src'])
img_link = "https:" + soup.select('.thumbimage')[0]['src']
# print(soup.select('title')[0].getText())
image = requests.get(img_link)
# print(image.content)

with open('image.jpg', 'wb') as f:
    f.write(image.content)
