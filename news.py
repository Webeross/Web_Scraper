import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com')

content = response.content

site = BeautifulSoup(content, 'html.parser')

#Html da notícia
noticia = site.find('div', attrs={'class': 'feed-post-body'})

#Título
titulo = noticia.find('span', attrs={'class': 'feed-post-header-chapeu'})

#Subtítulo
subtitulo = noticia.find('a', attrs={'class': 'feed-post-link'})

print(subtitulo.text)
