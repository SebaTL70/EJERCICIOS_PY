#! python

from tkinter import *

def mostrar(elemento):
    elemento.deiconify()
def ocultar(elemento):
    elemento.withdraw()



mainTk=Tk()
mainTk.geometry('400x400')
mainTk.config(bg='green')
mainTk.title('HOLA TKINTER!')

label1=Label(mainTk,bg='green',fg='white',text='HOLA MUNDO')
boton1=Button(mainTk,text='abrir',command=lambda:mostrar(ventana1) or label2.config(text='SALIO?')) #ver que pasa con ese OR!
label1.grid(row=1,column=1)
boton1.grid(row=2,column=1)

ventana1=Toplevel(mainTk)
ventana1.title("VENTANA SEGUNDA!")
ventana1.geometry('300x200')
ventana1.config(bg='red')

label2=Label(ventana1,bg='red',fg='white',text='TEXTO EN VENTANA 2')
boton2=Button(ventana1,text='cerrar',command=lambda:ocultar(ventana1))
label2.grid(row=1,column=1)
boton2.grid(row=2,column=1)

ocultar(ventana1)


ventana1.protocol("WM_DELETE_WINDOW","onexit") #INHABILITA EL x de la ventana hija
ventana1.resizable(0,True) # solo se redimensiona a lo largo


mainTk.mainloop()