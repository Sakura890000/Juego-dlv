##cinematica al iniciar el juego

from email.mime import image
import tkinter as tk
import turtle as tr
import os
from PIL import Image, ImageTk
from PIL import ImageOps 
import math

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

relay_img = None
relay = None
relay_id = None

escena_actual_cin = 5

#///deben reiniciarse por escena///
zoom_factor = 1.0
direccion = 1 #1 para bajar, -1 para subir, 0 para detener
balanceo_dir = 1
espejo = False
resta_zoom_pjs_escena5 = 0.016
iteracion = 0
angulo_orbita = 0.0
angulo_propio = 0
radio_espiral =300.0

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
zoom_factor_pj1_escena3 = 1.0




#///escena 1////?
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
    global direccion, escena_actual_cin
    
    if escena_actual_cin != 1:
        return
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
    global direccion, escena_actual_cin
    
    if escena_actual_cin != 1:
        return
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
        ventana.after(2000, secuencias_finales_escena1)
        

def mover_personajes_escena1():
    global balanceo_dir, escena_actual_cin
    
    if escena_actual_cin != 1:
        return

    # 1. Esto mantiene el balanceo arriba y abajo de ambos personajes
    canvas.move(pj1_id, 0, balanceo_dir * 3) 
    canvas.move(pj2_id, 0, balanceo_dir * 3) 
    balanceo_dir *= -1 
    
    # 2. El bucle de balanceo continúa de forma independiente
    ventana.after(80, mover_personajes_escena1) 

def secuencias_finales_escena1():
    global escena_actual_cin
    if escena_actual_cin != 1:
        return

    # 1. Frisk se mueve a la derecha primero (se ejecuta una sola vez)
    canvas.move(pj2_id, 5, 0)
    
    # 2. Esperamos medio segundo (500ms) y arranca la caminata de Link pasando la iteración 0
    ventana.after(500, lambda: mover_personaje1_escena1(0))
    ventana.after(80, secuencias_finales_escena1)

def mover_personaje1_escena1(iteracion):
    global escena_actual_cin
    
    if escena_actual_cin != 1:
        return
        
    # Ahora la iteración SÍ sube correctamente paso a paso
    if iteracion < 100:
        canvas.update()
        canvas.move(pj1_id, 5, 0)
        # Forzamos a pasar el argumento (iteracion + 1) en el lambda de forma limpia
        ventana.after(80, lambda: mover_personaje1_escena1(iteracion + 1)) 
    else:
        # ¡ÉXITO! La iteración llegó a 10, cambiamos de escena
        escena_actual_cin = 2
        cargar_siguiente_escena()
     
     
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
    pj2_img = pj2_img.resize((70, 100))
    pj2 = ImageTk.PhotoImage(pj2_img)
    pj2_id = canvas.create_image(370, 620, anchor="center", image=pj2)

    #reinicio de variables por si algo
    direccion = 1
    balanceo_dir = 1
    
    mover_fondo2() #inicia el movimiento del fondo
    mover_escena2() #inicia el movimiento de la escena
    
def mover_fondo2():
    global escena_actual_cin, direccion, fondo_id, pj1_id, pj2_id
    if escena_actual_cin != 2:
        return
    
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
    global direccion, escena_actual_cin, fondo_id
    if escena_actual_cin != 2:
        return
    
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
        
        ventana.after(2000, mover_personajes_escena2) #espera 2 segundos 
        ventana.after(2000, secuencias_finales_escena2)
        
def mover_personajes_escena2():
    global balanceo_dir, escena_actual_cin, pj1_id, pj2_id
    
    if escena_actual_cin != 2:
        return

    # 1. Esto mantiene el balanceo arriba y abajo de ambos personajes
    canvas.move(pj1_id, 0, balanceo_dir * 3) 
    canvas.move(pj2_id, 0, balanceo_dir * 3) 
    balanceo_dir *= -1 
    
    # 2. El bucle de balanceo continúa de forma independiente
    ventana.after(60, mover_personajes_escena2) 

