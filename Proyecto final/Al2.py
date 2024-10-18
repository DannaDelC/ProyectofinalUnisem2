import tkinter as tk          
from tkinter import ttk           

root = tk.Tk()
root.title("Matrices Inversa")
root.geometry("600x400")

frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(row=0, column=0,sticky=(tk.W, tk.E, tk.N, tk.S))

titulo = tk.Label(frame, text="Matrices Inversa", font=("Garamond", 20, "bold"),  bg= "#2B572C", fg="#9ACD32")
titulo.grid(row=0, column=0, sticky=tk.N, pady=(0, 10))

parrafo= """
En matemáticas, en particular en álgebra lineal, una matriz cuadrada A de orden n se dice que es invertible, no singular, no degenerada o regular si existe otra matriz cuadrada de orden n, llamada matriz inversa de A y denotada por A^{-1} si A⋅A^{-1}=A^{-1}⋅A=I_{n}, donde I_{n} es la matriz identidad de orden n y el producto utilizado es el producto de matrices usual.

Una matriz cuadrada no invertible se dice que es singular o degenerada. Una matriz es singular si y sólo si su determinante es nulo. La matriz singular A se caracteriza porque su multiplicación por la matriz columna X es igual a cero para algún X no nulo. El conjunto de estos vectores (y al subespacio vectorial formado por ellos) se llamará ker A (de kernel, núcleo en alemán), para una matriz invertible ker A es el vector nulo.

Esta expresión matemática puede sumarse, multiplicarse y descomponerse, por lo que su uso es común en el álgebra lineal.
"""

parrafo = tk.Label(frame, text=parrafo, font=("Helvetica", 11), wraplength=550, justify="left")
parrafo.grid(column=0, row=1, sticky=tk.W)

enlace = tk.Label(frame, text="Más información aquí", fg="blue", cursor="hand2")
enlace.grid(column=0, row=2, sticky=tk.W, pady=(10, 0))

def abrir_url(event):
    import webbrowser
    webbrowser.open_new("https://es.wikipedia.org/wiki/Matriz_invertible")

enlace.bind("<Button-1>", abrir_url)

root.mainloop()


