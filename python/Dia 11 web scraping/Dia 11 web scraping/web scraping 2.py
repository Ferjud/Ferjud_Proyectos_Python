import bs4
import requests

resultado = requests.get("https://escueladirecta-blog.blogspot.com/")

sopa = bs4.BeautifulSoup(resultado.text, "lxml")

columna_lateral = sopa.select(".r-snippetized p")
print(columna_lateral)

for p in columna_lateral:
    print(p.getText())

