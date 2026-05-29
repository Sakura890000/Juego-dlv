##cinematica al iniciar el juego

import tkinter as tk
import turtle as tr

from PIL import Image, ImageTk

ventana = tk.Tk()
canvas = tk.Canvas(ventana, width=700, height=690)
canvas.pack()
# ---- VAriables globales de cinematica ----
fondo_img = None
fondo = None
fondo_id = None

pj1_img = None
pj1 = None
pj1_id = None

pj2_img = None
pj2 = None
pj2_id = None
zoom_factor = 1.0

direccion = 1 #1 para bajar, -1 para subir, 0 para detener
balanceo_dir = 1

def escena1():
     global fondo_img, fondo, fondo_id
     global pj1_img, pj1, pj1_id
     global pj2_img, pj2, pj2_id
     global direccion, balanceo_dir
     
     canvas.delete("all") #limpia el canvas para la nueva escena
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
     
     #reinicio de variables por si algo
     direccion = 1
     balanceo_dir = 1
     
     mover_fondo1() #inicia el movimiento del fondo
     mover_escena1() #inicia el movimiento de la escena


#mover fondo


def mover_fondo1():
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
        
    ventana.after(50, mover_fondo1) #llama a esta funcion cada 50 milisegundos

    


def mover_escena1():
    global direccion
    canvas.move(fondo_id, -2, 0) #mueve el fondo en la direccion actual
    canvas.move(pj1_id, -2, 0)
    canvas.move(pj2_id, -2, 0)
    x, y = canvas.coords(fondo_id) #obtiene las coordenadas actuales del fondo
    
    if x >= -250:
          ventana.after(50, mover_escena1) 
    else:
        canvas.move(fondo_id, 0, 0) #detiene el movimiento del fondo
        canvas.move(pj1_id, 0, 0)
        canvas.move(pj2_id, 0, 0)

        ventana.after(2000, mover_personajes_escena1) #espera 2 segundos 
        
 

def mover_personajes_escena1():
    global balanceo_dir
    canvas.move(pj1_id, 0, balanceo_dir * 3) #mueve el personaje 1 en la direccion actual
    canvas.move(pj2_id, 0, balanceo_dir * 3) #mueve el personaje 2 en la direccion actual
    balanceo_dir *= -1 #cambia la direccion para el siguiente movimiento

    canvas.move(pj2_id, 5, 0)
    ventana.after(500, mover_personaje1_escena1)
    
    ventana.after(40, mover_personajes_escena1) #llama a esta funcion cada 50 milisegundos
    
def mover_personaje1_escena1():
     canvas.move(pj1_id, 5, 0)
     ventana.after(80, mover_personaje1_escena1) #llama a esta funcion cada 50 milisegundos
     
     
# escena1() #inicia la primera escena

def escena2():
    global fondo_img, fondo, fondo_id
    global pj1_img, pj1, pj1_id 
    global pj2_img, pj2, pj2_id
    global direccion, balanceo_dir
    
    canvas.delete("all") #limpia el canvas para la nueva escena
    
    # Cargar la imagen de fondo
    fondo_img = Image.open("escenario 2 bosque.jpg")
    fondo_img = fondo_img.resize((1400, 700))
    fondo = ImageTk.PhotoImage(fondo_img)
    fondo_id = canvas.create_image(0, 0,anchor="nw", image=fondo)
    
    #personaje 1
    pj1_img = Image.open("link lateral.png") #importa imagen 
    pj1_img = pj1_img.resize((100, 100))
    pj1 = ImageTk.PhotoImage(pj1_img)
    pj1_id = canvas.create_image(650, 590, anchor="center", image=pj1)

    #personaje 2
    pj2_img = Image.open("Frisk lateral.png") #importa imagen
    pj2_img = pj2_img.resize((100, 100))
    pj2 = ImageTk.PhotoImage(pj2_img)
    pj2_id = canvas.create_image(370, 620, anchor="center", image=pj2)

    #reinicio de variables por si algo
    direccion = 1
    balanceo_dir = 1
    
    mover_fondo2() #inicia el movimiento del fondo
    mover_escena2() #inicia el movimiento de la escena
    
def mover_fondo2():
    global direccion
    canvas.move(fondo_id, 0, direccion * 2) #mueve el fondo en la direccion actual
    canvas.move(pj1_id, 0, direccion * -2)
    canvas.move(pj2_id, 0, direccion * 5)
    
    x, y = canvas.coords(fondo_id) #obtiene las coordenadas actuales del fondo
    
    if y >= 0:
        direccion = -1
    elif y <= -8:
        direccion = 1
    elif x <= -690:
        direccion = 0
        
    ventana.after(50, mover_fondo2) #llama a esta funcion cada 50 milisegundos

def mover_escena2():
    global direccion
    canvas.move(fondo_id, -2, 0) #mueve el fondo en la direccion actual
    canvas.move(pj1_id, -0.5, 0)
    canvas.move(pj2_id, -0.5, 0)
    
    x, y = canvas.coords(fondo_id) #obtiene las coordenadas actuales del fondo
    
    if x >= -690:
        ventana.after(20, mover_escena2) 
    else:
        canvas.move(fondo_id, 0, 0) #detiene el movimiento del fondo
        canvas.move(pj1_id, 0, 0)
        canvas.move(pj2_id, 0, 0)
        ventana.after(2000, mover_personajes_escena1) #espera 2 segundos 
        
 

