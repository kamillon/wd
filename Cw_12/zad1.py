from lxml import html
import requests

url = "https://boardgamegeek.com/"
data = requests.get(url)
page = html.fromstring(data.text)

xpath = '//div[@id="results_1"]//h2//a'
foundElements = page.xpath(xpath)
for element in foundElements :
   print(element.tag, element.keys())
   for name, value in sorted(element.items()):
       if(name=="ng-href"):
        print('%s = %r' % (name, value))