def secuencias_finales_escena2():
    global escena_actual_cin, pj2_id
    if escena_actual_cin != 2:
        return

    # 1. Frisk se mueve a la derecha primero (se ejecuta una sola vez)
    canvas.move(pj2_id, 10, 0)
    
    # 2. Esperamos medio segundo (500ms) y arranca la caminata de Link pasando la iteración 0
    ventana.after(500, lambda: mover_personaje1_escena2(0))
    ventana.after(110, secuencias_finales_escena2)

def mover_personaje1_escena2(iteracion):
    global escena_actual_cin, pj1_id
    
    if escena_actual_cin != 2:
        return
        
    # Ahora la iteración SÍ sube correctamente paso a paso
    if iteracion < 100:
        canvas.move(pj1_id, 5, 0)
        # Forzamos a pasar el argumento (iteracion + 1) en el lambda de forma limpia
        ventana.after(80, lambda: mover_personaje1_escena2(iteracion + 1)) 
    else:
        # ¡ÉXITO! La iteración llegó a 10, cambiamos de escena
        escena_actual_cin = 3
        cargar_siguiente_escena()


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
    global zoom_factor, fondo_img, fondo_id, direccion, escena_actual_cin
    if escena_actual_cin != 3:
        return
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
    

    if zoom_factor < 1.015 : #limita el zoom a un factor de 2
        
         ventana.after(60, zoom_fondo_escena3) #llama a esta funcion cada 50 milisegundos
    else:
        ventana.after(2000, balanceo_personaje1_escena3)
        ventana.after(2531, balanceo_personaje2_escena3)
        ventana.after(3500, lambda: mover_personaje1_escena3()) #inicia el movimiento del personaje 1 en la escena 3 despues de 2 segundos
        ventana.after(3500, lambda: mover_personaje2_escena3()) #


#balanceo de personajes en escena 3
def balanceo_personaje1_escena3():  
    global escena_actual_cin, balanceo_dir, pj1_id, escena_actual_cin
    if escena_actual_cin != 3:
        return
    if escena_actual_cin != 3:
        return
    if not canvas.winfo_exists():
        return
    canvas.move(pj1_id, 0, balanceo_dir * 2) #mueve el personaje 1 en la direccion actual
    balanceo_dir *= -1 #cambia la direccion para el siguiente movimiento
    ventana.after(150, balanceo_personaje1_escena3)
    

def balanceo_personaje2_escena3():
    global balanceo_dir, escena_actual_cin
    if escena_actual_cin != 3:
       return
    if not canvas.winfo_exists():
        return
    canvas.move(pj2_id, 0, (balanceo_dir * -1) * 2) #mueve el personaje 2 en la direccion actual
    ventana.after(150, balanceo_personaje2_escena3)
        
#movimiento de los persoajes en escena 3
def mover_personaje1_escena3(iteracion=0):
    global pj1_img, pj1_id, zoom_factor, zoom_factor_pj1_escena3, escena_actual_cin
    if escena_actual_cin != 3:
       return
    if not canvas.winfo_exists():
        return
    if iteracion < 60: 
        canvas.move(pj1_id, 1, 4)
        #aumenta el tamaño del personaje 1 para simular acercamiento
        zoom_factor += 0.025
        
        w, h = pj1_img.size
        pj1_img_zoom = pj1_img.resize((int(w * zoom_factor), int(h * zoom_factor)))
        zoom_factor_pj1_escena3 = ImageTk.PhotoImage(pj1_img_zoom)  
        canvas.itemconfig(pj1_id, image=zoom_factor_pj1_escena3) 
        
        
        ventana.after(50, lambda: mover_personaje1_escena3(iteracion + 1))