def mover_personajes_escena1():
    global balanceo_dir
    canvas.move(pj1_id, 0, balanceo_dir * 3) #mueve el personaje 1 en la direccion actual
    canvas.move(pj2_id, 0, balanceo_dir * 3) #mueve el personaje 2 en la direccion actual
    balanceo_dir *= -1 #cambia la direccion para el siguiente movimiento

    canvas.move(pj2_id, 5, 0)
    ventana.after(500, mover_personaje1_escena1)
    
    ventana.after(40, mover_personajes_escena1) #llama a esta funcion cada 50 milisegundos
    
def mover_personaje1_escena1():
     canvas.move(pj1_id, 5, 0)
     ventana.after(200, mover_personaje1_escena1) #llama a esta funcion cada 50 milisegundos
     

def escena3 ():
    global fondo_img, fondo, fondo_id
    global pj1_img, pj1, pj1_id 
    global pj2_img, pj2, pj2_id
    global direccion, balanceo_dir
    
    canvas.delete("all") #limpia el canvas para la nueva escena
    
    # Cargar la imagen de fondo
    fondo_img = Image.open("escenario 3 entrada cueva.jpg")
    fondo_img = fondo_img.resize((700, 700))
    fondo = ImageTk.PhotoImage(fondo_img)
    fondo_id = canvas.create_image(0, 0,anchor="nw", image=fondo)
    if zoom_factor < 1.015 : #limita el zoom a un factor de 2
        #personaje 1
        pj1_img = Image.open("link.png") #importa imagen 
        pj1_img = pj1_img.resize((75, 85))
        pj1 = ImageTk.PhotoImage(pj1_img)
        pj1_id = canvas.create_image(330, 545, anchor="center", image=pj1)

        #personaje 2
        pj2_img = Image.open("Frisk.png") #importa imagen
        pj2_img = pj2_img.resize((75, 85))
        pj2 = ImageTk.PhotoImage(pj2_img)
        pj2_id = canvas.create_image(270, 540, anchor="center", image=pj2)
    
    #reinicio de variables por si algo
    direccion = 1
    balanceo_dir = 1
    
    zoom_fondo_escena3() #inicia el movimiento del fondo
    
def zoom_fondo_escena3 ():
    global zoom_factor, fondo_img, fondo_id, direccion
    #//zoom//
    zoom_factor += 0.001 #aumenta el factor de zoom
    w, h = fondo_img.size
    fondo_img = fondo_img.resize((int(w * zoom_factor), int(h * zoom_factor))) #redimensiona la imagen de fondo
    zoom_fondo = ImageTk.PhotoImage(fondo_img) 
    canvas.itemconfig(fondo_id, image=zoom_fondo) #actualiza la imagen del fondo en el canvas
    canvas.zoom_fondo = zoom_fondo #guarda la referencia para evitar que se elimine
    
    #//direccion//
    canvas.move(fondo_id, -2, -4) #mueve el fondo en la direccion actual
    # canvas.move(pj1_id, -2, -4)
    # canvas.move(pj2_id, -2, -4)
    
    x, y = canvas.coords(fondo_id) #obtiene las coordenadas actuales del fondo

    if zoom_factor < 1.015 : #limita el zoom a un factor de 2
        
         ventana.after(60, zoom_fondo_escena3) #llama a esta funcion cada 50 milisegundos
    else:
        ventana.after(2000, balanceo_personaje1_escena3, ) 
        ventana.after(2531, balanceo_personaje2_escena3)

#balanceo de personajes en escena 3
def balanceo_personaje1_escena3():
    global balanceo_dir
    canvas.move(pj1_id, 0, balanceo_dir * 2) #mueve el personaje 1 en la direccion actual
    balanceo_dir *= -1 #cambia la direccion para el siguiente movimiento


    ventana.after(250, balanceo_personaje1_escena3)
    ventana.after(2000,mover_personaje1_escena3)
    
    # ventana.after(40, balanceo_personajes_escena3) #llama a esta funcion cada 50 milisegundosded

def balanceo_personaje2_escena3():
    global balanceo_dir
    canvas.move(pj2_id, 0, balanceo_dir * 2) #mueve el personaje 2 en la direccion actual
    balanceo_dir *= 1 #cambia la direccion para el siguiente movimiento

    ventana.after(250, balanceo_personaje2_escena3)
    ventana.after(2200,mover_personaje2_escena3)
    
#movimiento de los persoajes en escena 3
def mover_personaje1_escena3():
    for i in range(5): #mueve el personaje 1 hacia la derecha durante 50 iteraciones
        canvas.move(pj1_id, 1, 4)
        fondo_img = fondo_img.resize((int(fondo_img.size[0] * 1.001), int(fondo_img.size[1] * 1.001))) #redimensiona la imagen de fondo
        zoom_fondo = ImageTk.PhotoImage(fondo_img)
        # ventana.after(200, mover_personaje1_escena3) #llama a esta funcion cada 50 milisegundos
        
def mover_personaje2_escena3():
    for i in range(7): #mueve el personaje 2 hacia la derecha durante 50 iteraciones
        canvas.move(pj2_id, 1, 2)
        # ventana.after(200, mover_personaje2_escena3) #llama a esta funcion cada 50 milisegundos

escena3() #inicia la tercera escena
ventana.mainloop()


