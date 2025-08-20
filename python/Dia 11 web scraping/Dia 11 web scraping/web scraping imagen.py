import bs4
import requests

resultado = requests.get("https://escueladirecta-blog.blogspot.com/")

sopa = bs4.BeautifulSoup(resultado.text, "lxml")

img = sopa.select("img")
print(img)

for i in img:
    print(i)






imagenes = sopa.select("img")[0]["src"]
print(imagenes)

imagen_curso = requests.get(imagenes)

f = open("img_curso.jpg","wb")
f.write(imagen_curso.content)
f.close()



