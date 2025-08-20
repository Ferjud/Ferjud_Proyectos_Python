import bs4
import requests

resultado = requests.get("https://escueladirecta-blog.blogspot.com/")

parrafo = bs4.BeautifulSoup(resultado.text, "lxml")

print(parrafo.select("link"))