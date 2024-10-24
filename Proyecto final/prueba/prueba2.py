import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Definición de Matrices")
root.geometry("600x450")
root.configure(bg="#D9D9D9")

frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S,))
frame.config(style="TFrame")

style = ttk.Style()
style.configure("TFrame", background="#D9D9D9")

titulo = tk.Label(frame, text="Definición de Matrices", font=("Garamond", 24, "bold"), bg="#D9D9D9", fg="#748891")
titulo.grid(column=0, row=0, sticky=tk.N, pady=(0, 10))

parrafo_text = """
Las matrices son un conjunto bidimensional de números o símbolos distribuidos de forma rectangular,  en líneas verticales y horizontales, de manera que sus elementos se organizan en filas y columnas. Sirven para describir  sistemas de ecuaciones lineales o diferenciales, así como para representar una aplicación lineal.

Toda matriz se representa por medio de una letra mayúscula, y sus elementos se reúnen entre dos paréntesis o corchetes, en letra minúscula. A su vez, tienen doble superíndice: el primero hace referencia a la fila y el segundo a la columna a la que pertenece.

Esta expresión matemática puede sumarse, multiplicarse y descomponerse, por lo que su uso es común en el álgebra lineal.
"""

parrafo = tk.Label(frame, text=parrafo_text, font=("Helvetica", 12), wraplength=550, justify="left", 
                   bg="#c8c6c9", borderwidth=2, relief="solid")
parrafo.grid(column=0, row=1, sticky=tk.W, pady=(10, 10))

separator = ttk.Separator(frame, orient="horizontal")
separator.grid(column=0, row=2, sticky=(tk.W, tk.E), pady=(10, 10))

enlace = tk.Label(frame, text="Más información aquí", font=("Helvetica", 12, "bold"), fg="#ffffff", bg="#748891", cursor="hand2")
enlace.grid(column=0, row=3, sticky=tk.W, pady=(10, 10))

def abrir_url(event):
    import webbrowser
    webbrowser.open_new("https://www.ferrovial.com/es/stem/matrices/")

enlace.bind("<Button-1>", abrir_url)

root.mainloop()