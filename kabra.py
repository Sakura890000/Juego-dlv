from PIL import Image,ImageTk
import turtle as tr
import random as rd

# crear pantalla
pantalla = tr.Screen()
perro = "perro.gif"
girar = "girar.gif"
pantalla.register_shape(girar)
pantalla.register_shape(perro)
pantalla.title("Tablero")
pantalla.bgcolor("#90e79c")
pantalla.setup(width=900, height=700)

# variables
TableroSizeX = 10
TableroSizeY = 10
casillaSize = 45

# Calcular límites exactos
inicioX = -(TableroSizeX * casillaSize) // 2
finX = (TableroSizeX * casillaSize) // 2
inicioY = -(TableroSizeY * casillaSize) // 2
finY = (TableroSizeY * casillaSize) // 2

# dibujador de cuadrícula
dibujante = tr.Turtle()
dibujante.hideturtle()
dibujante.speed(0)
dibujante.color("black")

# Líneas verticales (se suma +1 a finX para que range incluya la última línea)
for x in range(inicioX, finX + 1, casillaSize):
    dibujante.penup()
    dibujante.goto(x, inicioY)
    dibujante.pendown()
    dibujante.goto(x, finY)  # Conecta exactamente con el tope superior

# Líneas horizontales (se suma +1 a finY para que range incluya la última línea)
for y in range(inicioY, finY + 1, casillaSize):
    dibujante.penup()
    dibujante.goto(inicioX, y)
    dibujante.pendown()
    dibujante.goto(finX, y)  # Conecta exactamente con el tope derecho

# Tortuga para pintar
pintor = tr.Turtle()
pintor.hideturtle()
pintor.speed(0)
pintor.color("black", "#1d4ed8")  # Relleno azul

def registrar_clic(x, y):
    # Verificar límites del tablero
    if inicioX <= x <= finX and inicioY <= y <= finY:
        # Calcular esquina inferior izquierda de la casilla
        casilla_x = ((x - inicioX) // casillaSize) * casillaSize + inicioX
        casilla_y = ((y - inicioY) // casillaSize) * casillaSize + inicioY
        
        # Dibujar relleno azul
        pintor.penup()
        pintor.goto(casilla_x, casilla_y)
        pintor.pendown()
        pintor.begin_fill()
        for _ in range(4):
            pintor.forward(casillaSize)
            pintor.left(90)
        pintor.end_fill()

# Activar detección de clics
pantalla.onclick(registrar_clic)

# players config
jugador1 = tr.Turtle()
jugador1.shape(girar)
jugador1.color("red")
jugador1.penup()
jugador1.speed(3)

jugador2 = tr.Turtle()
jugador2.shape(perro)
jugador2.color("yellow")
jugador2.penup()
jugador2.speed(3)

# Diccionario para controlar las coordenadas lógicas (columna, fila) de cada jugador
# Empiezan en la casilla inferior izquierda (0, 0)
posiciones = {
    "J1": {"x": 0, "y": 0, "turtle": jugador1},
    "J2": {"x": 0, "y": 0, "turtle": jugador2}
}

turno_actual = "J1"  # Control de turnos



# Funciones para simular dados (ejemplo rápido presionando teclas)
def lanzar_dado():
    pasos = rd.randint(1, 6)
    print(f"Turno de {turno_actual}: Sacó un {pasos}")
    mover_jugador(pasos)

# 1. Configuración de casillas trampa (Se mantiene igual)
CANTIDAD_TRAMPAS = 15
casillas_trampa = set()

pintor_trampas = tr.Turtle()
pintor_trampas.hideturtle()
pintor_trampas.speed(0)
pintor_trampas.color("black", "#ef4444")  # Color rojo

while len(casillas_trampa) < CANTIDAD_TRAMPAS:
    tx = rd.randint(0, TableroSizeX - 1)
    ty = rd.randint(0, TableroSizeY - 1)
    
    if (tx, ty) != (0, 0):  # Evita poner trampa en la salida
        casillas_trampa.add((tx, ty))
        
        px = inicioX + (tx * casillaSize)
        py = inicioY + (ty * casillaSize)
        
        pintor_trampas.penup()
        pintor_trampas.goto(px, py)
        pintor_trampas.pendown()
        pintor_trampas.begin_fill()
        for _ in range(4):
            pintor_trampas.forward(casillaSize)
            pintor_trampas.left(90)
        pintor_trampas.end_fill()


# 2. Función de movimiento modificada para regresar al principio (0,0)
def mover_jugador(pasos):
    global turno_actual
    jugador = posiciones[turno_actual]
    
    # Calcular nueva posición lineal
    posicion_lineal_actual = jugador["y"] * TableroSizeX + jugador["x"]
    nueva_posicion_lineal = posicion_lineal_actual + pasos
    
    # Controlar límites del tablero
    max_casillas = TableroSizeX * TableroSizeY
    if nueva_posicion_lineal >= max_casillas:
        nueva_posicion_lineal = max_casillas - 1
    if nueva_posicion_lineal < 0:
        nueva_posicion_lineal = 0
        
    # Convertir a coordenadas (x, y)
    jugador["x"] = nueva_posicion_lineal % TableroSizeX
    jugador["y"] = nueva_posicion_lineal // TableroSizeX

    # ---- DETECCIÓN DE TRAMPAS: REGRESA AL PRINCIPIO ----
    if (jugador["x"], jugador["y"]) in casillas_trampa:
        print(f"¡¡MALA SUERTE!! {turno_actual} cayó en una trampa. Regresa al inicio.")
        jugador["x"] = 0
        jugador["y"] = 0
    # ----------------------------------------------------

    # Calcular coordenadas en pixeles (centrado en la casilla)
    pixel_x = inicioX + (jugador["x"] * casillaSize) + (casillaSize // 2)
    pixel_y = inicioY + (jugador["y"] * casillaSize) + (casillaSize // 2)
    
    # Mover físicamente la tortuga
    jugador["turtle"].goto(pixel_x, pixel_y)
    
    # Cambiar el turno al siguiente jugador
    turno_actual = "J2" if turno_actual == "J1" else "J1"


# Configurar el teclado para jugar
pantalla.listen()
pantalla.onkey(lanzar_dado, "space")  # Presiona ESPACIO para avanzar

# Colocar jugadores en la salida al iniciar el juego
mover_jugador(0)
mover_jugador(0)


pantalla.mainloop()
