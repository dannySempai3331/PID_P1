import tkinter as tk
from PIL import Image, ImageTk,ImageDraw
from tkinter import messagebox
import random

img = Image.open('Paisaje.jpg')

def getCoordenadas():

    if panel_imagen.winfo_ismapped():

        if entryX1.get() == "" or entryY1.get() == "" or entryX2.get() == "" or entryY2.get() == "":
            messagebox.showerror("Error", "¡Coordenadas no validas!") 

        else:

            C1 = (int(entryX1.get()), int(entryY1.get()))
            C2 = (int(entryX2.get()), int(entryY2.get()))

            if(C1[0] > C2[0]) or (C1[1] > C2[1]):

                messagebox.showerror("Error", "Las primeras coordenadas deben ser de la esquina superior izquierda")

            elif    ((C1[0] or C2[0]) > img.width) or ((C1[1] or C2[1]) > img.height):

                messagebox.showerror("Error", "Las coordenadas deben ser menor al tamaño de la imagen")

            elif C1 == C2:

                messagebox.showerror("Error", "Las coordenadas no pueden ser iguales")

            else:
                cambiarPixeles(C1,C2)

    else:
        messagebox.showerror("Error", "Primero debe cargar una imagen")

def abrirImagen():

    global img

    frame_ancho = frame_top.winfo_width()
    frame_alto = frame_top.winfo_height()

    img = img.resize((frame_ancho, frame_alto), Image.Resampling.LANCZOS)

    panel_imagen.pack()

    imagen_tk = ImageTk.PhotoImage(img)
    panel_imagen.config(image=imagen_tk)
    panel_imagen.image = imagen_tk

    ancho, alto = img.size

    label_DimImg.config(text= str(ancho) + " x " + str(alto))


def cambiarPixeles(C1,C2):

    global img
    draw = ImageDraw.Draw(img)

    for x in range(C1[0], C2[0]):
        for y in range(C1[1], C2[1]):

            red = random.randint(0,255)
            green = random.randint(0,255)
            blue = random.randint(0,255)

            draw.point((x, y), (red, green, blue))

    mostrarImagen()

def mostrarImagen():

    imagen_tk = ImageTk.PhotoImage(img)
    panel_imagen.config(image=imagen_tk)
    panel_imagen.image = imagen_tk


window = tk.Tk()
window.title("Primer Programa PID")
window.geometry("1000x1000")

menu = tk.Menu(window)
window.config(menu=menu)
filemenu = tk.Menu(menu)

menu.add_cascade(label="Archivo", menu=filemenu)
filemenu.add_command(label="Cargar imagen", command=abrirImagen)

frame_top = tk.Frame(window, height=500)

frame_mid = tk.Frame(window, height=1)

label_Dim = tk.Label(frame_mid, text="Dimensiones", font=("Consolas", 10))
label_Dim.pack()

label_DimImg = tk.Label(frame_mid, text="-", font=("Consolas", 10))
label_DimImg.pack()

frame_bottom = tk.Frame(window, bg="lightgreen", height=60)

label_Instrucciones = tk.Label(frame_bottom, text="Ingrese las coordenadas de las esquinas opuestas del rectangulo", font=("Consolas", 12))
label_Instrucciones.grid(row=0, column=1, columnspan=4, padx=10, pady=10)


labelX1 = tk.Label(frame_bottom, text="x1", font=("Consolas", 10))
labelX1.grid(row=1, column=1, padx=10, pady=10)

entryX1 = tk.Entry(frame_bottom, font=("Consolas", 10))
entryX1.grid(row=1, column=2, padx=10, pady=10)

labelY1 = tk.Label(frame_bottom, text="y1", font=("Consolas", 10))
labelY1.grid(row=2, column=1, padx=10, pady=10)

entryY1 = tk.Entry(frame_bottom, font=("Consolas", 10))
entryY1.grid(row=2, column=2, padx=10, pady=10)

labelX2 = tk.Label(frame_bottom, text="x2", font=("Consolas", 10))
labelX2.grid(row=1, column=3, padx=10, pady=10)

entryX2 = tk.Entry(frame_bottom, font=("Consolas", 10))
entryX2.grid(row=1, column=4, padx=10, pady=10)

labelY2 = tk.Label(frame_bottom, text="y2", font=("Consolas", 10))
labelY2.grid(row=2, column=3, padx=10, pady=10)

entryY2 = tk.Entry(frame_bottom, font=("Consolas", 10))
entryY2.grid(row=2, column=4, padx=10, pady=10)

button_Iniciar = tk.Button(frame_bottom, text="Iniciar", font=("Consolas", 10), bg="green", fg="white", command=getCoordenadas)
button_Iniciar.grid(row=2, column=5, columnspan=4, padx=10, pady=10)

panel_imagen = tk.Label(frame_top)

frame_top.pack(fill=tk.BOTH, expand=True)
frame_mid.pack(fill=tk.BOTH, expand=True)
frame_bottom.pack(fill=tk.BOTH, expand=True)

window.mainloop()

