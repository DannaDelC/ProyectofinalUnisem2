root = tk.Tk()
root.title("Marco 3D con Color")

frame = tk.Frame(root, bg="#748891")
frame.grid(column=0, row=0, padx=20, pady=20)

# Frame que actúa como el borde (el "marco 3D" con color personalizado)
marco_3d = tk.Frame(frame, bg="#000000", borderwidth=3, relief="raised")  # Color del borde y efecto 3D
marco_3d.grid(column=0, row=0, padx=10, pady=10)  # Padding para el efecto de marco

# Label dentro del frame 3D
parrafo_text = """
Las matrices son un conjunto bidimensional de números o símbolos distribuidos de forma rectangular, en líneas verticales y horizontales.
"""
parrafo = tk.Label(marco_3d, text=parrafo_text, font=("Helvetica", 12), wraplength=550, justify="left", 
                   bg="#93a5ac", borderwidth=2, relief="sunken")
parrafo.grid(column=0, row=0)

root.mainloop()