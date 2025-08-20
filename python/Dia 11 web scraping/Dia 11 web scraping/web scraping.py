import bs4
import requests

resultado = requests.get("https://escueladirecta-blog.blogspot.com/")

print(type(resultado))

print(resultado.text)

sopa = bs4.BeautifulSoup(resultado.text, "lxml")

print(sopa.select("title"))

print(sopa.select("title")[0].getText())

parrafo = bs4.BeautifulSoup(resultado.text, "lxml")

print(parrafo.select("link"))