def mover_personaje2_escena3(iteracion=0):
    global pj2_img, pj2_id, zoom_factor, zoom_factor_pj2_escena3, escena_actual_cin
    if escena_actual_cin != 3:
        return  
    if not canvas.winfo_exists():
        return
    if iteracion < 120:
        canvas.move(pj2_id, 1, 2.5)
        #aumenta el tamaño del personaje 2 para simular acercamiento
        zoom_factor_pj2_escena3_num =1.0 +  (iteracion * 0.015)
        
        w, h = pj2_img.size
        pj2_img_zoom = pj2_img.resize((int(w * zoom_factor_pj2_escena3_num), int(h * zoom_factor_pj2_escena3_num)))
        zoom_factor_pj2_escena3 = ImageTk.PhotoImage(pj2_img_zoom)
        canvas.itemconfig(pj2_id, image=zoom_factor_pj2_escena3)
        
        
        ventana.after(50, lambda: mover_personaje2_escena3(iteracion + 1))
    else: 
        escena_actual_cin = 4
        cargar_siguiente_escena()

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
    mover_pj2_escena4(0) #inicia el movimiento del personaje 2 en la escena 4

    
def mover_fondo4():
    global direccion, escena_actual_cin
    
    if escena_actual_cin != 4:
        return
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
    global espejo, escena_actual_cin
    if escena_actual_cin != 4:
        return
    if espejo:
        canvas.itemconfig(pj1_id, image=canvas.pj1_normal_escena4) #cambia a la imagen normal
    else:
        canvas.itemconfig(pj1_id, image=canvas.pj1_espejo_escena4) #cambia a la imagen espejo
    espejo = not espejo #cambia el estado del espejo para la siguiente iteracion
    ventana.after(750, movimiento_pj1_escena4) #llama a esta funcion cada 50 milisegundos
    
    # canvas.move(pj1_id, 0, 2) #mueve el personaje 1 hacia abajo
    # ventana.after(50, movimiento_pj1_escena4) #llama a esta funcion cada 50 milisegundos
    
def mover_pj2_escena4(iteracion =0):
    global balanceo_dir, direccion, escena_actual_cin
    if escena_actual_cin != 4:
        return
    if iteracion < 24:
        canvas.move(pj2_id, 0, balanceo_dir * -2)
        
        x, y = canvas.coords(fondo_id) #obtiene las coordenadas actuales del 
    
        if y >= 0: 
            balanceo_dir = -1 
        elif y <= -4: 
            balanceo_dir = 1 
        canvas.update() #actualiza el canvas para mostrar el movimiento
        ventana.after(250, lambda: mover_pj2_escena4(iteracion + 1)) #llama a esta funcion cada 50 milisegundos
    else:
        escena_actual_cin = 5
        cargar_siguiente_escena()

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
    global pj1_id, pj1_img, pj1, pj2_id, pj2_img, pj2, zoom_factor, resta_zoom_pjs_escena5, escena_actual_cin
    if escena_actual_cin != 5:
        return
    if iteracion < 49: #limita el movimiento a 20 iteraciones
        canvas.move(pj1_id, 0, -4) #mueve el personaje 1 hacia arriba
        canvas.move(pj2_id, 0, -4) #mueve el personaje 2 hacia arriba
        

        zoom_factor -= resta_zoom_pjs_escena5
        
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
        
        resta_zoom_pjs_escena5 -= 0.0002
        #///zoom pj1///
        canvas.update() #actualiza el canvas para mostrar el cambio de imagen
        ventana.after(100, lambda: mover_pjs_escena5(iteracion +1)) #llama a esta funcion cada 50 milisegundos
       
    else:
        escena_actual_cin = 6
        cargar_siguiente_escena()
