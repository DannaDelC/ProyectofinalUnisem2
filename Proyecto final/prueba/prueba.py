import tkinter as tk 
from tkinter import ttk

root = tk.Tk() 
root.title("Definición de Matrices")
root.geometry("600x400")
root.configure(bg="#D9D9D9")  # Fondo de la ventana

frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S,))
frame.config(style="TFrame")  # Aplicar estilo al frame

# Estilo del frame
style = ttk.Style()
style.configure("TFrame", background="#D9D9D9")

titulo = tk.Label(frame, text="Definición de Matrices", font=("Garamond", 20, "bold"), bg="#D9D9D9", fg="#748891")
titulo.grid(column=0, row=0, sticky=tk.N, pady=(0, 10))

parrafo_text = """
Las matrices son un conjunto bidimensional de números o símbolos distribuidos de forma rectangular,  en líneas verticales y horizontales, de manera que sus elementos se organizan en filas y columnas. Sirven para describir  sistemas de ecuaciones lineales o diferenciales, así como para representar una aplicación lineal.

Toda matriz se representa por medio de una letra mayúscula, y sus elementos se reúnen entre dos paréntesis o corchetes, en letra minúscula. A su vez, tienen doble superíndice: el primero hace referencia a la fila y el segundo a la columna a la que pertenece.

Esta expresión matemática puede sumarse, multiplicarse y descomponerse, por lo que su uso es común en el álgebra lineal.
"""

# Párrafo con borde
parrafo = tk.Label(frame, text=parrafo_text, font=("Helvetica", 11), wraplength=550, justify="left", 
                   bg="#D9D9D9", borderwidth=2, relief="solid")  # Añadir borde y color de fondo
parrafo.grid(column=0, row=1, sticky=tk.W)

enlace = tk.Label(frame, text="Más información aquí", fg="blue", cursor="hand2", bg="#D9D9D9")   
enlace.grid(column=0, row=2, sticky=tk.W, pady=(10, 0))

def abrir_url(event):
    import webbrowser
    webbrowser.open_new("https://www.ferrovial.com/es/stem/matrices/")

enlace.bind("<Button-1>", abrir_url)

root.mainloop()
