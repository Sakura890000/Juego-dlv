import turtle as tr
import random as rd
import os

# --- CONFIGURACIÓN DE LA PANTALLA ---
pantalla = tr.Screen()
pantalla.title("Tits Classic")
pantalla.bgcolor("#111116")
pantalla.setup(width=500, height=650)
pantalla.tracer(0)  # Apaga animaciones automáticas para evitar parpadeos

# --- REGISTRAR ASSETS ---
beacon = "assets/beacon.gif"
box = "assets/deepslate.gif"
soul = "assets/soul.gif"
luck = "assets/bricks.gif"
sculk= "assets/sculk.gif"

for asset in [beacon, box, soul, luck]:
    if os.path.exists(asset):
        pantalla.register_shape(asset)

# --- VARIABLES GLOBALES ---
TAMANO_CUADRADO = 32
COLUMNAS = 10
FILAS = 20

# Dimensiones del tablero en píxeles
ANCHO_TABLERO = COLUMNAS * TAMANO_CUADRADO
ALTO_TABLERO = FILAS * TAMANO_CUADRADO
ORIGEN_X = -ANCHO_TABLERO // 2
ORIGEN_Y = -ALTO_TABLERO // 2

# Matriz del tablero (0 significa vacío)
tablero = [[0 for _ in range(COLUMNAS)] for _ in range(FILAS)]

puntuacion = 0
puntuacionNec = 500
juego_terminado = False

# --- DEFINICIÓN DE PIEZAS (Tetrominós) ---
# Representan las coordenadas de cada bloque
# Cada pieza ahora asocia sus bloques con un asset específico
PIEZAS = {
    'I': [[(0,0), (1,0), (2,0), (3,0)], beacon], # Beacon
    'O': [[(0,0), (1,0), (0,1), (1,1)], box], # Box
    'T': [[(1,0), (0,1), (1,1), (2,1)], soul], # Soul
    'S': [[(1,0), (2,0), (0,1), (1,1)], luck], # Luck
    'Z': [[(0,0), (1,0), (1,1), (2,1)], beacon], # Beacon
    'J': [[(0,0), (0,1), (1,1), (2,1)], sculk], # Box
    'L': [[(2,0), (0,1), (1,1), (2,1)], soul]  # Soul
}

# --- TUTUGAS AUXILIARES ---
pintor = tr.Turtle()  # Dibuja los bloquesde juego
pintor.hideturtle()
pintor.speed(0)
pintor.penup()

marcador = tr.Turtle() 
marcador.hideturtle()
marcador.color("white")
marcador.penup()

#dibujar el borde
borde_pintor = tr.Turtle()
borde_pintor.hideturtle()
borde_pintor.penup()