def escena6():
    global fondo_img, fondo, fondo_id
    global pj1_img, pj1, pj1_id 
    global pj2_img, pj2, pj2_id
    global direccion, balanceo_dir, zoom_factor
    global relay_img, relay, relay_id
    
    canvas.update() #actualiza el canvas para mostrar el cambio de imagen
    canvas.delete("all") #limpia el canvas para la nueva escena
    
    # Cargar la imagen de fondo
    fondo_img = Image.open("escenario 6 cofre.jpeg")
    fondo_img = fondo_img.resize((700, 690))
    fondo = ImageTk.PhotoImage(fondo_img)
    fondo_id = canvas.create_image(0, 0,anchor="nw", image=fondo)

    #personaje 1
    frame_inicial_link = 20
    
    pj1_img = obtener_frame_link(frame_inicial_link)
    pj1_img = pj1_img.resize((65, 70))  #tamano de link ancho x alto
    pj1 = ImageTk.PhotoImage(pj1_img)   
    pj1_id = canvas.create_image(140, 590, anchor="center", image=pj1) #coordenadas de link x y

    #personaje 2
    
    frame_inicial_frisk = 2
    
    pj2_img = obtener_frame_frisk(frame_inicial_frisk)
    pj2_img = pj2_img.resize((80, 100))  #tamano de zelda ancho x alto
    pj2 = ImageTk.PhotoImage(pj2_img)
    pj2_id = canvas.create_image(570, 698, anchor="center", image=pj2) #coordenadas de zelda x y
    
    #relay
    relay_img = Image.open("relay.png")
    relay_img = relay_img.resize((80, 80))  #tamano de zelda ancho x alto
    relay = ImageTk.PhotoImage(relay_img)
    relay_id = canvas.create_image(472, 430, anchor="center", image=relay)
    
    direccion = 1.0
    balanceo_dir =  1.0
    zoom_factor = 1.0
    
    ventana.after(2000, lambda: movimiento_pjs_escena6_pt2()) #inicia el movimiento del personaje 1 en la escena 6 despues de 2 segundos

    
def movimiento_pjs_escena6_pt2(iteracion=0):
    global pj1_id, pj1, pj2_id, pj2, pj1_img, pj2_img
    global escena_actual_cin
    
    if escena_actual_cin != 6:
        return
    if iteracion <17: #si el personaje 1 esta en la posicion del cofre
        ##---pj2---
        canvas.coords(pj2_id, 230, 555) #obtiene las coordenadas actuales del personaje 2
        
        pj2_img = obtener_frame_frisk(4) #importa imagen
        pj2_img = pj2_img.resize((50, 65))  #tamano de zelda ancho x alto
        pj2 = ImageTk.PhotoImage(pj2_img)
        
        
        canvas.itemconfig(pj2_id, image=pj2) #actualiza la imagen del personaje 2 en el canvas
        
        #////pj1///
        sprite_inicial_link = 30
        total_frames_link = 3
        
        num_archivo_link = sprite_inicial_link + (iteracion % total_frames_link) #cambia el frame cada 3 iteraciones\
            
        canvas.coords(pj1_id, 595, 560) #obtiene las coordenadas actuales del personaje 1

        pj1_img = obtener_frame_link(sprite_inicial_link) #importa imagen
        pj1_img = pj1_img.resize((55, 70))  #tamano de link ancho x alto
        pj1 = ImageTk.PhotoImage(pj1_img)   
        canvas.itemconfig(pj1_id, image=pj1) #actualiza la imagen del personaje 1 en el canvas
        
       
        img_link_pil = obtener_frame_link(num_archivo_link)
        w_link, h_link = 65, 70
    
        img_link_res = img_link_pil.resize((int(w_link), int(h_link)))
        pj1 = ImageTk.PhotoImage(img_link_res)
        canvas.itemconfig(pj1_id, image=pj1) #actualiza la imagen del personaje 1 en el canvas
        
        canvas.update() #actualiza el canvas para mostrar el cambio de imagen
        ventana.after(300, lambda: movimiento_pjs_escena6_pt2(iteracion + 1)) #llama a esta funcion cada 50 milisegundos
    else: 
        movimiento_pjs_escena6_pt3() #inicia la siguiente parte del movimiento de los personajes en la escena 6
        
