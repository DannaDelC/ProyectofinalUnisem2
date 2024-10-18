import tkinter as tk          
from tkinter import ttk           

root = tk.Tk()
root.title("Scipy")
root.geometry("600x400")

frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(row=0, column=0,sticky=(tk.W, tk.E, tk.N, tk.S))

titulo = tk.Label(frame, text="Scipy", font=("Garamond", 20, "bold"), bg="#242424", fg='Orange' )
titulo.grid(row=0, column=0, sticky=tk.N, pady=(0, 10))

parrafo= """
SciPy es una colección de algoritmos matemáticos y funciones prácticas creadas sobre la extensión NumPy de Python. Añade una potencia significativa a la sesión interactiva de Python al proporcionar al usuario comandos y clases de alto nivel para manipular y visualizar datos. Con SciPy, una sesión interactiva de Python se convierte en un entorno de procesamiento de datos y creación de prototipos de sistemas que rivaliza con sistemas como MATLAB, IDL, Octave, R-Lab y SciLab.

El beneficio adicional de basar SciPy en Python es que también se obtiene un potente lenguaje de programación para desarrollar programas sofisticados y aplicaciones especializadas. Las aplicaciones científicas que utilizan SciPy se benefician del desarrollo de módulos adicionales en numerosos nichos del panorama del software por parte de desarrolladores de todo el mundo. Todo, desde programación paralela hasta subrutinas y clases para bases de datos y web, se ha puesto a disposición del programador Python. 
"""

parrafo = tk.Label(frame, text=parrafo, font=("Helvetica", 12), wraplength=560, justify="left" )
parrafo.grid(column=0, row=1, sticky=tk.W,)

enlace = tk.Label(frame, text="Más información aquí", fg="blue", cursor="hand2")
enlace.grid(column=0, row=2, sticky=tk.W, pady=(0, 10))

def abrir_url(event):
    import webbrowser
    webbrowser.open_new("https://docs.scipy.org/doc/scipy-1.8.1/tutorial/general.html")
enlace.bind("<Button-1>", abrir_url)

root.mainloop()

