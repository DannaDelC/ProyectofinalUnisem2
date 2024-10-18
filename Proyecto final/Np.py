import tkinter as tk          
from tkinter import ttk           

root = tk.Tk()
root.title("Numpy")
root.geometry("600x400")

frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(row=0, column=0,sticky=(tk.W, tk.E, tk.N, tk.S))

titulo = tk.Label(frame, text="Numpy", font=("Garamond", 20, "bold"), bg="#242424", fg='Orange' )
titulo.grid(row=0, column=0, sticky=tk.N, pady=(0, 10))

parrafo= """
NumPy (se pronuncia "numb pie") es uno de los paquetes más importantes a entender cuando estás comenzando a aprender Python.

El paquete es conocido por una estructura de datos muy útil llamado arreglo de NumPy. NumPy también permite a los desarrolladores de Python realizar en forma rápida una amplia variedad de cálculo numéricos.

Este tutorial te enseñará los fundamentos de NumPy que puedes usar para crear aplicaciones numéricas en Python

NumPy es una librería de Python para computación científica. NumPy significa  Python numérico. Aquí está la descripción oficial de la librería indicada en su página web: "NumPy es el paquete fundamental para la computación científica con Python. Contiene entre otras cosas:
"""

parrafo = tk.Label(frame, text=parrafo, font=("Helvetica", 12), wraplength=560, justify="left" )
parrafo.grid(column=0, row=1, sticky=tk.W,)

enlace = tk.Label(frame, text="Más información aquí", fg="blue", cursor="hand2")
enlace.grid(column=0, row=2, sticky=tk.W, pady=(0, 10))

def abrir_url(event):
    import webbrowser
    webbrowser.open_new("https://www.freecodecamp.org/espanol/news/la-guia-definitiva-del-paquete-numpy-para-computacion-cientifica-en-python/")
enlace.bind("<Button-1>", abrir_url)

root.mainloop()