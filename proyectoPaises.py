from random import randint
import requests
from bs4 import BeautifulSoup
import urllib.request
import PIL.Image
from PIL import ImageTk
from tkinter import *
from tkinter import messagebox

class Bandera:
    def __init__(self,window):
        self.banderas=[]
        self.window=window

        self.window.protocol("WM_DELETE_WINDOW", self.punt)
        self.puntuacion=0
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


    def comprobacion(self):
        if self.entry.get()!='':
            resultado=self.entry.get()
            print(self.banderas[self.numero]["Pais"])
            if resultado.upper()==self.banderas[self.numero]["Pais"]:
                messagebox.showinfo(message="Has acertado", title="Resultado")
                self.puntuacion+=10
                print("Has acertado")
            else:
                messagebox.showinfo(message="Has fallado", title="Resultado")
                print("Has fallado")
                self.puntuacion-=3
                print("Era: "+self.banderas[self.numero]["Pais"])
        else:
            print("Introduzca algo.")


    def punt(self):
        messagebox.showinfo(message="Tienes "+str(self.puntuacion)+" puntos", title="Resultado")

        self.window.destroy()

    def metodo(self):
        self.numero=randint(0,len(self.banderas)-1)
        print(self.banderas[self.numero]["Bandera"])

        urllib.request.urlretrieve(self.banderas[self.numero]["Bandera"],"gfg.jpg")

        image1 = PIL.Image.open("gfg.jpg")
        test = ImageTk.PhotoImage(image1)

        self.label1 = Label(self.window,image=test)
        self.label1.image = test
        self.label1.place(x=10, y=20)

        self.entry=Entry()
        self.entry.place(x=350,y=80)

        button = Button(text="Compruebe el resultado", command=self.comprobacion)
        button.place(x=350, y=120)

        button = Button(text="Terminar el juego", command=self.punt)
        button.place(x=350, y=200)

    def ejecutar(self):
        self.label1.place_forget()
        self.metodo()
if __name__=="__main__":
    print("Ejecuta el otro archivo")