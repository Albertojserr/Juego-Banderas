from Ventana import Ventana
from tkinter import *

import urllib.request
from PIL import Image,ImageTk
from proyectoPaises import Bandera
if __name__=="__main__":

    window=Ventana("Juego de banderas")

    color="light steel blue"

    Label(window, text="¿De dónde es esta bandera?",bg=color,fg="black").pack()
    band=Bandera(window)
    b=Button(window, text="Siguiente", command=band.ejecutar)
    b.place(x=350,y=160)
    for url in band.urls:
        band.crear(url)

    band.metodo()
    '''urllib.request.urlretrieve("https://www.banderasdelmundo.net/wp-content/uploads/2019/08/bandera-de-yibuti-300x200.jpg","gfg.jpg")
    #ejecutar(window)
    image1 = Image.open("gfg.jpg")
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test
    label1.place(x=10, y=20)'''
    window.mainloop()
