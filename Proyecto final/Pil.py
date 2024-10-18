import tkinter as tk          
from tkinter import ttk           

root = tk.Tk()
root.title("Pillow")
root.geometry("600x400")

frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(row=0, column=0,sticky=(tk.W, tk.E, tk.N, tk.S))

titulo = tk.Label(frame, text="Pillow", font=("Garamond", 20, "bold"), bg="#242424", fg='Orange' )
titulo.grid(row=0, column=0, sticky=tk.N, pady=(0, 10))

parrafo= """
Pillow es una variante (o fork) de la popular librería PIL (Python Image Library) que permite procesar con facilidad imágenes con Python 2.x/3.x. El proyecto lo inició Alex Clark cuando PIL se quedó sin desarrollo a finales del año 2009. Actualmente, Pillow es mantenido con la ayuda de otros colaboradores.

Con Pillow podemos consultar información básica de una imagen como su tamaño, el formato que tiene (jpg, png, gif, etc.), el tipo de imagen (bits/pixel, BN/color, etc.) y, también, es posible modificar su aspecto realizando operaciones para cambiar su tamaño, recortar un área, girar, aplicar filtros y efectos, convertir el tipo de imagen y su formato, etc.
"""

parrafo = tk.Label(frame, text=parrafo, font=("Helvetica", 12), wraplength=560, justify="left" )
parrafo.grid(column=0, row=1, sticky=tk.W,)

enlace = tk.Label(frame, text="Más información aquí", fg="blue", cursor="hand2")
enlace.grid(column=0, row=2, sticky=tk.W, pady=(10, 0))

def abrir_url(event):
    import webbrowser
    webbrowser.open_new("https://python-para-impacientes.blogspot.com/2014/12/fundamentos-para-procesar-imagenes-con.html")
enlace.bind("<Button-1>", abrir_url)

root.mainloop()