def movimiento_pjs_escena6_pt3(iteracion=0):
    global pj1_id, pj1, pj2_id, pj2, pj1_img, pj2_img, frame_inicial_link, frame_inicial_frisk
    global escena_actual_cin
    
    if escena_actual_cin != 6:
        return
    canvas.coords(pj1_id, 143, 643) #obtiene las coordenadas actuales del personaje 1

    pj1_img = Image.open("link_escena6.png") #importa imagen
    pj1_img = pj1_img.resize((19, 45))  #tamano de link ancho x alto
    pj1 = ImageTk.PhotoImage(pj1_img)
    canvas.itemconfig(pj1_id, image=pj1) #actualiza la imagen del personaje 1 en el canvas
    
    if iteracion < 7: #si el personaje 2 esta en la posicion del cofre
        #///pj2//
        canvas.coords(pj2_id, 305, 535) #obtiene las coordenadas actuales del personaje 2
        sprites_frisk = [10, 7, 4]
        
        num_archivo_frisk = sprites_frisk[iteracion % len(sprites_frisk)] #cambia el frame cada 2 iteraciones\
        
        
        img_frisk_pil = obtener_frame_frisk(num_archivo_frisk)
        w_frisk, h_frisk = 35, 40
        
        img_frisk_res = img_frisk_pil.resize((int(w_frisk), int(h_frisk)))
        pj2 = ImageTk.PhotoImage(img_frisk_res)
        
        canvas.itemconfig(pj2_id, image=pj2) #actualiza la imagen del personaje 2 en el canvas
        
        canvas.update() #actualiza el canvas para mostrar el cambio de imagen
        ventana.after(600, lambda: movimiento_pjs_escena6_pt3(iteracion + 1)) #llama a esta funcion cada 50 milisegundos
    else:
        movimiento_pjs_escena6_pt4() #inicia la siguiente parte del movimiento de los personajes en la escena 6

def movimiento_pjs_escena6_pt4(iteracion=0):
    global pj1_id, pj1, pj2_id, pj2, pj1_img, pj2_img, frame_inicial_link, frame_inicial_frisk
    global relay_id, relay_img, relay
    global escena_actual_cin
    
    if escena_actual_cin != 6: 
        return
    if iteracion < 10:
        canvas.coords(pj2_id, 370, 750) #obtiene las coordenadas actuales del personaje 1
        pj2_img = Image.open("Frisk.png") #importa imagen
        pj2_img = pj2_img.resize((1700, 1700))  #tamano de zelda ancho x alto
        pj2 = ImageTk.PhotoImage(pj2_img)
        canvas.itemconfig(pj2_id, image=pj2) #actualiza la imagen
        
        #---relay---
        canvas.coords(relay_id, 1900, 750) #obtiene las coordenadas actuales del relay
        relay = ImageTk.PhotoImage(relay_img)
        canvas.itemconfig(relay_id, image=relay) #actualiza la imagen del relay en el canvas
        
        ventana.after(400, lambda: movimiento_pjs_escena6_pt4(iteracion + 1)) #llama a esta funcion cada 50 milisegundos
    else:
        pj2_img = pj2_img.resize((15, 15))  #tamano de zelda ancho x alto
        pj2 = ImageTk.PhotoImage(pj2_img)
        canvas.itemconfig(pj2_id, image=pj2) #actualiza la imagen
        movimiento_pjs_escena6_pt5() #inicia la siguiente parte del movimiento de los personajes en la escena 6

def movimiento_pjs_escena6_pt5(iteracion=0):
    global pj1_id, pj1, pj2_id, pj2, pj1_img, pj2_img
    global relay_id, relay_img, relay
    global escena_actual_cin
    
    if escena_actual_cin != 6:
        return
    if iteracion < 15:
        
        frame_inicial_link = 0
        total_frames_link = 3
        num_archivo_link = frame_inicial_link + (iteracion % total_frames_link) #cambia el frame cada 3 iteraciones\
            
        canvas.coords(pj1_id, 370, 380) #obtiene las coordenadas actuales del personaje 2

        canvas.itemconfig(pj1_id, image=pj1) #actualiza la imagen del personaje 1 en el canvas
        img_link_pil = obtener_frame_link(num_archivo_link)
        w_link, h_link = 1500, 1500 
        img_link_res = img_link_pil.resize((int(w_link), int(h_link)))
        pj1 = ImageTk.PhotoImage(img_link_res)
        canvas.itemconfig(pj1_id, image=pj1) #actualiza la imagen del personaje 1 en el canvas
        canvas.update() #actualiza el canvas para mostrar el cambio de imagen
        ventana.after(200, lambda: movimiento_pjs_escena6_pt5(iteracion + 1)) #llama a esta funcion cada 50 milisegundos
    
    else:
        pj1_img = pj1_img.resize((15, 15))  #tamano de link ancho x alto
        pj1 = ImageTk.PhotoImage(pj1_img)
        canvas.itemconfig(pj1_id, image=pj1) #actualiza la imagen del personaje 1 en el canvas
        
        #---relay---
        canvas.coords(relay_id, 472, 430) #obtiene las coordenadas actuales del relay
        relay = ImageTk.PhotoImage(relay_img)
        canvas.itemconfig(relay_id, image=relay) #actualiza la imagen del relay en el canvas
        movimiento_pjs_escena6_pt6() #inicia la siguiente parte del movimiento de los personajes en la escena 6