# --- FUNCIONES DE DIBUJO ---
def dibujar_cuadrado(x, y, asset):
    """Dibuja un bloque de Tetris usando una imagen (asset)"""
    px = ORIGEN_X + (x * TAMANO_CUADRADO) + (TAMANO_CUADRADO // 2)
    py = ORIGEN_Y + (y * TAMANO_CUADRADO) + (TAMANO_CUADRADO // 2)
    pintor.goto(px, py)
    if os.path.exists(asset):
        pintor.shape(asset)
        pintor.stamp()
    else:
        # Fallback
        pintor.pendown()
        pintor.color("gray")
        for _ in range(4):
            pintor.forward(TAMANO_CUADRADO - 1)
            pintor.left(90)
        pintor.penup()

def actualizar_pantalla():
    """Redibuja todo el escenario: bordes, bloques fijos y pieza actual"""
    pintor.clearstamps()
    
    # límites del tablero
    borde_pintor.clearstamps()
    borde_pintor.penup()
    borde_pintor.color("#33333d")
    borde_pintor.pensize(3)
    borde_pintor.goto(ORIGEN_X - 2, ORIGEN_Y - 2)
    borde_pintor.pendown()
    for _ in range(2):
        borde_pintor.forward(ANCHO_TABLERO + 4)
        borde_pintor.left(90)
        borde_pintor.forward(ALTO_TABLERO + 4)
        borde_pintor.left(90)
    borde_pintor.pensize(1)
    borde_pintor.penup()

    # Dibujar bloques ya consolidados
    for r in range(FILAS):
        for c in range(COLUMNAS):
            if tablero[r][c] != 0:
                dibujar_cuadrado(c, r, tablero[r][c])

    # Dibujar la pieza que está cayendo
    if not juego_terminado:
        for bloque in pieza_actual:
            bx = px_actual + bloque[0]
            by = py_actual + bloque[1]
            if by < FILAS:
                dibujar_cuadrado(bx, by, asset_actual)

    pantalla.update()


def mostrar_instrucciones_tetris():
    instr = tr.Turtle()
    instr.hideturtle()
    instr.penup()
    instr.color("white")
    try:
        y = ALTO_TABLERO // 2 - 20
    except Exception:
        y = 260
    instr.goto(0, y)
    instr.write("Tetris: Izq/Dcha mover, Abajo bajar, Arriba rotar. Completa líneas.", align="center", font=("Arial", 12, "bold"))
    pantalla.update()
    pantalla.ontimer(instr.clear, 8000)

def actualizar_marcador():
    """Actualiza los puntos en la parte superior"""
    marcador.clear()
    marcador.goto(0, ALTO_TABLERO // 2 + 10)
    marcador.write(f"PUNTOS: {puntuacion}", align="center", font=("Arial", 16, "bold"))
    if juego_terminado:
        marcador.goto(0, 0)
        if puntuacion >= puntuacionNec:
            marcador.write("GANASTE", align="center", font=("Arial", 30, "bold"))
            print("GANO")
        else:
            marcador.write("PERDISTE POR PUTO", align="center", font=("Arial", 30, "bold"))
            print("PERDIO")

        
        

# --- LÓGICA DE JUEGO ---
def nueva_pieza():
    """Genera un nuevo tetrominó al azar arriba del tablero"""
    global pieza_actual, asset_actual, px_actual, py_actual, juego_terminado
    tipo = rd.choice(list(PIEZAS.keys()))
    pieza_actual = [list(b) for b in PIEZAS[tipo][0]]
    asset_actual = PIEZAS[tipo][1]
    
    px_actual = COLUMNAS // 2 - 2
    py_actual = FILAS - 2

    if colisiona(pieza_actual, px_actual, py_actual):
        juego_terminado = True
        actualizar_marcador()

def colisiona(pieza, px, py):
    """Detecta si la pieza choca contra los bordes o bloques existentes"""
    for bloque in pieza:
        bx = px + bloque[0]
        by = py + bloque[1]
        if bx < 0 or bx >= COLUMNAS or by < 0:
            return True
        if by < FILAS and tablero[by][bx] != 0:
            return True
    return False

def fijar_pieza():
    """Fija la pieza actual en la matriz cuando ya no puede bajar más"""
    global puntuacion
    for bloque in pieza_actual:
        bx = px_actual + bloque[0]
        by = py_actual + bloque[1]
        if by < FILAS:
            tablero[by][bx] = asset_actual

    # Limpiar
    lineas_eliminadas = 0
    for r in range(FILAS - 1, -1, -1):
        if 0 not in tablero[r]: # Si la fila no contiene ningún cero, está llena
            del tablero[r]
            tablero.append([0 for _ in range(COLUMNAS)]) # Inserta fila vacía arriba
            lineas_eliminadas += 1

    if lineas_eliminadas > 0:
        puntuacion += (lineas_eliminadas * 100)
        actualizar_marcador()

    nueva_pieza()

# --- CONTROLES DE MOVIMIENTO ---
def mover_izquierda():
    global px_actual
    if not juego_terminado and not colisiona(pieza_actual, px_actual - 1, py_actual):
        px_actual -= 1
        actualizar_pantalla()

def mover_derecha():
    global px_actual
    if not juego_terminado and not colisiona(pieza_actual, px_actual + 1, py_actual):
        px_actual += 1
        actualizar_pantalla()

def bajar_pieza():
    global py_actual
    if juego_terminado:
        return
    if not colisiona(pieza_actual, px_actual, py_actual - 1):
        py_actual -= 1
    else:
        fijar_pieza()
    actualizar_pantalla()

def rotar_pieza():
    """Rota la pieza 90 grados usando álgebra de coordenadas (X, Y) -> (-Y, X)"""
    global pieza_actual
    if juego_terminado:
        return
    
    # Calcular centro de rotación aproximado de la pieza
    nueva_pieza_rotada = []
    for b in pieza_actual:
        nueva_pieza_rotada.append([-b[1], b[0]])

    # Ajustar para que no rote fuera de rango
    if not colisiona(nueva_pieza_rotada, px_actual, py_actual):
        pieza_actual = nueva_pieza_rotada
        actualizar_pantalla()

# --- BUCLE DE CAÍDA AUTOMÁTICA ---
def caer_automatico():
    """Provoca la caída constante de la pieza cada medio segundo"""
    if not juego_terminado:
        bajar_pieza()
        pantalla.listen()
        pantalla.ontimer(caer_automatico, 500) # 500 milisegundos = 0.5 segundos

# --- CONFIGURACIÓN DE TECLADO ---
pantalla.listen()
pantalla.onkeypress(mover_izquierda, "Left")
pantalla.onkeypress(mover_derecha, "Right")
pantalla.onkeypress(bajar_pieza, "Down")
pantalla.onkeypress(rotar_pieza, "Up")

# --- INICIALIZACIÓN ---
nueva_pieza()
mostrar_instrucciones_tetris()
actualizar_marcador()
actualizar_pantalla()
caer_automatico()

pantalla.mainloop()
