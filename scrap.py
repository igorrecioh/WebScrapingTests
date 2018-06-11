import urllib2
from bs4 import BeautifulSoup

# URL a scrapear
quote_page = 'http://www.basketaraba.com/es/clasificaciones.asp?grupo=5ab236d03dad3'

# Realizamos la consulta a la web y obtenemos el html correspondiente
pagina = urllib2.urlopen(quote_page)

# Analizamos el html y lo guardamos en la variable `parse`
parse = BeautifulSoup(pagina, 'html.parser')

# Buscamos todas las etiquetas 'tr' seguidas de la clase 'impar' y lo guardamos en la lista 'name'
nombres_impar = parse.find_all('tr', {'class':'impar'})

# Obtenemos la posicion del equipo, partidos, puntos...
posicion = parse.find_all('td', {'align':'center'})
for i in posicion:
    print i.getText()

# Guardamos en una lista los nombres de los equipos pares
lista_impar = [ ]

# Recorremos la lista 'name' y obtenemos los nombres de equipo
for i, nombre_impar in enumerate(nombres_impar):
    equipos_impar = nombre_impar.find('td', {'align':'left'}).getText()
    lista_impar.append(equipos_impar)
    print lista_impar[i]

# Buscamos todas las etiquetas 'tr' seguidas de la clase 'par'    
nombres_par = parse.find_all('tr', {'class':'par'})

# Guardamos en una lista los nombres de los equipos impares
lista_par = [ ]

# Recorremos la lista 'name2' y obtenemos los nombres de equipo
for i, nombre_par in enumerate(nombres_par):
    equipos_par = nombre_par.find('td', {'align':'left'}).getText()
    lista_par.append(equipos_par)
    print lista_par[i]
      
    