def movimiento_pjs_escena6_pt6(iteracion=0):
    global pj1_id, pj1, pj2_id, pj2, pj1_img, pj2_img
    global escena_actual_cin
    
    if escena_actual_cin != 6:
        return
    if iteracion < 5:
        #///pj2///
        if iteracion ==0:
             canvas.coords(pj2_id, 450, 560) #obtiene las coordenadas actuales del personaje 2
        sprites_frisk = [10, 7]
        
        num_archivo_frisk = sprites_frisk[iteracion % len(sprites_frisk)] #cambia el frame cada 2 iteraciones\
        
        
        img_frisk_pil = obtener_frame_frisk(num_archivo_frisk)
        w_frisk, h_frisk = 35, 40
        
        img_frisk_res = img_frisk_pil.resize((int(w_frisk), int(h_frisk)))
        pj2 = ImageTk.PhotoImage(img_frisk_res)
        
        canvas.itemconfig(pj2_id, image=pj2) #actualiza la imagen del personaje 2 en el canvas
        
        canvas.update() #actualiza el canvas para mostrar el cambio de imagen
       
        if iteracion == 0:
            canvas.coords(pj1_id, 500, 560) #obtiene las coordenadas actuales del personaje 1
        sprites_link = [60, 10]
        
        num_archivo_link = sprites_link[iteracion % len(sprites_link)] #cambia el frame cada 2 iteraciones\
            
        img_link_pil = obtener_frame_link(num_archivo_link)
        w_link, h_link = 35, 40
        img_link_res = img_link_pil.resize((int(w_link), int(h_link)))
        pj1 = ImageTk.PhotoImage(img_link_res)
        canvas.itemconfig(pj1_id, image=pj1) #actualiza la imagen del personaje 1 en el canvas
        
        canvas.update() #actualiza el canvas para mostrar el cambio de imagen
        ventana.after(2000, lambda: movimiento_pjs_escena6_pt6(iteracion + 1)) #llama a esta funcion cada 50 milisegundos
    else:
        movimiento_pjs_escena6_pt7() #inicia la siguiente parte del movimiento de los personajes en la escena 6
   
def movimiento_pjs_escena6_pt7(iteracion=0):
    global pj1_id, pj1, pj2_id, pj2, pj1_img, pj2_img
    global relay_id, relay_img, relay
    global direccion
    global escena_actual_cin
    
    if escena_actual_cin != 6:
        return
    if iteracion < 65:
       #relay
        if iteracion == 0:
            canvas.coords(relay_id, 350, 335) #obtiene las coordenadas actuales del relay
        relay_img = Image.open("Relay1.jpg")
        relay_img = relay_img.resize((700, 730))  #tamano de zelda ancho x alto
        relay = ImageTk.PhotoImage(relay_img)
        canvas.itemconfig(relay_id, image=relay) #actualiza la imagen del relay
        canvas.move(relay_id, 0, direccion * 2) #mueve el fondo en la direccion actual
        
        x, y = canvas.coords(relay_id) #obtiene las coordenadas actuales del fondo
        
        if y >= 335:
            direccion = -1
        elif y <= 325:
            direccion = 1
            

        ventana.after(30, lambda: movimiento_pjs_escena6_pt7(iteracion + 1)) #llama a esta funcion cada 50 milisegundos
    else:
        escena_actual_cin = 7
        cargar_siguiente_escena()
        
