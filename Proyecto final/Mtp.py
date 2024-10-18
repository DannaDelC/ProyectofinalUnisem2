import tkinter as tk          
from tkinter import ttk           

root = tk.Tk()
root.title("Matplotlib")
root.geometry("600x400")

frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(row=0, column=0,sticky=(tk.W, tk.E, tk.N, tk.S))

titulo = tk.Label(frame, text="Matplotlib", font=("Garamond", 20, "bold"), bg="#242424", fg='Orange' )
titulo.grid(row=0, column=0, sticky=tk.N, pady=(0, 10))

parrafo= """
Matplotlib es una biblioteca de visualización de datos potente y muy popular en Python. En este tutorial, analizaremos cómo crear gráficos de líneas, gráficos de barras y gráficos de dispersión en Matplotlib utilizando datos del mercado de valores en 2022. Estos son los gráficos básicos que le permitirán comenzar a comprender, visualizar y contar historias sobre los datos. La visualización de datos es una habilidad esencial para todos los analistas de datos y Matplotlib es una de las bibliotecas más populares para crear visualizaciones. 

Este tutorial requiere algunos conocimientos previos básicos sobre matrices NumPy y marcos de datos de Pandas. Cuando usemos esas bibliotecas, explicaremos rápidamente lo que estamos haciendo. El enfoque principal de este tutorial es Matplotlib, que funciona sobre estas estructuras de datos para crear visualizaciones. 
"""

parrafo = tk.Label(frame, text=parrafo, font=("Helvetica", 12), wraplength=560, justify="left" )
parrafo.grid(column=0, row=1, sticky=tk.W,)

enlace = tk.Label(frame, text="Más información aquí", fg="blue", cursor="hand2")
enlace.grid(column=0, row=2, sticky=tk.W, pady=(0, 10))

def abrir_url(event):
    import webbrowser
    webbrowser.open_new("https://www.datacamp.com/tutorial/matplotlib-tutorial-python")
enlace.bind("<Button-1>", abrir_url)

root.mainloop()