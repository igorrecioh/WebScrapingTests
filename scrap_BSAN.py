import urllib2
from bs4 import BeautifulSoup
from datetime import datetime
import csv

# URL a scrapear
quote_page = 'http://www.infobolsa.es/cotizacion/santander'

# Realizamos la consulta a la web y obtenemos el html correspondiente
pagina = urllib2.urlopen(quote_page)

# Analizamos el html y lo guardamos en la variable `parse`
parse = BeautifulSoup(pagina, 'html.parser')

# Buscamos todas las etiquetas 'div' seguidas de la clase 'subdata1' y lo guardamos en la lista 'bsan'
bsan = parse.find_all('div', {'class':'subdata1'})
#print bsan

for i, valores in enumerate(bsan):
    valor = valores.find('div', {'class':'price flop center'}).getText()
    print valor


bsan2 = parse.find_all('div', {'class':'difs'})
#print bsan2

for i, diferencias in enumerate(bsan2):
    dif = diferencias.find ('div', {'class':'dif center flop'}).getText()
    print dif
print datetime.now()

valor2 = valor.replace(",",".")
dif2 = dif.replace(",",".")

miDato = [["precio", "diferencia", "fecha"],
          [valor2, dif2, datetime.now()]]
miCsv = open('acciones.csv', 'w')
with miCsv:
    writer = csv.writer(miCsv)
    writer.writerows(miDato)