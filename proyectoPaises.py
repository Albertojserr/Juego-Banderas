from random import randint
import requests
from bs4 import BeautifulSoup
import urllib.request
import PIL.Image
from PIL import ImageTk
from tkinter import *


'''
def limpieza(texto):
    PALABRAS_COMUNES = ["bandera", "de","banera","del","colores"]
    PALABRAS_SANCION = ["europa", "america","asia","africa","oceania","centroamerica","mapa"]
    texto=texto.lower()
    palabras = texto.split()
    for palabra in palabras:
        if palabra in PALABRAS_SANCION:
            return None
    reformado = ['' if palabra in PALABRAS_COMUNES else palabra for palabra in palabras]
    texto = " ".join(reformado)
    texto=texto.strip()
    texto=texto.upper()
    return texto
url_eu = 'https://www.banderasdelmundo.net/banderas-paises-de-europa/'#funciona
url_suram='https://www.banderasdelmundo.net/banderas-de-los-paises-de-sudamerica/'#funciona
url_noram='https://www.banderasdelmundo.net/banderas-de-los-paises-de-america-del-norte/'#funciona
url_cntram='https://www.banderasdelmundo.net/banderas-paises-america-central/'#funciona
url_as='https://www.banderasdelmundo.net/banderas-paises-de-asia/'#funciona
url_af='https://www.banderasdelmundo.net/banderas-de-paises-africa/'#funciona
url_oc='https://www.banderasdelmundo.net/bandera-paises-de-oceania/'#funciona
urls=[url_eu,url_suram,url_noram,url_cntram,url_as,url_af,url_oc]
html_text = requests.get(url_oc).text
soup = BeautifulSoup(html_text, 'html.parser')
banderas=[]
def filtrar(mezcla):
    for link in mezcla.find_all('img'):
        if link.get('loading')=="lazy":
            if link.get('data-src')!=None:
                Pais=limpieza(link.get('alt'))
                if Pais !=None:
                    banderas.append({"Pais": Pais,"Bandera": link.get('data-src')})
filtrar(soup)
html_text = requests.get(url_af).text
soup = BeautifulSoup(html_text, 'html.parser')
filtrar(soup)
html_text = requests.get(url_suram).text
soup = BeautifulSoup(html_text, 'html.parser')
filtrar(soup)
html_text = requests.get(url_noram).text
soup = BeautifulSoup(html_text, 'html.parser')
def crear(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    filtrar(soup)
for Url in urls:
    crear(Url)
for pais in banderas:
    print(pais["Pais"])
#print(banderas[0])'''
class Bandera:
    def __init__(self,window):
        self.banderas=[]
        self.window=window
        url_eu = 'https://www.banderasdelmundo.net/banderas-paises-de-europa/'#funciona
        url_suram='https://www.banderasdelmundo.net/banderas-de-los-paises-de-sudamerica/'#funciona
        url_noram='https://www.banderasdelmundo.net/banderas-de-los-paises-de-america-del-norte/'#funciona
        url_cntram='https://www.banderasdelmundo.net/banderas-paises-america-central/'#funciona
        url_as='https://www.banderasdelmundo.net/banderas-paises-de-asia/'#funciona
        url_af='https://www.banderasdelmundo.net/banderas-de-paises-africa/'#funciona
        url_oc='https://www.banderasdelmundo.net/bandera-paises-de-oceania/'#funciona
        self.urls=[url_eu,url_suram,url_noram,url_cntram,url_as,url_af,url_oc]

    def limpieza(self,texto):
        PALABRAS_COMUNES = ["bandera", "de","banera","del","colores"]
        PALABRAS_SANCION = ["europa", "america","asia","africa","oceania","centroamerica","mapa"]
        texto=texto.lower()
        palabras = texto.split()
        for palabra in palabras:
            if palabra in PALABRAS_SANCION:
                return None
        reformado = ['' if palabra in PALABRAS_COMUNES else palabra for palabra in palabras]
        texto = " ".join(reformado)
        texto=texto.strip()
        texto=texto.upper()
        return texto
    def filtrar(self,mezcla):
        for link in mezcla.find_all('img'):
            if link.get('loading')=="lazy":
                if link.get('data-src')!=None:
                    Pais=self.limpieza(link.get('alt'))
                    if Pais !=None:
                        self.banderas.append({"Pais": Pais,"Bandera": link.get('data-src')})

    def crear(self,url):
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        self.filtrar(soup)

    def ejecutar(self):
        numero=randint(0,len(self.banderas)-1)
        print(self.banderas[numero]["Bandera"])

        urllib.request.urlretrieve(self.banderas[numero]["Bandera"],"gfg.jpg")

        image1 = PIL.Image.open("gfg.jpg")
        test = ImageTk.PhotoImage(image1)

        label1 = Label(self.window,image=test)
        label1.image = test
        label1.place(x=10, y=20)
        pais=input("Escribe el pais:")
        print(self.banderas[numero]["Pais"])
        if pais.upper()==self.banderas[numero]["Pais"]:
            print("Has acertado")
        else:
            print("Has fallado")

if __name__=="__main__":
    a=10