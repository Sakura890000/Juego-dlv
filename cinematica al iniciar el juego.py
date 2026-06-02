##cinematica al iniciar el juego

import tkinter as tk
import turtle as tr
import os
from PIL import Image, ImageTk
from PIL import ImageOps 


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

#///deben reiniciarse por escena///
zoom_factor = 1.0
direccion = 1 #1 para bajar, -1 para subir, 0 para detener
balanceo_dir = 1
espejo = False

##---frames de los personajes---##
def obtener_frame_link(num_archivo):
    
    carpeta_sprites_link = "link sprites"
    
    nombre_archivo = f"{num_archivo}_link sprites.png"
    ruta_completa = os.path.join(carpeta_sprites_link, nombre_archivo)
    
    img_link = Image.open(ruta_completa)
    
    return img_link

def obtener_frame_frisk(num_archivo):
    
    carpeta_sprites_frisk = "frisk sprites"

    nombre_archivo = f"{num_archivo}_frisk sprites.png"
    ruta_completa = os.path.join(carpeta_sprites_frisk, nombre_archivo)
    
    img_frisk = Image.open(ruta_completa)
    
    return img_frisk

#///variable unica de escena 3///
zoom_factor_pj2_escena3 = 1.0

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

    
##---ESCENA 1----##

def mover_escena1():
    global direccion
    canvas.move(fondo_id, -2, 0) #mueve el fondo en la direccion actual
    canvas.move(pj1_id, -2, 0)
    canvas.move(pj2_id, -2, 0)
    x, y = canvas.coords(fondo_id) #obtiene las coordenadas actuales del fondo
    
    canvas.update() 
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
    
    canvas.update() #actualiza el canvas para mostrar el movimiento
    canvas.move(pj2_id, 5, 0)
    ventana.after(500, mover_personaje1_escena1)
    
    ventana.after(40, mover_personajes_escena1) #llama a esta funcion cada 50 milisegundos
    
def mover_personaje1_escena1():
     canvas.move(pj1_id, 5, 0)
     ventana.after(80, mover_personaje1_escena1) #llama a esta funcion cada 50 milisegundos
     
     
## --- ESCENA 2----##

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
     
##---- ESCENA 3----##

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
        pj1_id = canvas.create_image(370, 550, anchor="center", image=pj1)

        #personaje 2
        pj2_img = Image.open("Frisk.png") #importa imagen
        pj2_img = pj2_img.resize((75, 85))
        pj2 = ImageTk.PhotoImage(pj2_img)
        pj2_id = canvas.create_image(270, 545, anchor="center", image=pj2)
    
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
        ventana.after(2000, lambda: balanceo_personaje1_escena3(pasos_restantes=100))
        ventana.after(2531, lambda: balanceo_personaje2_escena3(pasos_restantes=100))


#balanceo de personajes en escena 3
def balanceo_personaje1_escena3(pasos_restantes):
    global balanceo_dir
    if pasos_restantes > 0:
        canvas.move(pj1_id, 0, balanceo_dir * 2) #mueve el personaje 1 en la direccion actual
        balanceo_dir *= -1 #cambia la direccion para el siguiente movimiento
        ventana.after(150, lambda: balanceo_personaje1_escena3(pasos_restantes=pasos_restantes-1))
        if pasos_restantes < 90:
            mover_personaje1_escena3() #inicia el movimiento del personaje 1 despues de balancear


def balanceo_personaje2_escena3(pasos_restantes):
    global balanceo_dir
    if pasos_restantes > 0:
        canvas.move(pj2_id, 0, balanceo_dir * 2) #mueve el personaje 2 en la direccion actual
        balanceo_dir *= 1 #cambia la direccion para el siguiente movimiento
        ventana.after(150, lambda: balanceo_personaje2_escena3(pasos_restantes=pasos_restantes-1))
        if pasos_restantes < 90:
            mover_personaje2_escena3() #inicia el movimiento del personaje 2 despues de balancear

#movimiento de los persoajes en escena 3
def mover_personaje1_escena3():
    global pj1_img, pj1_id, zoom_factor
    for i in range(5): #mueve el personaje 1 hacia la derecha durante 50 iteraciones
        canvas.move(pj1_id, 1, 4)
        #aumenta el tamaño del personaje 1 para simular acercamiento
        zoom_factor += 0.025
        
        w, h = pj1_img.size
        pj1_img_zoom = pj1_img.resize((int(w * zoom_factor), int(h * zoom_factor)))
        zoom_pj1 = ImageTk.PhotoImage(pj1_img_zoom)  
        
    
        canvas.itemconfig(pj1_id, image=zoom_pj1) 
        canvas.update() #actualiza el canvas para mostrar el cambio de imagen
        canvas.after(50) #espera 50 milisegundos antes de la siguiente iteracion

