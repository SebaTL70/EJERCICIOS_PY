#! python
#IMPORTO EL MÓDULO TKINTER.
from tkinter import *

#Tk() es la ventana inicial.
mainWin=Tk()
mainWin.geometry("500x500")
mainWin.config(bg='#e5a9a9')

def funcionMostrar(ventana):
    ventana.deiconify() #deiconify muestra la ventana previamente oculta con withdraw()

def funcionOcultar(ventana):
    ventana.withdraw() #oculto ventana

def ejecutar(f):
    mainWin.after(200,f)

secundariaWin=Toplevel(mainWin) #esta es la ventana hija que se abre sin ningun mainloop()-que es solo para la principal.
#como las hijas aparecen, entonces hay que ocultarlas.
#secundariaWin.withdraw() #esto la oculta.




boton1=Button(mainWin,text='Abrir la ventana hija',command=lambda:ejecutar(funcionMostrar(secundariaWin)))#declaro un Button en mainWin

#boton1.pack() #muestra el button con pack
#tambien se puede cargar con grid para ubicarlo.

boton1.grid(row=1,column=1)

boton2=Button(mainWin,text='Oculta ventana hija',command=lambda:ejecutar(funcionOcultar(secundariaWin)))
boton2.grid(row=2,column=2)









funcionOcultar(secundariaWin)

#mainloop() arranca la ventana. mainloop() es siempre la ventana inicial.
mainWin.mainloop()