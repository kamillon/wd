from lxml import html
import requests
import pandas as pd
import numpy as np 
url = "https://boardgamegeek.com/browse/boardgame"
data = requests.get(url)

page = html.fromstring(data.text)
xpath = '//*[@id="collection"]//*[@class="table-responsive"]'
table_div = page.get_element_by_id('collection')

table = table_div.xpath('./*[@class="table-responsive"]/table')[0]

headers = [label for label in table.xpath('.//th')]
reszta = [label for label in table.xpath('//tr/td')]
del(headers[1])
labels = []
r1 = []
for header in headers:
    anchor = header.xpath('./a/text()')
    if len(anchor) > 0:
        labels.append(anchor[0].strip())
    else:
        labels.append(header.text.strip())

for element in reszta:
    anchor = element.xpath('.//a/text()')
    if len(anchor) > 0:
        r1.append(anchor[0].strip())
    else:
        r1.append(element.text.strip())
s = np.array(r1)
x = np.reshape(s, (100,7))
s = np.delete(x, 1, 1)
s = np.delete(s, 5, 1)
c = np.array(labels)
c = np.delete(c, 5)

for x in range(0, np.size(s, 0)):
    anchor = element.xpath('//a/@name')
    s[x][0] = anchor[x]

df = pd.DataFrame(s, columns=c)
print(df)