import tkinter as tk


# Crear la ventana principal
window = tk.Tk()
window.title("Primer Programa PID")
window.geometry("800x700")

menu = tk.Menu(window)
window.config(menu=menu)
filemenu = tk.Menu(menu)

menu.add_cascade(label="Archivo", menu=filemenu)
filemenu.add_command(label="Cargar")

# Crear los frames
frame_top = tk.Frame(window, height=500)
frame_mid = tk.Frame(window, height=5)

labelDim = tk.Label(frame_mid, text="Dimensiones", font=("Consolas", 10))
labelDim.pack()

labelDimImg = tk.Label(frame_mid, text="aqui van las dimensiones de la imagen", font=("Consolas", 10))
labelDimImg.pack()

frame_bottom = tk.Frame(window, bg="lightgreen", height=60)

labelInstrucciones = tk.Label(frame_bottom, text="Ingrese las coordenadas de los puntos", font=("Consolas", 10))
labelInstrucciones.grid(row=0, column=1, columnspan=4, padx=10, pady=10)


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

buttonIniciar = tk.Button(frame_bottom, text="Iniciar", font=("Consolas", 10), bg="green", fg="white")
buttonIniciar.grid(row=2, column=5, columnspan=4, padx=10, pady=10)

# Empacar los frames en la ventana
frame_top.pack(fill=tk.BOTH, expand=True)
frame_mid.pack(fill=tk.BOTH, expand=True)
frame_bottom.pack(fill=tk.BOTH, expand=True)




# Mostrar la ventana
window.mainloop()

