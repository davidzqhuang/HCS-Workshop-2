
# pythonprogramminglanguage.com
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

req = Request("https://politico.com")
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")

links = []
for link in soup.findAll('a'):
    links.append(link.text)

print(links)
from wordcloud import WordCloud, STOPWORDS

wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='white', colormap='Pastel2', collocations=False, stopwords = STOPWORDS).generate(" ".join(links))

import matplotlib.pyplot as plt
plt.imshow(wordcloud)

from datetime import date
plt.savefig("pol-wordcloud-"+str(date.today())+".png")
