import requests
import bs4
import lxml
res = requests.get('http://quotes.toscrape.com/page/1/')
soup = bs4.BeautifulSoup(res.text, 'lxml')
authors = []
for quote in soup.select('.quote'):
    authors.append(quote.select('small.author')[0].text)
quotes = []
for quote in soup.select('.quote'):
    quotes.append(quote.select('span.text')[0].text)
tags = []
for tag in soup.select('span.tag-item'):
    tags.append(tag.select('a.tag')[0].text)

print(authors)
print(quotes)
print(tags)
