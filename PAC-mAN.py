"""PAC-MAN"""

import tkinter as tk

import random

ventana =tk.Tk()

ventana.title("Pac-Man")
ventana.resizable = False, False

size_celda = 20

# 1 = Muro 
# 2 = puntos 
# 3  pastilla 
# 0 = vacio 
# 4 = compuerta Fantasma
matriz_pacman = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
    [1,3,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,3,1],
    [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1],
    [1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1],
    [1,2,2,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,2,2,1],
    [1,1,1,1,1,1,2,1,1,1,1,1,0,1,1,0,1,1,1,1,1,2,1,1,1,1,1,1],
    [0,0,0,0,0,1,2,1,1,1,1,1,0,1,1,0,1,1,1,1,1,2,1,0,0,0,0,0],
    [0,0,0,0,0,1,2,1,1,0,0,0,0,0,0,0,0,0,0,1,1,2,1,0,0,0,0,0],
    [0,0,0,0,0,1,2,1,1,0,1,1,1,4,4,1,1,1,0,1,1,2,1,0,0,0,0,0],
    [1,1,1,1,1,1,2,1,1,0,1,0,0,0,0,0,0,1,0,1,1,2,1,1,1,1,1,1],
    [0,0,0,0,0,0,2,0,0,0,1,0,0,0,0,0,0,1,0,0,0,2,0,0,0,0,0,0],
    [1,1,1,1,1,1,2,1,1,0,1,0,0,0,0,0,0,1,0,1,1,2,1,1,1,1,1,1],
    [0,0,0,0,0,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,0,0,0,0,0],
    [0,0,0,0,0,1,2,1,1,0,0,0,0,0,0,0,0,0,0,1,1,2,1,0,0,0,0,0],
    [0,0,0,0,0,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,0,0,0,0,0],
    [1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
    [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
    [1,3,2,2,1,1,2,2,2,2,2,2,2,0,0,2,2,2,2,2,2,2,1,1,2,2,3,1],
    [1,1,1,2,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1],
    [1,1,1,2,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1],
    [1,2,2,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,2,2,1],
    [1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1],
    [1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]


juego_activo = True

pacman_fila = 23
pacman_col =13
pacman_id = None
score_texto_id = None
boca_pacman = True
bareta_visible = True
vidas_pacman = 3
iconos_vidas_id = []

#///marcador///
margen_arriba = 60


ancho_canvas = len(matriz_pacman[0]) *size_celda
alto_canvas = (len(matriz_pacman) * size_celda) + margen_arriba + 40

#///puntos///
mapa_ids_bolitas = {}
puntuacion = 0

#///movimiento///

pacman_dx = 0
pacman_dy = 0
pacman_deseo_dx = 0
pacman_deseo_dy = 0

canvas = tk.Canvas(ventana, width= ancho_canvas, height= alto_canvas, bg="#0000d2")
canvas.pack()

##??//--FASTASTMAS--//??
modo_fantasma = "scatter"
modo_anterior = "scatter"

blinky_fila = 11
blinky_col = 13
blinky_id = None
blinky_dx = -1
blinky_dy = 0
blinky_perrito = 0
blinky_muerto = False
blinky_pupula_right_id= None
blinky_pupila_left_id = None
blinky_ojo_right_id = None
blinky_ojo_left_id = None
blinky_afuera = True

pinky_fila =  14
pinky_col =14
pinky_dx = 0
pinky_dy = -1
pinky_perrito = 0
pinky_muerto = False
pinky_id = None
pinky_pupula_right_id= None
pinky_pupila_left_id = None
pinky_ojo_right_id = None
pinky_ojo_left_id = None
pinky_afuera = False

inky_fila = 14
inky_col = 12
inky_dx = 0
inky_dy = -1
inky_perrito = 0
inky_muerto = False
inky_afuera = False
inky_id = None
inky_ojo_left_id = None
inky_ojo_right_id = None
inky_pupila_left_id = None
inky_pupila_right_id = None

clyde_fila = 14
clyde_col = 15
clyde_dx = 0
clyde_dy = -1
clyde_perrito = 0
clyde_muerto = False
clyde_afuera = False
clyde_id = None
clyde_ojo_left_id = None
clyde_ojo_right_id = None
clyde_pupila_left_id = None
clyde_pupila_right_id = None


pausado = False

def win():
    global juego_activo
    
    if vidas_pacman <= 0:
        juego_activo = False
        
        print("game over")
        
        return
    if len(mapa_ids_bolitas) == 0:
        juego_activo =False
        print("yujuu")
        
        return

def mapa_pacman():
    
    grosor_borde = 3
    for fila in range(len(matriz_pacman)):
        for col in range(len(matriz_pacman[fila])):
            
            x1 = col * size_celda
            y1 = (fila * size_celda) +margen_arriba
            x2 = x1 + size_celda
            y2 = y1 + size_celda
            
            tipo = matriz_pacman[fila][col]
            
            if tipo in [0, 2, 3, 4]:
                canvas.create_rectangle(x1, y1, x2, y2, fill="black", outline="")
        

            
            if tipo == 1:
                grosor_borde = 2
                canvas.create_rectangle(
                    x1 + grosor_borde, 
                    y1 + grosor_borde, 
                    x2 - grosor_borde, 
                    y2 - grosor_borde, 
                    fill="black", 
                    outline =""
                )
            cx = x1 + (size_celda // 2)
            cy = y1 + (size_celda // 2)
            
            if tipo == 2:
                radio = 2
                id_bolita = canvas.create_oval(cx - radio, cy - radio, cx + radio, cy + radio, 
                                   fill="#ffb8ae", outline="#ffb8ae")
                mapa_ids_bolitas[(fila, col)]= id_bolita
            
            elif tipo == 3:
                radio = 5
                id_bolita = canvas.create_oval(cx - radio, cy - radio, cx + radio, cy + radio, 
                                   fill="#ffb8ae", outline="#ffb8ae")
                mapa_ids_bolitas[(fila, col)] = id_bolita
            elif tipo == 4:
                canvas.create_line(x1, cy, x2, cy, fill="white", width=2)
                
def crear_pacman():
    global pacman_id
    x1 = pacman_col *size_celda
    y1 = pacman_fila *size_celda
    x2 = x1 + size_celda
    y2 = y1 +size_celda
    
    pacman_id = canvas.create_arc(
        x1 + 2, y1 + 2, x2 -2, y2 - 2,
        fill="yellow",
        outline="yellow",
        start=30,
        extent=300,
        style=tk.PIESLICE 
    )

def teclado_pacman(event):
    global pacman_dx, pacman_dy
    global pacman_deseo_dx, pacman_deseo_dy
    
    tecla = event.keysym.lower()
    
    if tecla in ["up", "w"]:
        pacman_deseo_dx = 0
        pacman_deseo_dy = -1
    elif tecla in ["down", "s"]:
        pacman_deseo_dx = 0
        pacman_deseo_dy = 1
    elif tecla in ["right", "d"]:
        pacman_deseo_dx = 1
        pacman_deseo_dy =0
    elif tecla in ["left", "a"]:
        pacman_deseo_dx = -1
        pacman_deseo_dy = 0
        
def mover_pacman():
    global pacman_col, pacman_fila, pacman_dy, pacman_dx, boca_pacman
    global pacman_deseo_dy, pacman_deseo_dx
    if not juego_activo:
        return
    
    test_fila_deseo = pacman_fila + pacman_deseo_dy
    test_col_deseo = pacman_col + pacman_deseo_dx
    
    giro_true = False
    if 0 <= test_fila_deseo < len(matriz_pacman) and 0 <= test_col_deseo < len(matriz_pacman[0]):
        casilla_deseo = matriz_pacman[test_fila_deseo][test_col_deseo]
        
        if casilla_deseo != 1 and casilla_deseo != 4:
            pacman_dx = pacman_deseo_dx
            pacman_dy = pacman_deseo_dy
            giro_true = True
    
    if not giro_true:
        nueva_fila = pacman_fila + pacman_dy
        nueva_col = pacman_col + pacman_dx    
    
    else:
        nueva_fila = test_fila_deseo
        nueva_col = test_col_deseo
    ##TUNEL____
    ancho_matriz = len(matriz_pacman[0])
    
    if nueva_col <0:
        nueva_col = ancho_matriz - 1
    elif nueva_col>= ancho_matriz:
        nueva_col = 0
    

    
    if 0 <= nueva_fila < len(matriz_pacman) and 0 <= nueva_col < len(matriz_pacman[0]):
        avance = matriz_pacman[nueva_fila][nueva_col]
        
        if avance != 1 and avance != 4:
            
            pacman_fila = nueva_fila
            pacman_col = nueva_col
            
            #HAce-- wakawaka--//
            wakawaka()
            
            ghost_busters()
            
            morido()
            
            win()
            
            if pacman_dx != 0 or pacman_dy != 0:
                #abre y cierra boca
                if boca_pacman:
                    
                    angulo_boca = 30
                    
                    if pacman_dx == -1:
                        angulo_boca = 210
                    elif pacman_dy == -1:
                        angulo_boca = 120
                    elif pacman_dy == 1:
                        angulo_boca = 300
                    
                    canvas.itemconfig(pacman_id, start=angulo_boca, extent= 300, style=tk.PIESLICE)
                else:
                    canvas.itemconfig(pacman_id, start= 0, extent= 359.9, style = tk.PIESLICE)
            
                boca_pacman =not boca_pacman
            
            x1 = pacman_col * size_celda
            y1 =  (pacman_fila * size_celda) + margen_arriba
            x2 = x1 + size_celda
            y2 = y1 + size_celda
            
            canvas.coords(pacman_id, x1 + 2, y1 + 2, x2 - 2, y2 - 2)

    ventana.after(150, mover_pacman)
        
def modo_frightened():
    global modo_fantasma
    modo_fantasma = "frightened"
    print ("🍬 ¡PAC-MAN SE METIÓ UN BAZUCO! Fantasmas asustados.")
    
    canvas.itemconfig(blinky_id, fill="#0000bb", outline="#0000bb")
    canvas.itemconfig(pinky_id, fill="#0000bb", outline="#0000bb")
    canvas.itemconfig(inky_id, fill="#0000bb", outline="#0000bb")
    canvas.itemconfig(clyde_id, fill="#0000bb", outline="#0000bb")
    
    canvas.itemconfig(blinky_pupila_left_id, fill= "#0000bb", outline="#0000bb")
    canvas.itemconfig(blinky_pupula_right_id, fill= "#0000bb", outline="#0000bb")
    
    canvas.itemconfig(pinky_pupila_left_id, fill= "#0000bb", outline="#0000bb")
    canvas.itemconfig(pinky_pupula_right_id, fill= "#0000bb", outline="#0000bb")
    
    canvas.itemconfig(inky_pupila_left_id, fill= "#0000bb", outline="#0000bb")
    canvas.itemconfig(inky_pupila_right_id, fill= "#0000bb", outline="#0000bb")
    
    canvas.itemconfig(clyde_pupila_left_id, fill= "#0000bb", outline="#0000bb")
    canvas.itemconfig(clyde_pupila_right_id, fill= "#0000bb", outline="#0000bb")
    
    ventana.after(7000, abstinencia)

def crear_vida ():
    global iconos_vidas_id
    suelo_y = (len(matriz_pacman) * size_celda) + margen_arriba + 10
    
    for i in range (vidas_pacman - 1):
        pos_x = 40 + (i * 25)
        
        id_vida = canvas.create_arc(
            pos_x, suelo_y, pos_x + 16, suelo_y + 16,
            fill= "yellow",
            outline="yellow",
            start= 210,
            extent= 300,
            style= "pieslice"
        )
        iconos_vidas_id.append(id_vida)


def morido():
    global vidas_pacman, pacman_fila, pacman_col, pacman_dx, pacman_dy
    global blinky_fila, blinky_col, blinky_afuera, pinky_fila, pinky_col, pinky_afuera
    global inky_fila, inky_col, inky_afuera, clyde_fila, clyde_col, clyde_afuera
    global blinky_muerto, pinky_muerto, inky_muerto, clyde_muerto
    
    if not juego_activo or modo_fantasma == "frightened":
        return
    
    fantasmas = [
        (blinky_fila, blinky_col, blinky_muerto),
        (pinky_fila, pinky_col, pinky_muerto),
        (inky_fila, inky_col, inky_muerto),
        (clyde_fila, clyde_col, clyde_muerto)
    ]
    for ff, cf, esta_morido in fantasmas:
        if pacman_fila == ff and pacman_col == cf and not esta_morido:
            vidas_pacman -= 1
            
            animar_morido()
            return
    
def animar_morido (angulo_actual = 300):
    global juego_activo, pacman_fila, pacman_col, pacman_dx, pacman_dy
    
    juego_activo = False
    if angulo_actual > 0:
        canvas.itemconfig(pacman_id, extent= angulo_actual)
        ventana.after(60, lambda: animar_morido(angulo_actual - 30))
    
    else:
        canvas.itemconfig(pacman_id, extent= 0)
        ventana.after(1500, reiniciar_morido)
        
def reiniciar_morido ():
    global juego_activo, pacman_fila, pacman_col, pacman_dx, pacman_dy
    global blinky_fila, blinky_col, blinky_afuera, pinky_fila, pinky_col, pinky_afuera
    global inky_fila, inky_col, inky_afuera, clyde_fila, clyde_col, clyde_afuera
    
    pacman_fila, pacman_col = 23, 13
    pacman_dx, pacman_dy = 0, 0
    
    blinky_fila, blinky_col, blinky_afuera = 11, 13, True
    pinky_fila, pinky_col, pinky_afuera = 14, 14, True
    inky_fila, inky_col, inky_afuera = 14, 12, True
    clyde_fila, clyde_col, clyde_afuera = 14, 15, True
    
    canvas.itemconfig(pacman_id, start = 30, extent = 300)
    
    x1 = pacman_col *size_celda
    y1 = (pacman_fila * size_celda) +margen_arriba
    canvas.coords(pacman_id, x1 + 2, y1 + 1, x1 + size_celda - 2, y1 + size_celda - 2)
    
    juego_activo = True
    mover_pacman()
def abstinencia():
    global modo_fantasma, modo_anterior
    
    if modo_fantasma != "frightened":
        return
    
    modo_fantasma = modo_anterior
    print("⚠️ ¡los fastasmas estan en abstinencia y periguen la keta que se metio pacman!")
    if not blinky_muerto:
        canvas.itemconfig(blinky_id, fill="red", outline="red")
        canvas.itemconfig(blinky_pupila_left_id, fill="blue", outline="blue")
        canvas.itemconfig(blinky_pupula_right_id, fill="blue", outline="blue")
    
    if not pinky_muerto:
        canvas.itemconfig(pinky_id, fill="#FFB8FF", outline="#FFB8FF")
        canvas.itemconfig(pinky_pupila_left_id, fill="blue", outline="blue")
        canvas.itemconfig(pinky_pupula_right_id, fill="blue", outline="blue")

    if not inky_muerto:
        canvas.itemconfig(inky_id, fill="#00FFFF", outline="#00FFFF")
        canvas.itemconfig(inky_pupila_left_id, fill="blue", outline="blue")
        canvas.itemconfig(inky_pupila_right_id, fill="blue", outline="blue")
    
    if not clyde_muerto:
        canvas.itemconfig(clyde_id, fill="#FFB852", outline="#FFB852")
        canvas.itemconfig(clyde_pupila_left_id, fill="blue", outline="blue")
        canvas.itemconfig(clyde_pupula_right_id, fill="blue", outline="blue")

def wakawaka ():
    global puntuacion
    casilla_actual = matriz_pacman[pacman_fila][pacman_col]
    
    if casilla_actual == 2 or casilla_actual == 3:
        
        if casilla_actual == 2:
            puntuacion += 10
        elif casilla_actual == 3:
            puntuacion += 50
            
            modo_frightened()
        
        coordenada = (pacman_fila, pacman_col)
        if coordenada in mapa_ids_bolitas:
            id_amarillo = mapa_ids_bolitas[coordenada]
            
            canvas.delete(id_amarillo)
            
            del mapa_ids_bolitas[coordenada]
            
    matriz_pacman[pacman_fila][pacman_col] = 0
    
    canvas.itemconfig(score_texto_id, text=f"{puntuacion:02d}")
    win()

def crear_score():
    global score_texto_id
    
    canvas.create_text(
        40, 20,
        text="1UP",
        fill= "white",
        font =("Courier", 16, "bold"),
        anchor= "nw"
    )
    
    score_texto_id = canvas.create_text(
        40, 40, 
        text= "00",
        fill= "white",
        font= ("Courier", 16, "bold"),
        anchor= "nw"
    )
    
    mitad_ancho = ancho_canvas //2
    canvas.create_text(
        mitad_ancho, 20,
        text = "HIGH SCORE",
        fill= "white",
        font= ("Courier", 16, "bold"),
        anchor = "n"
    )
    
    canvas.create_text(
        mitad_ancho, 40,
        text= "5000",
        fill= "white",
        font= ("Courier", 16, "bold"),
        anchor= "n"
    )
    
def viva_bazuco ():
    global bareta_visible
    posicion_bareta = [(3, 1), (3, 26), (23, 1), (23, 26)]
    
    color_actual = "#ffb8ae" if bareta_visible else "black"
    for fila, col in posicion_bareta:
        if matriz_pacman[fila][col] == 3:
            coordenada = (fila, col)
            
            if coordenada in mapa_ids_bolitas:
                id_grafico =mapa_ids_bolitas[coordenada]
                canvas.itemconfig(id_grafico, fill= color_actual, outline=color_actual)
    
    bareta_visible = not bareta_visible
    
    ventana.after(200, viva_bazuco)
    
def ghost_busters():
    global puntuacion, modo_fantasma
    global blinky_fila, blinky_col, blinky_muerto, blinky_dx, blinky_dy, blinky_perrito
    global pinky_fila, pinky_col, pinky_muerto, pinky_dx, pinky_dy, pinky_perrito, pinky_afuera
    global inky_fila, inky_col, inky_muerto, inky_dx, inky_dy, inky_perrito, inky_afuera
    global clyde_fila, clyde_col, clyde_muerto, clyde_dx, clyde_dy, clyde_perrito, clyde_afuera
    
    if modo_fantasma != "frightened":
        return
    
    if pacman_fila == blinky_fila and pacman_col == blinky_col and not blinky_muerto:
        puntuacion += 200
        blinky_muerto = True
        blinky_dx, blinky_dy = 0, 0
        # Borramos el cuerpo rojo/azul (fill="") dejando solo los ojos blancos y pupilas
        canvas.itemconfig(blinky_id, fill="", outline="")
        canvas.itemconfig(blinky_pupila_left_id, fill="blue", outline="blue")
        canvas.itemconfig(blinky_pupula_right_id, fill="blue", outline="blue")  
        print("🎯 ¡Blinky devorado! Sus ojos corren a la casa.")
        
    if pacman_fila == pinky_fila and pacman_col == pinky_col and not pinky_muerto:
        puntuacion += 200
        pinky_muerto = True
        pinky_dx, pinky_dy = 0, 0
        canvas.itemconfig(pinky_id, fill="", outline="")
        canvas.itemconfig(pinky_pupila_left_id, fill="blue", outline="blue")
        canvas.itemconfig(pinky_pupula_right_id, fill="blue", outline="blue")
        canvas.itemconfig(score_texto_id, text=f"{puntuacion:02d}")
        print("🎯 ¡Pinky devorada! Sus ojos corren a la casa.")
        
    if pacman_fila == inky_fila and pacman_col == inky_col and not inky_muerto:
        puntuacion += 200
        inky_muerto = True
        inky_dx, inky_dy = 0, 0
        canvas.itemconfig(inky_id, fill="", outline="")
        canvas.itemconfig(inky_pupila_left_id, fill="blue", outline="blue")
        canvas.itemconfig(inky_pupila_right_id, fill="blue", outline="blue")
        canvas.itemconfig(score_texto_id, text=f"{puntuacion:02d}")
        print("🎯 ¡Inky devorado! Sus ojos corren a la casa.")
        
    if pacman_fila == clyde_fila and pacman_col == clyde_col and not clyde_muerto:
        puntuacion += 200
        clyde_muerto = True
        clyde_dx, clyde_dy = 0, 0
        canvas.itemconfig(clyde_id, fill="", outline="")
        canvas.itemconfig(clyde_pupila_left_id, fill="blue", outline="blue")
        canvas.itemconfig(clyde_pupula_right_id, fill="blue", outline="blue")
        canvas.itemconfig(score_texto_id, text=f"{puntuacion:02d}")
        print("🎯 ¡Clyde devorado! Sus ojos corren a la casa.")
        
#??//funciones de fastasmas///??

def reloj_modo_ia():
    global modo_fantasma, modo_anterior
    
    if modo_fantasma == "frightened":
        ventana.after(1000, reloj_modo_ia)
        return
    if modo_fantasma == "scatter":
        modo_fantasma = "chase"
        modo_anterior = "chase"
        ventana.after(20000, reloj_modo_ia)
        
    elif modo_fantasma == "chase":
        modo_fantasma = "scatter"
        modo_anterior = "scatter"
        ventana.after(7000, reloj_modo_ia)
def crear_blinky():
    global blinky_id
    global blinky_pupula_right_id, blinky_pupila_left_id, blinky_ojo_left_id, blinky_ojo_right_id
    
    x1 = blinky_col * size_celda
    y1 = (blinky_fila * size_celda) + margen_arriba
    x2 = x1 + size_celda
    y2 = y1 + size_celda
    
    mx1, my1 =x1 + 2, y1 + 2
    mx2, my2 = x2 - 2, y2 - 2
    
    ancho_util = mx2 - mx1
    p1_x = mx1 + (ancho_util * 0.25)
    p2_x = mx1 + (ancho_util * 0.5)
    p3_x = mx1 + (ancho_util * 0.75)
    alto_picos_y = my2 - 4
    
    puntos_blinky = [
        mx1, my2, 
        mx1, my1 + 8,
        mx1 + 4, my1 + 2,
        mx2 - 4, my1 + 2,
        mx2, my1 + 8,
        mx2, my2,
        p3_x, alto_picos_y,
        p2_x, my2,
        p1_x, alto_picos_y
    ]
    
    blinky_id = canvas.create_polygon(puntos_blinky, fill= "#FF0000", outline="#FF0000")
    
    blinky_ojo_left_id = canvas.create_oval(mx1 + 2, my1 + 4, mx1 + 7, my1 + 10, fill="white", outline="white")
    blinky_ojo_right_id = canvas.create_oval(mx2 - 7, my1 + 4, mx2 - 2, my1 + 10, fill="white", outline="white")
    
    blinky_pupila_left_id = canvas.create_oval(mx1 + 2, my1 + 6, mx1 + 5, my1 + 9, fill="blue", outline="blue")
    blinky_pupula_right_id = canvas.create_oval(mx2 - 7, my1 + 6, mx2 - 4, my1 + 9, fill="blue", outline="blue")
    
def mover_blinky ():
    global blinky_fila, blinky_col, blinky_dx, blinky_dy, blinky_afuera
    global modo_fantasma, blinky_perrito, blinky_muerto
    if not juego_activo: return
    
    if blinky_perrito > 0:
        blinky_perrito -= 1
        ventana.after(200, mover_blinky)
        return
    if blinky_fila >= 12 and not blinky_afuera:
        if blinky_col < 13:
            blinky_dx = 1; blinky_dy = 0
        elif blinky_col > 14:
            blinky_dx = -1; blinky_dy = 0
        else:
            blinky_dx = 0; blinky_dy = -1
    else:
        blinky_afuera = True
    if blinky_afuera:
        target_c = 0
        target_f = 0
        if blinky_muerto:
            target_f = 11
            target_c = 13
        elif modo_fantasma == "chase":
            target_f = pacman_fila
            target_c = pacman_col
        elif modo_fantasma == "scatter":
            target_f = -2
            target_c =25
        else:
            target_f = 0
            target_c = 0
        opcionesd_giro = []
        direcciones_posibles = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in direcciones_posibles:
            if dx == -blinky_dx and dy == -blinky_dy:
                continue
            test_f = blinky_fila + dy
            test_c = blinky_col + dx
            
            if 0 <= test_f <len(matriz_pacman) and 0 <= test_c < len(matriz_pacman[0]):
                if matriz_pacman[test_f][test_c] != 1 and matriz_pacman[test_f][test_c] != 4:
                    opcionesd_giro.append((dx, dy))
        if len(opcionesd_giro) > 0:
            f_recto = blinky_fila +blinky_dy
            c_recto = blinky_col + blinky_dx
            choque = True
            if 0 <= f_recto < len(matriz_pacman) and 0 <= c_recto <len(matriz_pacman[0]):
                if matriz_pacman[f_recto][c_recto] != 1:
                    choque = False
            if len(opcionesd_giro) > 1 or choque:
                if modo_fantasma == "frightened" and not blinky_muerto:
                    blinky_dx, blinky_dy = random.choice(opcionesd_giro)
                else:
                    mejor_dx, mejor_dy = blinky_dx, blinky_dy
                    distancia_min = float('inf')
                    for dx, dy in opcionesd_giro:
                        f_futuro = blinky_fila + dy
                        c_futuro = blinky_col + dx
                            
                        dist_cuadrado = (f_futuro - target_f)** 2 +(c_futuro - target_c)** 2
                        if dist_cuadrado < distancia_min:
                            distancia_min = dist_cuadrado
                            mejor_dx = dx
                            mejor_dy= dy
                    blinky_dx = mejor_dx
                    blinky_dy = mejor_dy
    ##MOVIMIENTO
    nueva_fila = blinky_fila + blinky_dy
    nueva_col = blinky_col + blinky_dx
    
    ancho_matriz = len(matriz_pacman[0])
    if nueva_col < 0:
        nueva_col = ancho_matriz -1
    elif nueva_col >= ancho_matriz:
        nueva_col = 0
    if 0 <= nueva_fila < len(matriz_pacman) and 0 <=nueva_col <len(matriz_pacman[0]):
        if matriz_pacman[nueva_fila][nueva_col] != 1 and (matriz_pacman[nueva_fila][nueva_col]  
        != 4 or not blinky_afuera):
            blinky_fila = nueva_fila
            blinky_col =nueva_col
                
            x1 = blinky_col *size_celda
            y1 = (blinky_fila * size_celda) +margen_arriba
            x2 = x1 + size_celda
            y2 = y1 + size_celda

            mx1, my1 = x1 + 2, y1 + 2
            mx2, my2 = x2 - 2, y2 - 2
            ancho_util = mx2 - mx1
            
            p1_x = mx1 + (ancho_util * 0.25)
            p2_x = mx1 + (ancho_util * 0.5)
            p3_x = mx1 + (ancho_util * 0.75)
            
            alto_picos_y = my2 - 4
            
            puntos_actualizados = [
                                mx1, my2, mx1, my1 + 8, mx1 + 4, my1 + 2, mx2 - 4, my1 + 2,
                                mx2, my1 + 8, mx2, my2, p3_x, alto_picos_y, p2_x, my2, p1_x, alto_picos_y
                            ]
            canvas.coords(blinky_id, puntos_actualizados)
            canvas.coords(blinky_ojo_left_id, mx1 + 2, my1 + 4, mx1 + 7, my1 + 10)
            canvas.coords(blinky_ojo_right_id, mx2 - 7, my1 + 4, mx2 - 2, my1 + 10)
            canvas.coords(blinky_pupila_left_id, mx1 + 4, my1 + 6, mx1 + 6, my1 + 8)
            canvas.coords(blinky_pupula_right_id, mx2 - 6, my1 + 6, mx2 - 4, my1 + 8)
            blinky_ojoalegre()
    ghost_busters()
    if blinky_muerto and blinky_fila == 11 and blinky_col == 13:
        blinky_fila = 14
        blinky_col = 11
    elif blinky_muerto and blinky_fila == 14 and blinky_col == 11:
        blinky_muerto = False
        blinky_afuera = False
        blinky_perrito = 10
        canvas.itemconfig(blinky_id, fill="red", outline="red")
        canvas.itemconfig(blinky_pupila_left_id, fill="blue", outline="blue")
        canvas.itemconfig(blinky_pupula_right_id, fill="blue", outline="blue")
    morido()
    win()
    canvas.update()
    
    velocidad_actual = 80 if blinky_muerto else 200
    ventana.after(velocidad_actual, mover_blinky)
    
def blinky_ojoalegre():
    
    x_base = blinky_col * size_celda
    y_base = (blinky_fila * size_celda) +margen_arriba   
    mx1, my1 = x_base + 2, y_base + 2
    
    centro_ojo_y = my1 + 7
    
    centro_ojo_left_x = mx1 + 4.5
    centro_ojo_right_x = mx1 + 13.5
    
    desfase_x_left = 0
    desfase_x_right = 0
    desfase_y = 0
    
    if blinky_dx == -1:
        desfase_x_left = -2
        desfase_x_right = -2
        desfase_y = 0
    elif blinky_dx == 1:
        desfase_x_left = 1.5
        desfase_x_right = 0.5
        desfase_y = 0
    elif blinky_dy == -1:
        desfase_x_left = -0.5
        desfase_x_right = -0.5
        desfase_y = -2
    elif blinky_dy == 1:
        desfase_x_left = -0.5
        desfase_x_right = -0.5
        desfase_y = 1.5       

    radio_pupila = 1.25

    cx_left = centro_ojo_left_x + desfase_x_left
    cx_right = centro_ojo_right_x + desfase_x_right
    cy = centro_ojo_y + desfase_y
        
    canvas.coords(blinky_pupila_left_id,
                  cx_left - radio_pupila,
                  cy - radio_pupila,
                  cx_left + radio_pupila,
                  cy + radio_pupila,
                  )
    canvas.coords(blinky_pupula_right_id,
                  cx_right - radio_pupila,
                  cy - radio_pupila,
                  cx_right + radio_pupila,
                  cy +radio_pupila)
    

def crear_pinky():
    global pinky_id
    global pinky_pupula_right_id, pinky_pupila_left_id, pinky_ojo_left_id, pinky_ojo_right_id
    
    x1 = pinky_col * size_celda
    y1 = (pinky_fila * size_celda) + margen_arriba
    x2 = x1 + size_celda
    y2 = y1 + size_celda
    
    mx1, my1 =x1 + 2, y1 + 2
    mx2, my2 = x2 - 2, y2 - 2
    
    ancho_util = mx2 - mx1
    p1_x = mx1 + (ancho_util * 0.25)
    p2_x = mx1 + (ancho_util * 0.5)
    p3_x = mx1 + (ancho_util * 0.75)
    alto_picos_y = my2 - 4
    
    puntos_pinky = [
        mx1, my2, 
        mx1, my1 + 8,
        mx1 + 4, my1 + 2,
        mx2 - 4, my1 + 2,
        mx2, my1 + 8,
        mx2, my2,
        p3_x, alto_picos_y,
        p2_x, my2,
        p1_x, alto_picos_y
    ]
    
    pinky_id = canvas.create_polygon(puntos_pinky, fill= "#FFB8FF", outline="#FFB8FF")
    
    pinky_ojo_left_id = canvas.create_oval(mx1 + 2, my1 + 4, mx1 + 7, my1 + 10, fill="white", outline="white")
    pinky_ojo_right_id = canvas.create_oval(mx2 - 7, my1 + 4, mx2 - 2, my1 + 10, fill="white", outline="white")
    
    pinky_pupila_left_id = canvas.create_oval(mx1 + 2, my1 + 6, mx1 + 5, my1 + 9, fill="blue", outline="blue")
    pinky_pupula_right_id = canvas.create_oval(mx2 - 7, my1 + 6, mx2 - 4, my1 + 9, fill="blue", outline="blue")
    
def mover_pinky():
    global pinky_fila, pinky_col, pinky_dx, pinky_dy
    global modo_fantasma, pinky_afuera, pinky_perrito, pinky_muerto
    
    if not juego_activo: return
    
    if pinky_perrito > 0:
        pinky_perrito -= 1
        ventana.after(200, mover_pinky)
        return
    
    if pinky_fila >= 12 and not pinky_afuera:
        if pinky_col < 13:
            pinky_dx = 1
            pinky_dy = 0
        elif pinky_col > 14:
            pinky_dx = -1
            pinky_dy =0
        else:
            pinky_dx = 0
            pinky_dy = -1
    else:
        pinky_afuera = True
    if pinky_afuera:
        target_f = 0
        target_c = 0
        
        if pinky_muerto:
            target_f = 11
            target_c = 13
        elif modo_fantasma == "chase":
            target_f = pacman_fila +(pacman_dy * 4)
            target_c = pacman_col + (pacman_dx * 4)
        elif modo_fantasma == "scatter":
            target_f = -2
            target_c = 2
        
        opcionesd_giro = []
        direcciones_posibles = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
        
        for dx, dy in direcciones_posibles:
            if dx == -pinky_dx and dy == -pinky_dy:
                continue
            test_f = pinky_fila + dy
            test_c = pinky_col + dx
            
            if 0 <= test_f < len(matriz_pacman) and 0 <= test_c <len(matriz_pacman[0]):
                casilla_evaluada = matriz_pacman[test_f][test_c]
                if casilla_evaluada != 1 and casilla_evaluada != 4:
                    opcionesd_giro.append((dx, dy))
                    
        if len(opcionesd_giro)> 0:
            f_recto = pinky_fila +pinky_dy
            c_recto =  pinky_col + pinky_dx
            choque = True
            if 0 <= f_recto < len(matriz_pacman) and 0<= c_recto < len(matriz_pacman[0]):
                if matriz_pacman[f_recto][c_recto] != 1:
                    choque = False
            if len(opcionesd_giro) > 1 or choque:
                if modo_fantasma == "frightened" and not pinky_muerto:
                    pinky_dx, pinky_dy = random.choice(opcionesd_giro)
                else: 
                    mejor_dx, mejor_dy = pinky_dx, pinky_dy
                    distancia_min = float('inf')
                    
                    for dx, dy in opcionesd_giro:
                        f_futuro = pinky_fila + dy
                        c_futuro = pinky_col +dx
                        
                        dist_cuadrado = (f_futuro -  target_f)**2 + (c_futuro - target_c)**2
                        if dist_cuadrado < distancia_min:
                            distancia_min = dist_cuadrado
                            mejor_dx = dx
                            mejor_dy =  dy
                    pinky_dx = mejor_dx
                    pinky_dy = mejor_dy
    
    ##MOVIMIENTO
    nueva_fila = pinky_fila +pinky_dy
    nueva_col = pinky_col + pinky_dx
    
    ancho_matriz = len(matriz_pacman[0])
    if nueva_col < 0: 
        nueva_col = ancho_matriz -1 
    elif nueva_col >= ancho_matriz:
        nueva_col = 0
    
    if 0 <= nueva_fila < len(matriz_pacman) and 0 <= nueva_col < len(matriz_pacman[0]):
        casilla_destino = matriz_pacman[nueva_fila][nueva_col]
        
        if casilla_destino != 1 and (casilla_destino != 4 or not pinky_afuera or pinky_muerto):
            pinky_fila = nueva_fila
            pinky_col = nueva_col
            
            x1 = pinky_col * size_celda
            y1 = (pinky_fila * size_celda) + margen_arriba
            x2 = x1 + size_celda
            y2 = y1 + size_celda
            
            mx1, my1, mx2, my2 = x1 + 2, y1 + 2, x2 - 2, y2 - 2
            puntos = [mx1, my2, mx1, my1 + 8, mx1 + 4, my1 + 2,
                      mx2 - 4, my1 + 2, mx2, my1 + 8, mx2, my2,
                      mx1 + ((mx2 - mx1) * 0.75),
                      my2 - 4, mx1 + ((mx2 - mx1) * 0.5),
                      my2, mx1 + ((mx2 - mx1) * 0.25),
                      my2 - 4
                      ]
            
            canvas.coords(pinky_id, puntos)
            canvas.coords(pinky_ojo_left_id, mx1 + 2, my1 + 4, mx1 + 7, my1 + 10)
            canvas.coords(pinky_ojo_right_id, mx2 - 7, my1 + 4, mx2 - 2, my1 + 10)
            canvas.coords(pinky_pupila_left_id, mx1 + 4, my1 + 6, mx1 + 6, my1 + 8)
            canvas.coords(pinky_pupula_right_id, mx2 - 6, my1 + 6, mx2 - 4, my1 + 8)
    
            
            pinky_ojoalegre()
    
    ghost_busters() 
    if pinky_muerto and pinky_fila == 11 and pinky_col == 13:
        pinky_fila = 14  # Entra al centro de la jaula
        pinky_col = 16
    elif pinky_muerto and pinky_fila == 14 and pinky_col == 16:
        pinky_muerto = False

        pinky_afuera = False  # Para que vuelva a ejecutar su salida forzada hacia arriba
        pinky_perrito = 15    # 3 segundos en el perrito (castigo)
        canvas.itemconfig(pinky_id, fill="#FFB8FF", outline="#FFB8FF")
        canvas.itemconfig(pinky_pupila_left_id, fill="blue", outline="blue")
        canvas.itemconfig(pinky_pupula_right_id, fill="blue", outline="blue")
    
    win()
    morido()
    canvas.update()
    
    velocidad_actual = 80 if pinky_muerto else 200
    ventana.after(velocidad_actual, mover_pinky)
            
def pinky_ojoalegre():
    
    x_base = pinky_col * size_celda
    y_base = (pinky_fila * size_celda) +margen_arriba   
    mx1, my1 = x_base + 2, y_base + 2
    
    centro_ojo_y = my1 + 7
    
    centro_ojo_left_x = mx1 + 4.5
    centro_ojo_right_x = mx1 + 13.5
    
    desfase_x_left = 0
    desfase_x_right = 0
    desfase_y = 0
    
    if pinky_dx == -1:
        desfase_x_left = -2
        desfase_x_right = -2
        desfase_y = 0
    elif pinky_dx == 1:
        desfase_x_left = 1.5
        desfase_x_right = 0.5
        desfase_y = 0
    elif pinky_dy == -1:
        desfase_x_left = -0.5
        desfase_x_right = -0.5
        desfase_y = -2
    elif pinky_dy == 1:
        desfase_x_left = -0.5
        desfase_x_right = -0.5
        desfase_y = 1.5       

    radio_pupila = 1.25

    cx_left = centro_ojo_left_x + desfase_x_left
    cx_right = centro_ojo_right_x + desfase_x_right
    cy = centro_ojo_y + desfase_y
        
    canvas.coords(pinky_pupila_left_id,
                  cx_left - radio_pupila,
                  cy - radio_pupila,
                  cx_left + radio_pupila,
                  cy + radio_pupila,
                  )
    canvas.coords(pinky_pupula_right_id,
                  cx_right - radio_pupila,
                  cy - radio_pupila,
                  cx_right + radio_pupila,
                  cy +radio_pupila)
    
    
def crear_inky():
    global inky_id, inky_ojo_left_id, inky_ojo_right_id, inky_pupila_left_id, inky_pupila_right_id
    
    x1, y1 = inky_col * size_celda, (inky_fila * size_celda) + margen_arriba
    x2, y2 = x1 + size_celda, y1 + size_celda
    mx1, my1, mx2, my2 = x1 + 2, y1 + 2, x2 - 2, y2 - 2
    p1_x = mx1 + ((mx2 - mx1) * 0.25)
    p2_x = mx1 + ((mx2 - mx1) * 0.5)
    p3_x = mx1 + ((mx2 - mx1) * 0.75)
    puntos = [mx1, my2, mx1, my1 + 8, 
            mx1 + 4, my1 + 2, mx2 - 4, my1 + 2, 
            mx2, my1 + 8, mx2, my2, 
            p3_x, my2 - 4, 
            p2_x, my2, 
            p1_x, my2 - 4]
    
    inky_id = canvas.create_polygon(puntos, fill= "#00FFFF", outline="#00FFFF")
    inky_ojo_left_id = canvas.create_oval(mx1 + 2, my1 + 4, mx1 + 7, my1 + 10, fill="white", outline="white")
    inky_ojo_right_id = canvas.create_oval(mx2 - 7, my1 + 4, mx2 - 2, my1 + 10, fill="white", outline="white")
    inky_pupila_left_id =canvas.create_oval(mx1 + 2, my1 + 6, mx1 + 5, my1 + 9, fill="blue", outline="blue")
    inky_pupila_right_id = canvas.create_oval(mx2 - 7, my1 + 6, mx2 - 4, my1 + 9, fill="blue", outline="blue")
    
    inky_ojoalegre()
    
def inky_ojoalegre():
    x_base, y_base = inky_col *size_celda, (inky_fila * size_celda) +margen_arriba
    mx1, my1 = x_base + 2, y_base +2
    centro_ojo_y = my1 + 7
    centro_ojo_left_x, centro_ojo_right_x = mx1 + 4.5, mx1 + 13.5
    df_x_l, df_x_r, df_y = 0,0,0
    if inky_dx == -1:
        df_x_l = -2; df_x_r = -2
    elif inky_dx == 1: df_x_l = 1.5; df_x_r = 0.5
    elif inky_dy == -1: df_x_l = -0.5; df_x_r = -0.5; df_y = -2
    elif inky_dy == 1: df_x_l = -0.5; df_x_r =-0.5; df_y = 1.5
    
    radio_pupila = 1.25
    cx_left = centro_ojo_left_x + df_x_l
    cx_right = centro_ojo_right_x + df_x_r
    cy = centro_ojo_y + df_y
    canvas.coords(inky_pupila_left_id,
                  cx_left - radio_pupila,
                  cy - radio_pupila,
                  cx_left + radio_pupila,
                  cy + radio_pupila)
    canvas.coords(inky_pupila_right_id, 
                  cx_right - radio_pupila, 
                  cy - radio_pupila,
                  cx_right + radio_pupila, 
                   cy + radio_pupila)
    
def mover_inky ():
    global inky_fila, inky_col, inky_dx, inky_dy
    global modo_fantasma, inky_afuera, inky_perrito, inky_muerto
    
    if not juego_activo: return
    
    if inky_perrito > 0:
        inky_perrito -= 1
        ventana.after(200, mover_inky)
        return
    if inky_fila >= 12 and not inky_afuera:
        if inky_col < 13:
            # Si está muy a la izquierda (col 12), camina horizontalmente a la DERECHA hacia el centro
            inky_dx = 1
            inky_dy = 0
        elif inky_col > 14:
            # Si se pasó a la derecha, camina a la IZQUIERDA hacia el centro
            inky_dx = -1
            inky_dy = 0
        else:
            # ¡Ya está perfectamente alineado con la puerta! Flota verticalmente hacia ARRIBA
            inky_dx = 0
            inky_dy = -1
    else:
        inky_afuera = True
    
    if inky_afuera:
        target_f, target_c = 0, 0
        
        if inky_muerto:
            target_f = 11
            target_c = 13
            
        elif modo_fantasma == "chase":
            pivot_f = pacman_fila + (pacman_dy *2)
            pivot_c = pacman_col + (pacman_dx * 2)
            target_f = pivot_f + (pivot_f - blinky_fila)
            target_c = pivot_c + (pivot_c - blinky_col)
        elif modo_fantasma == "scatter":
            target_f =  32; target_c = 27
        
        opciones = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if dx == -inky_dx and dy == -inky_dy: 
                continue
            tf, tc = inky_fila + dy, inky_col + dx
            if 0 <= tf < len(matriz_pacman) and 0 <= tc < len(matriz_pacman[0]):
                if matriz_pacman[tf][tc] != 1 and matriz_pacman[tf][tc] !=4:
                    opciones.append((dx, dy))
        if len(opciones)> 0:
            f_r, c_r = inky_fila + inky_dy, inky_col + inky_dx
            choque = True
            if 0 <= f_r < len(matriz_pacman) and 0 <= c_r < len(matriz_pacman[0]):
                if matriz_pacman[f_r][c_r] != 1:
                    choque = False
            if len(opciones) > 1 or choque:
                if modo_fantasma == "frightened" and not inky_muerto:
                    inky_dx, inky_dy = random.choice(opciones)
                else:
                    mejor_dx, mejor_dy = inky_dx, inky_dy
                    dist_min = float('inf')
                    for dx, dy in opciones:
                        ff, cc = inky_fila + dy, inky_col + dx
                        dist = (ff - target_f) ** 2+ (cc - target_c) ** 2
                        if dist < dist_min:
                            dist_min = dist
                            mejor_dx = dx
                            mejor_dy = dy
                    inky_dx, inky_dy = mejor_dx, mejor_dy
            
    #movimiento
    nf, nc = inky_fila + inky_dy, inky_col + inky_dx
    
    ancho_matriz = len(matriz_pacman[0])
    if nc < 0: 
        nc = ancho_matriz -1 
    elif nc >= ancho_matriz:
        nc = 0
        
    if 0<= nf < len(matriz_pacman) and 0 <= nc < len(matriz_pacman[0]):
        if matriz_pacman[nf][nc] != 1 and (matriz_pacman[nf][nc]!=4 or not inky_afuera):
            inky_fila, inky_col = nf, nc
            
            x1 = inky_col * size_celda
            y1 = (inky_fila * size_celda) + margen_arriba
            x2 = x1 + size_celda
            y2 = y1 + size_celda
            
            mx1, my1, mx2, my2 = x1 + 2, y1 + 2, x2 - 2, y2 - 2
            puntos = [mx1, my2, mx1, my1 + 8, mx1 + 4, my1 + 2,
                      mx2 - 4, my1 + 2, mx2, my1 + 8, mx2, my2,
                      mx1 + ((mx2 - mx1) * 0.75),
                      my2 - 4, mx1 + ((mx2 - mx1) * 0.5),
                      my2, mx1 + ((mx2 - mx1) * 0.25),
                      my2 - 4
                      ]
            canvas.coords(inky_id, puntos)
            canvas.coords(inky_ojo_left_id, mx1 + 2, my1 + 4, mx1 + 7, my1 + 10)
            canvas.coords(inky_ojo_right_id, mx2 - 7, my1 + 4, mx2 - 2, my1 + 10)
            canvas.coords(inky_pupila_left_id, mx1 + 4, my1 + 6, mx1 + 6, my1 + 8)
            canvas.coords(inky_pupila_right_id, mx2 - 6, my1 + 6, mx2 - 4, my1 + 8)
            inky_ojoalegre()
    
    ghost_busters()        
    if inky_muerto and inky_fila == 11 and inky_col == 13:
        inky_fila = 14
        inky_col = 12
    elif inky_muerto and inky_fila == 14 and inky_col == 12:
        inky_muerto = False
        inky_afuera = False
        inky_perrito = 10
        canvas.itemconfig(inky_id, fill="#00FFFF", outline="#00FFFF")
        canvas.itemconfig(inky_pupila_left_id, fill="blue", outline="blue")
        canvas.itemconfig(inky_pupila_right_id, fill="blue", outline="blue")
    
    win()   
    morido()
    canvas.update()
    
    velocidad_actual = 80 if inky_muerto else 200
    ventana.after(velocidad_actual, mover_inky)
    

def crear_clyde ():
    global clyde_id, clyde_ojo_left_id, clyde_ojo_right_id, clyde_pupila_left_id, clyde_pupula_right_id
    x1, y1 = clyde_col * size_celda, (clyde_fila * size_celda) + margen_arriba
    x2, y2 = x1 + size_celda, y1 + size_celda
    mx1, my1, mx2, my2 = x1 + 2, y1 + 2, x2 - 2, y2 - 2
    p1_x = mx1 + ((mx2 - mx1) * 0.25); p2_x = mx1 + ((mx2 - mx1) * 0.5); p3_x = mx1 + ((mx2 - mx1) * 0.75)
    puntos = [mx1, my2, mx1, my1 + 8, mx1 + 4, my1 + 2, mx2 - 4, my1 + 2, mx2, my1 + 8, mx2, my2, p3_x, my2 - 4, p2_x, my2, p1_x, my2 - 4]
    
    clyde_id = canvas.create_polygon(puntos, fill="#FFB852", outline="#FFB852")
    clyde_ojo_left_id = canvas.create_oval(mx1 + 2, my1 + 4, mx1 + 7, my1 + 10, fill="white", outline="white")
    clyde_ojo_right_id = canvas.create_oval(mx2 - 7, my1 + 4, mx2 - 2, my1 + 10, fill="white", outline="white")
    clyde_pupila_left_id = canvas.create_oval(mx1 + 2, my1 + 6, mx1 + 5, my1 + 9, fill="blue", outline="blue")
    clyde_pupula_right_id = canvas.create_oval(mx2 - 7, my1 + 6, mx2 - 4, my1 + 9, fill="blue", outline="blue")
    
    clyde_ojoalegre()

def mover_clyde():
    global clyde_fila, clyde_col, clyde_dx, clyde_dy, modo_fantasma 
    global clyde_afuera, clyde_perrito, clyde_muerto
    
    if not juego_activo: return
    
    if clyde_perrito > 0:
        clyde_perrito -= 1
        ventana.after(200, mover_clyde)
        return
    
    if clyde_fila >= 12 and not clyde_afuera:
        if clyde_col > 14:
            # Si está muy a la derecha (col 15), camina horizontalmente a la IZQUIERDA hacia el centro
            clyde_dx = -1
            clyde_dy = 0
        elif clyde_col < 13:
            # Si se pasó a la izquierda, camina a la DERECHA hacia el centro
            clyde_dx = 1
            clyde_dy = 0
        else:
            # ¡Ya está perfectamente alineado con la puerta! Flota verticalmente hacia ARRIBA
            clyde_dx = 0
            clyde_dy = -1
    else:
        clyde_afuera = True
        
    if clyde_afuera:    
        target_f, target_c = 0, 0
        dist_a_pacman = (clyde_fila - pacman_fila) ** 2 + (clyde_col - pacman_col) ** 2
        
        if clyde_muerto:
            target_c = 13
            target_f = 11
        elif modo_fantasma == "chase":
            if dist_a_pacman >  64:
                target_f = pacman_fila; target_c = pacman_col
            
            else: 
                target_f = 32; target_c = 0
        
        elif modo_fantasma == "scatter":
            target_f = 32; target_c = 0
            
        opciones = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if dx == -clyde_dx and dy == -clyde_dy:
                continue
            tf, tc = clyde_fila + dy, clyde_col + dx
            if 0 <= tf < len(matriz_pacman) and 0<= tc < len(matriz_pacman[0]):
                if matriz_pacman[tf][tc] != 1 and matriz_pacman[tf][tc] != 4:
                    opciones.append((dx, dy))
                    
        if len(opciones)> 0:
            f_r, c_r = clyde_fila + clyde_dy, clyde_col + clyde_dx
            choque =  True
            if 0 <= f_r < len(matriz_pacman) and 0 <= c_r < len(matriz_pacman[0]):
                if matriz_pacman[f_r][c_r] != 1:
                    choque = False
            if len(opciones) > 1 or choque:
                if modo_fantasma == "frightened" and not clyde_muerto:
                    clyde_dx, clyde_dy = random.choice(opciones)
                else:
                    mejor_dx, mejor_dy = clyde_dx, clyde_dy; dist_min = float('inf')
                    for dx, dy in opciones:
                        ff, cc = clyde_fila + dy, clyde_col + dx
                        dist = (ff - target_f) ** 2 + (cc - target_c) ** 2
                        if dist < dist_min:
                            dist_min = dist
                            mejor_dx = dx
                            mejor_dy = dy
                    clyde_dx, clyde_dy = mejor_dx, mejor_dy
                    
    #movimiento 
    nf, nc= clyde_fila+ clyde_dy, clyde_col + clyde_dx
    
    ancho_matriz = len(matriz_pacman[0])
    if nc < 0: 
        nc = ancho_matriz -1 
    elif nc >= ancho_matriz:
        nc = 0
        
    if 0 <= nf < len(matriz_pacman) and 0 <= nc < len(matriz_pacman[0]):
        if matriz_pacman[nf][nc] != 1 and (matriz_pacman[nf][nc] != 4 or not clyde_afuera):
            clyde_fila, clyde_col = nf, nc
            
            x1 = clyde_col * size_celda
            y1 = (clyde_fila * size_celda) + margen_arriba
            x2 = x1 + size_celda
            y2 = y1 + size_celda
            
            mx1, my1 = x1 + 2, y1 + 2
            mx2, my2 = x2 - 2, y2 - 2
            ancho_util = mx2 - mx1
            p1_x = mx1 + (ancho_util * 0.25)
            p2_x = mx1 + (ancho_util * 0.5)
            p3_x = mx1 + (ancho_util * 0.75)
            alto_picos_y = my2 - 4
            
            puntos_actualizados = [
                mx1, my2, mx1, my1 + 8, mx1 + 4, my1 + 2, mx2 - 4, my1 + 2,
                mx2, my1 + 8, mx2, my2, p3_x, alto_picos_y, p2_x, my2, p1_x, alto_picos_y
            ]
            canvas.coords(clyde_id, puntos_actualizados)
            canvas.coords(clyde_ojo_left_id, mx1 + 2, my1 + 4, mx1 + 7, my1 + 10)
            canvas.coords(clyde_ojo_right_id, mx2 - 7, my1 + 4, mx2 - 2, my1 + 10)
            canvas.coords(clyde_pupila_left_id, mx1 + 4, my1 + 6, mx1 + 6, my1 + 8)
            canvas.coords(clyde_pupula_right_id, mx2 - 6, my1 + 6, mx2 - 4, my1 + 8)
            
            clyde_ojoalegre()
    
    ghost_busters()
    if clyde_muerto and clyde_fila == 11 and clyde_col == 13:
        clyde_fila = 14
        clyde_col = 15
    elif clyde_muerto and clyde_fila == 14 and clyde_col == 15:
        clyde_muerto = False
        clyde_afuera = False
        clyde_perrito = 15
        canvas.itemconfig(clyde_id, fill="#FFB852", outline="#FFB852")
        canvas.itemconfig(clyde_pupila_left_id, fill="blue", outline="blue")
        canvas.itemconfig(clyde_pupula_right_id, fill="blue", outline="blue")
    
    win()   
    morido()
    canvas.update()
    
    velocidad_actual = 80 if clyde_muerto else 200
    ventana.after(velocidad_actual, mover_clyde)        
            

def clyde_ojoalegre():
    x_base, y_base = clyde_col * size_celda, (clyde_fila * size_celda) + margen_arriba   
    mx1, my1 = x_base + 2, y_base + 2
    centro_ojo_y = my1 + 7
    centro_ojo_left_x, centro_ojo_right_x = mx1 + 4.5, mx1 + 13.5
    df_x_l, df_x_r, df_y = 0, 0, 0
    
    if clyde_dx == -1: df_x_l = -2; df_x_r = -2
    elif clyde_dx == 1: df_x_l = 1.5; df_x_r = 0.5
    elif clyde_dy == -1: df_x_l = -0.5; df_x_r = -0.5; df_y = -2
    elif clyde_dy == 1: df_x_l = -0.5; df_x_r = -0.5; df_y = 1.5       
    
    radio_pupila = 1.25
    
    canvas.coords(clyde_pupila_left_id, centro_ojo_left_x + df_x_l - radio_pupila,
                  centro_ojo_y + df_y - radio_pupila,
                  centro_ojo_left_x + df_x_l + radio_pupila,
                  centro_ojo_y + df_y + radio_pupila)
    canvas.coords(clyde_pupula_right_id, centro_ojo_right_x + df_x_r - radio_pupila,
                  centro_ojo_y + df_y - radio_pupila,
                  centro_ojo_right_x + df_x_r + radio_pupila,
                  centro_ojo_y + df_y + radio_pupila)
##FUNCIN PARA EMPEZAR EL JUEGO
def motor_pacman ():
    mapa_pacman()
    crear_pacman()
    crear_score()
    crear_blinky()
    crear_pinky()
    crear_inky()
    crear_clyde()
    crear_vida()
    
    ventana.bind("<KeyPress>", teclado_pacman)
    
    reloj_modo_ia()
    mover_pacman()
    viva_bazuco()
    mover_blinky()
    mover_pinky()
    mover_inky()
    mover_clyde()

motor_pacman()


ventana.mainloop()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⠋⠙⠋⠉⠙⢷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶⣶⣄⠀⠀⠀⢠⣾⣿⣁⡀⠀⠀⠀⠀⠀⠀⢑⣿⡆⠀⠀⠀⢠⣾⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣾⣦⡀⢠⣾⡿⣛⣛⡻⢷⣄⠀⠀⣴⣾⣿⠛⠻⠦⣄⣴⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠻⢿⣿⣿⣿⣿⣿⢿⣿⣿⣧⢼⣿⣿⣿⠿⣿⣇⢸⡟⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠿⢿⣾⣿⣤⠿⠋⠀⠈⠻⢿⣿⣧⣿⠟⣬⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠃⠀⠀⢀⣴⣖⣶⠀⠀⠀⠀⠀⢀⡈⠀⠀⢘⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣶⣶⣶⠿⠿⠿⠿⠷⠶⠶⠶⠛⠋⠻⣦⣤⣀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⣿⠻⢷⣤⣀⠀⠀⠀⠈⠀⠀⠀⣀⣈⡻⢿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⡿⠛⡏⠁⠂⠘⠭⢿⣒⣒⡒⠒⠒⠊⠉⠁⠀⠀⣿⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠟⠁⡄⠣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡌⠙⠲⣤⣀⠠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣏⠀⠀⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠋⠀⠀⠀⠀⠈⠙⠚⠓⠶⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣶⣀⡴⠛⢷⣄⣠⣄⡀⠀⠀⠀⠀⠀⠀⠀⠐⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠳⢦⡀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⠴⠾⣿⣿⣿⣿⣿⠟⠛⠿⣿⣦⣄⠙⢻⣿⣷⣦⡤⠤⠶⠒⠛⠁⣠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⡾⠏⠁⠀⠀⠀⠀⠰⠿⠟⠋⠀⠀⠀⠀⠈⠉⠛⠙⠋⠉⠉⠀⠀⠀⠀⠀⣀⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⡀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠒⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⢀⣾⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀
# ⠀⠀⠀⠀⢄⣾⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢸⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣧⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀
# ⠀⠀⠀⠀⣼⣋⣧⣶⠀⠀⠀⢀⡀⣀⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⣼⣿⣿⣟⣤⡀⠀⠀⠀⠀⠀⠀⠘⣦⠀⠀
# ⠀⠀⠀⠀⣿⡟⡇⣿⣤⣤⣴⣼⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⣷⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠏⣴⣿⣿⠋⠉⠉⠛⠋⡄⠂⠀⠀⠀⠀⠈⣇⠀
# ⠀⠀⠀⢀⣿⣷⣜⢿⣿⣿⣿⣿⣿⣿⣟⢿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⠾⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠐⠖⣠⣶⣿⣟⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀
# ⠀⠀⢀⣾⠋⠻⣿⡶⠍⠙⠛⢿⣿⣿⣿⣮⡙⠿⣿⣶⣤⣄⣀⣤⣤⣤⣤⡀⢀⣈⣁⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
# ⠀⠀⣾⠇⠀⠀⠘⢷⡇⠀⠀⠀⢿⣿⣿⣿⣿⣶⣼⣿⣿⣟⣻⣿⣿⣿⣿⡿⠟⠛⠁⠀⠉⠻⢿⣿⣶⣤⣴⣶⣶⣤⣶⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠇
# ⠀⢸⣿⠀⠀⠀⢠⡞⠀⠀⠀⠀⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣋⣠⣀⠀⠀⠀⠀⠀⠀⠀⢉⣛⢻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀
# ⠀⢸⡏⠀⠀⠀⣼⠁⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠿⡿⠛⠉⠉⠉⠁⠀⢀⠀⠀⠀⠀⠀⠉⠰⠿⠿⠛⠻⠟⠉⠁⢩⢹⣿⣿⣄⠀⠸⣆⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀
# ⠀⣿⢿⠀⠀⣰⠇⠀⠀⠀⠀⠀⣿⡟⢻⣿⣿⣿⣿⣿⡟⠻⢶⣤⠀⠀⠀⠀⠀⠀⠀⢸⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⢿⣿⣿⣦⠀⢹⣆⠀⠀⠀⠀⠀⠀⠀⡇⠀
# ⢀⡟⠺⠀⢐⡿⠀⠀⠀⠀⢀⣼⣿⠁⠀⢻⣿⣿⣿⣿⣿⣷⣤⣿⣤⣤⣤⣤⣶⡄⠀⠀⣿⣇⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠈⢿⣷⣿⡾⠁⢿⣿⣷⣿⣿⡷⠀⠀⠀⠀⠀⠀⡇⠀
# ⢸⡇⠀⠘⣿⡁⠀⠀⢀⣰⣿⣿⠃⠀⠀⠀⢻⣿⣽⠋⠛⢯⢿⣿⠛⠛⠋⠉⠙⠛⠲⣄⠉⠉⠁⠈⠉⠙⠛⠷⣦⣤⣤⣌⠀⠀⢸⡟⠁⠀⠀⠻⣿⣿⣿⣍⠀⠀⠀⠀⠀⠀⢧⠀
# ⢸⠁⠀⠀⢹⣷⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⢸⣿⢢⠀⠂⠀⣭⣿⡀⠀⠀⠀⠀⠀⠀⢸⡉⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⡿⠀⠀⠀⠀⠀⢹⣿⡿⠉⠀⠀⠀⠀⠀⠀⡾⠀
# ⠀⠀⠀⠀⠀⠋⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⣼⣏⠈⠁⢰⠀⢨⣿⣧⣀⡀⣠⠀⠀⠀⣸⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⠀⠀⠀⠀⠀⣸⡍⠁⠀⠀⠀⠀⠀⠀⣠⣷⠀
# ⠀⠀⠀⠀⠀⠀⠙⢿⣿⡇⠀⠀⠀⠀⠀⢠⣿⠟⠇⠀⠈⠑⢦⣿⠿⠿⠿⠿⠶⢀⢀⣸⠿⣶⣦⣠⡖⠀⠀⠀⠀⠀⠀⠀⢀⣿⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠘⢻⡆
# ⠀⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀⠀⣸⡗⠀⠀⠀⠀⠀⠀⠙⠷⡄⣀⠀⠀⠻⠟⠃⠀⠀⠀⠀⠤⠀⠀⠀⠀⠀⠀⠀⣾⡟⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
# ⠀⠀⠀⠀⠀⠀⠀⠀⠹⠇⠀⠀⠀⠀⠀⣸⣿⠠⢰⣶⠄⠀⠀⠀⢀⣀⠀⢠⠀⠀⢠⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣙⣿⠁⠀⠀⠀⠀⠀⣸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠇