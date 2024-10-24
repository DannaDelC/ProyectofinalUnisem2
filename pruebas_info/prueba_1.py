import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Definición de Matrices")
root.geometry("600x420")
root.configure(bg="#748891")  # Fondo de la ventana

# Estilo para ttk.Frame
style = ttk.Style()
style.configure("Custom.TFrame", background="#c8c6c9")  # Configura el estilo personalizado

# Crear un frame con ttk y aplicarle el estilo
frame = ttk.Frame(root, padding="10 10 10 10", style="Custom.TFrame")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Label de título utilizando tkinter Label (que soporta bg y fg)
titulo = tk.Label(frame, text="Definición de Matrices", font=("Garamond", 24, "bold"), bg="#c8c6c9", fg="black")
titulo.grid(column=0, row=0, sticky=tk.N, pady=(0, 10))

# Frame para el borde de color (simulando el efecto de marco 3D)
marco_3d = tk.Frame(frame, bg="#000000", borderwidth=4, relief="raised")  # Aquí pones el color del borde
marco_3d.grid(column=0, row=1, sticky=tk.W, pady=(10, 10))

# Label del párrafo dentro del marco 3D
parrafo_text = """
Las matrices son un conjunto bidimensional de números o símbolos distribuidos de forma rectangular, en líneas verticales y horizontales, de manera que sus elementos se organizan en filas y columnas. Sirven para describir sistemas de ecuaciones lineales o diferenciales, así como para representar una aplicación lineal.

Toda matriz se representa por medio de una letra mayúscula, y sus elementos se reúnen entre dos paréntesis o corchetes, en letra minúscula. A su vez, tienen doble superíndice: el primero hace referencia a la fila y el segundo a la columna a la que pertenece.

Esta expresión matemática puede sumarse, multiplicarse y descomponerse, por lo que su uso es común en el álgebra lineal.
"""

parrafo = tk.Label(marco_3d, text=parrafo_text, font=("Helvetica", 12), wraplength=550, justify="left",
                   bg="#93a5ac", borderwidth=2, relief="sunken")
parrafo.grid(column=0, row=0, padx=2, pady=5)  # Agregamos un padding dentro del marco 3D

# Label del enlace
enlace = tk.Label(frame, text="Más información aquí", font=("Helvetica", 16, "bold"), fg="#ffffff", bg="#748891",
                  cursor="hand2", borderwidth=2, relief="sunken")
enlace.grid(column=0, row=2, sticky=tk.W, pady=(10, 10))

# Función para abrir el enlace en el navegador
def abrir_url(event):
    import webbrowser
    webbrowser.open_new("https://www.ferrovial.com/es/stem/matrices/")

enlace.bind("<Button-1>", abrir_url)

root.mainloop()