def mover_personaje2_escena3():
    global pj2_img, pj2_id, zoom_factor_pj2_escena3
    for i in range(7): #mueve el personaje 2 hacia la derecha durante 50 iteraciones
        canvas.move(pj2_id, 1, 2.5)
        #aumenta el tamaño del personaje 2 para simular acercamiento
        zoom_factor_pj2_escena3 += 0.02
        
        w, h = pj2_img.size
        pj2_img_zoom = pj2_img.resize((int(w * zoom_factor_pj2_escena3), int(h * zoom_factor_pj2_escena3)))
        zoom_pj2 = ImageTk.PhotoImage(pj2_img_zoom)
        
        canvas.itemconfig(pj2_id, image=zoom_pj2)
        canvas.update() #actualiza el canvas para mostrar el cambio de imagen
        canvas.after(30) #espera 50 milisegundos antes de la siguiente iteracion

##---- ESCENA 4----##

def escena4 ():
    global fondo_img, fondo, fondo_id
    global pj1_img, pj1, pj1_id 
    global pj2_img, pj2, pj2_id
    global direccion, balanceo_dir, zoom_factor
    
    canvas.delete("all") #limpia el canvas para la nueva escena
    
    # Cargar la imagen de fondo
    fondo_img = Image.open("escenario 4 cueva interior.jpg")
    fondo_img = fondo_img.resize((850, 700))
    fondo = ImageTk.PhotoImage(fondo_img)
    fondo_id = canvas.create_image(0, 0,anchor="nw", image=fondo)
    
    #personaje 1
    pj1_img = Image.open("link lateral2.png") #importa imagen 
    pj1_img = pj1_img.resize((90, 90))
    pj1 = ImageTk.PhotoImage(pj1_img)
    pj1_id = canvas.create_image(490, 640, anchor="center", image=pj1)
    
    #--- espejo de pj1 ---
    pj1_img_espejo_escena4 = ImageOps.mirror(pj1_img) #personaje 1 para que mire hacia la derecha
    pj1_normal_escena4 = ImageTk.PhotoImage(pj1_img) #personaje 1 normal
    pj1_espejo_escena4 = ImageTk.PhotoImage(pj1_img_espejo_escena4) #personaje 1 espejo
    
    canvas.pj1_normal_escena4 = pj1_normal_escena4 #guarda la referencia para evitar que se elimine
    canvas.pj1_espejo_escena4 = pj1_espejo_escena4 #guarda la referencia para evitar que se elimine

    #personaje 2
    pj2_img = Image.open("Frisk lateral left.png") #importa imagen
    pj2_img = pj2_img.resize((55, 75))
    pj2 = ImageTk.PhotoImage(pj2_img)
    pj2_id = canvas.create_image(240, 560, anchor="center", image=pj2)
    
    direccion = 1.0
    balanceo_dir =  1.0
    zoom_factor = 1.0
    mover_fondo4()
    movimiento_pj1_escena4() #inicia el movimiento del personaje 1 en la escena 4
    mover_pj2_escena4() #inicia el movimiento del personaje 2 en la escena 4

    
    
def mover_fondo4():
    global direccion
    canvas.move(fondo_id, 0, direccion *2 ) #mueve el fondo en la direccion actual
    canvas.move(pj1_id, 0, direccion * 2)
    # canvas.move(pj2_id, 0, direccion * 2)
    
    #obtiene las coordenadas actuales del fondo
    x, y = canvas.coords(fondo_id) #obtiene las coordenadas actuales del fondo
    #cambiar la direccion si el fondo llega a cierto punto
    if y >= 0: 
        direccion = -1 
    elif y <= -4: 
        direccion = 1 
    canvas.update() #actualiza el canvas para mostrar el movimiento
    ventana.after(250, mover_fondo4) #llama a esta funcion cada 50 milisegundos
    
    

def movimiento_pj1_escena4():
    global espejo
    if espejo:
        canvas.itemconfig(pj1_id, image=canvas.pj1_normal_escena4) #cambia a la imagen normal
    else:
        canvas.itemconfig(pj1_id, image=canvas.pj1_espejo_escena4) #cambia a la imagen espejo
    espejo = not espejo #cambia el estado del espejo para la siguiente iteracion
    ventana.after(750, movimiento_pj1_escena4) #llama a esta funcion cada 50 milisegundos
    
    # canvas.move(pj1_id, 0, 2) #mueve el personaje 1 hacia abajo
    # ventana.after(50, movimiento_pj1_escena4) #llama a esta funcion cada 50 milisegundos
    
