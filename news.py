import requests
from bs4 import BeautifulSoup
import pandas as pd 

lista_noticias = []

response = requests.get('https://g1.globo.com')

content = response.content

site = BeautifulSoup(content, 'html.parser')

#Html da notícia
noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

# print(noticias)
for noticia in noticias:
    #Título
    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
    # print(titulo.text)
    # print(titulo['href']) #link da noticia

    #Subtítulo
    subtitulo = noticia.find('a', attrs={'class': 'feed-post-body-resumo'})

    if (subtitulo):
        # print(subtitulo.text)
        lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
    else:
        lista_noticias.append([titulo.text, '', titulo['href']])

    
news = pd.DataFrame(lista_noticias, columns=['Título', 'Subtítulo', 'Link'])

news.to_excel('Noticias.xlsx', index=False)

# print(news)
