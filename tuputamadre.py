import turtle
import tkinter as tk

# --- VENTANA 1 (Usa el turtle normal) ---
ventana1 = turtle.Screen()
ventana1.title("Ventana Uno")
t1 = turtle.Turtle()
t1.color("red")
t1.forward(100)

# --- VENTANA 2 (Usa Tkinter para crear otra ventana) ---
raiz2 = tk.Tk()
raiz2.title("Ventana Dos")

# Crear un lienzo de turtle dentro de la segunda ventana
canvas2 = turtle.Canvas(raiz2, width=400, height=400)
canvas2.pack()

# Asociar una nueva pantalla y tortuga a ese lienzo
ventana2 = turtle.TurtleScreen(canvas2)
t2 = turtle.RawTurtle(ventana2) # RawTurtle se usa para lienzos externos
t2.color("blue")
t2.forward(100)

# Mantener ambas ventanas vivas
raiz2.mainloop()