def mover_pj2_escena4():
    global balanceo_dir, direccion
    canvas.move(pj2_id, 0, balanceo_dir * -2)
    
    x, y = canvas.coords(fondo_id) #obtiene las coordenadas actuales del 
   
    if y >= 0: 
        balanceo_dir = -1 
    elif y <= -4: 
        balanceo_dir = 1 
    canvas.update() #actualiza el canvas para mostrar el movimiento
    ventana.after(250, mover_pj2_escena4) #llama a esta funcion cada 50 milisegundos
    
##---- ESCENA 5----##



def escena5():
    global fondo_img, fondo, fondo_id
    global pj1_img, pj1, pj1_id 
    global pj2_img, pj2, pj2_id
    global direccion, balanceo_dir, zoom_factor
    
    canvas.delete("all") #limpia el canvas para la nueva escena
    
    # Cargar la imagen de fondo
    fondo_img = Image.open("escenario 5 cueva pasillo.jpeg")
    fondo_img = fondo_img.resize((700, 700))
    fondo = ImageTk.PhotoImage(fondo_img)
    fondo_id = canvas.create_image(0, 0,anchor="nw", image=fondo)
    
    #personaje 1
    frame_inicial_link = 61
    
    pj1_img = obtener_frame_link(frame_inicial_link) #importa imagen
    pj1_img = pj1_img.resize((75, 85))
    pj1 = ImageTk.PhotoImage(pj1_img)
    pj1_id = canvas.create_image(340, 720, anchor="center", image=pj1)

    #personaje 2
    frame_inicial_frisk = 10
    
    pj2_img = obtener_frame_frisk(frame_inicial_frisk) #importa imagen
    pj2_img = pj2_img.resize((75, 85))
    pj2 = ImageTk.PhotoImage(pj2_img)
    pj2_id = canvas.create_image(290, 750, anchor="center", image=pj2)
    
    direccion = 1.0
    balanceo_dir =  1.0
    zoom_factor = 1.0
    
    mover_pjs_escena5() #inicia el movimiento del personaje 1 en la escena 5
    
def mover_pjs_escena5(iteracion=0):
    global pj1_id, pj1_img, pj1, pj_2_id, pj2_img, pj2, zoom_factor
    
    if iteracion < 45: #limita el movimiento a 20 iteraciones
        canvas.move(pj1_id, 0, -4) #mueve el personaje 1 hacia arriba
        canvas.move(pj2_id, 0, -4) #mueve el personaje 2 hacia arriba
        
        zoom_factor -= 0.016
        
        ##pj1 sprites
        sprite_inicial_link = 61
        total_frames_link = 9
        num_archivo_link = sprite_inicial_link + (iteracion % total_frames_link) #cambia el frame cada 5 iteraciones\
        
        #Pj2 sprites
        sprite_inicial_frisk = 10
        total_frames_frisk = 3
        num_archivo_frisk = sprite_inicial_frisk + (iteracion % total_frames_frisk) #cambia el frame cada 5 iteraciones
        
        #pj1 actualizar
        img_link_pil = obtener_frame_link(num_archivo_link)
        w_link, h_link = 140, 150
        
        img_link_res = img_link_pil.resize((int(w_link * zoom_factor), int(h_link * zoom_factor)))
        pj1 = ImageTk.PhotoImage(img_link_res)
        canvas.itemconfig(pj1_id, image=pj1) #actualiza la imagen del personaje 1 en el canvas
        
        #pj2 actualizar
        img_frisk_pil = obtener_frame_frisk(num_archivo_frisk)
        w_frisk, h_frisk = 140, 150
        img_frisk_res = img_frisk_pil.resize((int(w_frisk * zoom_factor), int(h_frisk * zoom_factor)))
        pj2 = ImageTk.PhotoImage(img_frisk_res)
        canvas.itemconfig(pj2_id, image=pj2) #actualiza la imagen del personaje 2 en el canvas
        
        #///zoom pj1///
        canvas.update() #actualiza el canvas para mostrar el cambio de imagen
        ventana.after(100, lambda: mover_pjs_escena5(iteracion +1)) #llama a esta funcion cada 50 milisegundos
       
       


escena5() #inicia la quinta escena


ventana.mainloop()


