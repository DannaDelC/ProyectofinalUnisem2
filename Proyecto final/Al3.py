import tkinter as tk          
from tkinter import ttk           

root = tk.Tk()
root.title("Matriz por Gauss-Jordan")
root.geometry("600x400")

frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(row=0, column=0,sticky=(tk.W, tk.E, tk.N, tk.S))

titulo = tk.Label(frame, text="Matriz por Gauss-Jordan", font=("Garamond", 20, "bold"),  bg= "#2B572C", fg="#9ACD32")
titulo.grid(row=0, column=0, sticky=tk.N, pady=(0, 10))

parrafo= """
Carl Friedrich Gauss vivió a finales del siglo XVIII y principios del XIX, pero se lo sigue considerando uno de los matemáticos más prolíficos de la historia. Sus aportes a la ciencia de las matemáticas y la física abarcan campos como el álgebra, la teoría de números, el análisis, la geometría diferencial, la astronomía y la óptica, entre otros. Sus descubrimientos sobre la teoría de las matrices cambiaron la forma de trabajar de los matemáticos durante los dos siglos pasados.

La primera vez que estudiamos la eliminación de Gauss-Jordan fue en la sección Sistemas de ecuaciones lineales: dos variables En esta sección volveremos a examinar esta técnica de resolver sistemas, esta vez mediante matrices.
"""

parrafo = tk.Label(frame, text=parrafo, font=("Helvetica", 12), wraplength=550, justify="left" )
parrafo.grid(column=0, row=1, sticky=tk.W,)

enlace = tk.Label(frame, text="Más información aquí", fg="blue", cursor="hand2")
enlace.grid(column=0, row=2, sticky=tk.W, pady=(10, 0))

def abrir_url(event):
    import webbrowser
    webbrowser.open_new("https://openstax.org/books/prec%C3%A1lculo-2ed/pages/9-6-resolver-sistemas-con-eliminacion-de-gauss-jordan")

enlace.bind("<Button-1>", abrir_url)

root.mainloop()



