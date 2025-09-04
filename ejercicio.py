from tkinter import *

#variables globales
BASE = 460
ALTURA = 460

# ventana pricipal
ventana_principal = Tk()
ventana_principal.title("tren")
ventana_principal.resizable(False,False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg="white")


# Frame de graficación
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="green",width=480,height=480)
frame_graficacion.place(x=10,y=10)

#lienzo de graficacion
c =Canvas(frame_graficacion,width=BASE,height=ALTURA)
c.config(bg="black")
c.place(x=10,y=10)

base = c.create_rectangle(80,300,300,200,fill="pink", outline="blue")
base = c.create_rectangle(180,130,290,200,fill="blue")
base = c.create_rectangle(171,100,300,130,fill="orange")
base = c.create_rectangle(182,80,290,100,fill="white")

texto_1 = c.create_text(190,250,anchor="center", text="juan fernando", font=("Arial", 25, "bold"), fill="blue" , activefill="yellow")

base = c.create_rectangle(110,150,140,200,fill="red")
base = c.create_rectangle(100,170,150,145,fill="red")

rueda1 = c.create_oval(110,340,160,275, fill="gray40", outline="black")
rueda2 = c.create_oval(180,340,230,275, fill="gray40", outline="black")
rueda3 = c.create_oval(250,340,300,275, fill="gray40", outline="black")

base = c.create_rectangle(65,295,80,205,fill="green", outline="blue")

base = c.create_rectangle(50,295,70,180,fill="green", outline="blue")

#desplegar ventana pricipal
ventana_principal.mainloop()
