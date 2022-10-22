from Ventana import Ventana
from tkinter import *

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
    window.mainloop()
