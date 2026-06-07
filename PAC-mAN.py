"""PAC-MAN"""

import tkinter as tk
import turtle as tr

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

pacman_fila = 23
pacman_col =13
pacman_id = None
score_texto_id = None

#///marcador///
margen_arriba = 60


ancho_canvas = len(matriz_pacman[0]) *size_celda
alto_canvas = (len(matriz_pacman) * size_celda) + margen_arriba

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

def mapa_pacman():

    for fila in range(len(matriz_pacman)):
        for col in range(len(matriz_pacman[fila])):
            
            x1 = col * size_celda
            y1 = (fila * size_celda) +margen_arriba
            x2 = x1 + size_celda
            y2 = y1 + size_celda
            
            tipo = matriz_pacman[fila][col]
            
            if tipo in [0, 2, 3, 4]:
                canvas.create_rectangle(x1, y1, x2, y2, fill="black", outline="")
        
            cx = x1 + (size_celda // 2)
            cy = y1 + (size_celda // 2)
            
            if tipo == 1:
                grosor_borde = 2
                canvas.create_rectangle(
                    x1 + grosor_borde, 
                    y1 + grosor_borde, 
                    x2 - grosor_borde, 
                    y2 - grosor_borde, 
                    fill="black", 
                    outline=""
                )
            
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
        extent=300
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
    global pacman_col, pacman_fila, pacman_dy, pacman_dx
    global pacman_deseo_dy, pacman_deseo_dx
    
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
            
            #HAce-- wakawaka--//
            wakawaka()
            pacman_fila = nueva_fila
            pacman_col = nueva_col
            
            angulo_boca = 30
        
            if pacman_dx == -1:
                angulo_boca = 210
            elif pacman_dy ==  -1:
                angulo_boca =120
            elif pacman_dy == 1:
                angulo_boca =300
                
            canvas.itemconfig(pacman_id, start=angulo_boca, extent= 300)
        
            x1 = pacman_col * size_celda
            y1 =  (pacman_fila * size_celda) + margen_arriba
            x2 = x1 + size_celda
            y2 = y1 + size_celda
            
            canvas.coords(pacman_id, x1 + 2, y1 + 2, x2 - 2, y2 - 2)
            
    ventana.after(150, mover_pacman)
        

def wakawaka ():
    global puntuacion
    casilla_actual = matriz_pacman[pacman_fila][pacman_col]
    
    if casilla_actual == 2 or casilla_actual == 3:
        
        if casilla_actual == 2:
            puntuacion += 10
        else:
            puntuacion+= 50
        
        coordenada = (pacman_fila, pacman_col)
        if coordenada in mapa_ids_bolitas:
            id_amarillo = mapa_ids_bolitas[coordenada]
            
            canvas.delete(id_amarillo)
            
            del mapa_ids_bolitas[coordenada]
            
    matriz_pacman[pacman_fila][pacman_col] = 0
    
    canvas.itemconfig(score_texto_id, text=f"{puntuacion:02d}")

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
        ancho= "n"
    )
    
mapa_pacman()
crear_pacman()
crear_score()

ventana.bind("<KeyPress>", teclado_pacman)

mover_pacman()


ventana.mainloop()