def escena7():
    global fondo_img, fondo, fondo_id
    global pj1_img, pj1, pj1_id 
    global pj2_img, pj2, pj2_id
    global direccion, balanceo_dir, zoom_factor
    global angulo_propio, angulo_orbita, radio_espiral
    
    
    canvas.update() #actualiza el canvas para mostrar el cambio de imagen
    canvas.delete("all") #limpia el canvas para la nueva escena
    
    # Cargar la imagen de fondo
    fondo_img = Image.open("escenario 7 espiral.jpg")
    fondo_img = fondo_img.resize((700, 700))
    fondo = ImageTk.PhotoImage(fondo_img)
    fondo_id = canvas.create_image(0, 0,anchor="nw", image=fondo)
    
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
    
    direccion = 1.0
    balanceo_dir =  1.0
    zoom_factor = 1.0
    angulo_orbita = 0.0
    angulo_propio = 0
    radio_espiral = 300.0
    
    mov_escena7()
    
def mov_escena7(iteracion = 0):
    global pj1, pj1_img, pj1_id
    global pj2, pj2_img, pj2_id
    global angulo_orbita, angulo_propio, radio_espiral
    global escena_actual_cin
    
    if not canvas.winfo_exists():
        return
    
    if iteracion <  100 and radio_espiral > 5:
        #centro de la img
        centro_x = 350
        centro_y = 345
        
        #gira en circulos
        angulo_orbita += 0.15
        #acerca el centro
        radio_espiral -= 3.0
        
        #posicion
        nuevo_x1 = centro_x + (radio_espiral * math.cos(angulo_orbita))
        nuevo_y1 = centro_y + (radio_espiral * math.sin(angulo_orbita))
        
        angulo_orbita2 = angulo_orbita + math.pi
        
        nuevo_x2 = centro_x + (radio_espiral * math.cos(angulo_orbita2))
        nuevo_y2 = centro_y + (radio_espiral * math.sin(angulo_orbita2))
        #movemos al nene
        canvas.coords(pj1_id, nuevo_x1, nuevo_y1)
        canvas.coords(pj2_id, nuevo_x2, nuevo_y2)
        
        #Rotacion viva la coca
        angulo_propio =(angulo_propio + 12) % 360
        
        pj1_img = Image.open("link.png")
        pj2_img = Image.open("Frisk.png")
        
        #escala
        escala = radio_espiral / 300.0 
        if escala < 0.1: 
            escala = 0.1 #limite de size
        
        w, h = int(75 * escala), int (85 * escala)
        img_petit1 = pj1_img.resize((w, h))
        img_petit2 = pj2_img.resize((w, h))
        
        #no fumen
        img_rotada1 = img_petit1.rotate(angulo_propio, expand= True)
        img_rotada2 = img_petit2.rotate(angulo_propio, expand= True)
        
        #updateo el canvas para q tk lo lea
        pj1 = ImageTk.PhotoImage(img_rotada1)
        canvas.itemconfig(pj1_id, image=pj1)
        pj2 = ImageTk.PhotoImage(img_rotada2)
        canvas.itemconfig(pj2_id, image=pj2)
        
        
        #RECURSIVIDAD PAQ VEA Q SI SE NOJOA
        ventana.after(40, lambda: mov_escena7(iteracion + 1))
    else: 
        escena_actual_cin = 8
        cargar_siguiente_escena()
      
        

#---carga de escena----


def cargar_siguiente_escena ():
    global cargar_siguiente_escena
    
    canvas.delete("all")
    if escena_actual_cin == 1:
        escena1()
    elif escena_actual_cin == 2:
        escena2()
    elif escena_actual_cin == 3:
        escena3()
    elif escena_actual_cin == 4:
        escena4()
    elif escena_actual_cin == 5:
        escena5()
    elif escena_actual_cin == 6:
        escena6()
    elif escena_actual_cin == 7:
        escena7()
    elif escena_actual_cin == 8:
        ventana.destroy
        import kabra_con_guardado

        kabra_con_guardado()
    
escena5()
    
    

# escena7() #inicia la sexta escena


ventana.mainloop()


