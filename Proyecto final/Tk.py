import tkinter as tk          
from tkinter import ttk           

root = tk.Tk()
root.title("Tkinter")
root.geometry("600x400")

frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(row=0, column=0,sticky=(tk.W, tk.E, tk.N, tk.S))

titulo = tk.Label(frame, text="Tkinter", font=("Garamond", 20, "bold"), bg="#242424", fg='Orange' )
titulo.grid(row=0, column=0, sticky=tk.N, pady=(0, 10))

parrafo= """
Tkinter es una librería del lenguaje de programación Python y funciona para la creación y el desarrollo de aplicaciones de escritorio. Esta librería facilita el posicionamiento y desarrollo de una interfaz gráfica de escritorio con Python. Tkinter es el paquete estándar de Python para interactuar con Tk.

De acuerdo a la documentación de Python, TK se describe a sí mismo como el único toolkit o kit de herramientas para el desarrollo de una interfaz gráfica de usuario (GUI) que funciona en todos los sistemas operativos, es decir, funciona en Windows, Mac OS y Linux. Además, está diseñado y preparado para lenguajes dinámicos con un alto nivel, como pueden ser Tcl, Ruby o Perl, entre otros.

Saber qué es Tkinter te aporta mucha facilidad en el desarrollo de tus aplicaciones.
"""

parrafo = tk.Label(frame, text=parrafo, font=("Helvetica", 12), wraplength=560, justify="left" )
parrafo.grid(column=0, row=1, sticky=tk.W,)

enlace = tk.Label(frame, text="Más información aquí", fg="blue", cursor="hand2")
enlace.grid(column=0, row=2, sticky=tk.W, pady=(0, 10))

def abrir_url(event):
    import webbrowser
    webbrowser.open_new("https://keepcoding.io/blog/que-es-tkinter/#:~:text=Tkinter%20es%20una%20librer%C3%ADa%20del,Python%20para%20interactuar%20con%20Tk.")
enlace.bind("<Button-1>", abrir_url)

root.mainloop()