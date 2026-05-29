##cinematica al iniciar el juego

import tkinter as tk
import turtle as tr

from PIL import Image, ImageTk

ventana = tk.Tk()
canvas = tk.Canvas(ventana, width=700, height=690)
canvas.pack()

# Cargar la imagen de fondo
fondo_img = Image.open("escenario 1 tienda de acampar.jpg")
fondo = ImageTk.PhotoImage(fondo_img)
fondo_id = canvas.create_image(0, 0, anchor="nw", image=fondo)

#personaje 1
pj1_img = Image.open("link.png") #importa imagen
pj1_img = pj1_img.resize((150, 150))  #tamano de link ancho x alto
pj1 = ImageTk.PhotoImage(pj1_img)   
pj1_id = canvas.create_image(350, 570, anchor="center", image=pj1) #coordenadas de link x y

#personaje 2
pj2_img = Image.open("Frisk.png") #importa imagen
pj2_img = pj2_img.resize((150, 150))  #tamano de zelda ancho x alto
pj2 = ImageTk.PhotoImage(pj2_img)
pj2_id = canvas.create_image(670, 590, anchor="center", image=pj2) #coordenadas de zelda x y


#mover fondo

direccion = 1 # 1 = abajo, -1 = arriba
def mover_fondo():
    global direccion
    canvas.move(fondo_id, 0, direccion *2 ) #mueve el fondo en la direccion actual
    canvas.move(pj1_id, 0, direccion * 2)
    canvas.move(pj2_id, 0, direccion * 2)
    
    #obtiene las coordenadas actuales del fondo
    x, y = canvas.coords(fondo_id) #obtiene las coordenadas actuales del fondo
    #cambiar la direccion si el fondo llega a cierto punto
    if y >= 0: 
        direccion = -1 
    elif y <= -8: 
        direccion = 1 
    elif x <= -250:
        direccion = 0
        
    ventana.after(50, mover_fondo) #llama a esta funcion cada 50 milisegundos

    
mover_fondo() #inicia el movimiento del fondo

def mover_escena():
    global direccion
    canvas.move(fondo_id, -2, 0) #mueve el fondo en la direccion actual
    canvas.move(pj1_id, -2, 0)
    canvas.move(pj2_id, -2, 0)
    x, y = canvas.coords(fondo_id) #obtiene las coordenadas actuales del fondo
    
    if x >= -250:
          ventana.after(50, mover_escena) 
    else:
        canvas.move(fondo_id, 0, 0) #detiene el movimiento del fondo
        canvas.move(pj1_id, 0, 0)
        canvas.move(pj2_id, 0, 0)

        ventana.after(2000, mover_personajes) #espera 2 segundos 
        
balanceo_dir = 1 # 1 = derecha, -1 = izquierda   
mover_escena() #inicia el movimiento de la escena
def mover_personajes():
    global balanceo_dir
    canvas.move(pj1_id, 0, balanceo_dir * 3) #mueve el personaje 1 en la direccion actual
    canvas.move(pj2_id, 0, balanceo_dir * 3) #mueve el personaje 2 en la direccion actual
    balanceo_dir *= -1 #cambia la direccion para el siguiente movimiento

    canvas.move(pj2_id, 5, 0)
    ventana.after(500, mover_personaje1)
    
    ventana.after(40, mover_personajes) #llama a esta funcion cada 50 milisegundos
    
def mover_personaje1():
     canvas.move(pj1_id, 5, 0)
     ventana.after(80, mover_personaje1) #llama a esta funcion cada 50 milisegundos
     
     
ventana.mainloop()


