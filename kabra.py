from PIL import Image, ImageTk
import turtle as tr
import random as rd

# Sprites
perro = "perro.gif"
girar = "girar.gif"
grass = "grass.gif"

# crear pantalla
pantalla = tr.Screen()

# Registrar sprites
pantalla.register_shape(girar)
pantalla.register_shape(perro)
pantalla.register_shape(grass)

# organizar pantalla
pantalla.title("Tablero")
pantalla.bgcolor("#90e79c")
pantalla.setup(width=900, height=700)

# variables
TableroSizeX = 10
TableroSizeY = 10
casillaSize = 64

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

# Líneas verticales
for x in range(inicioX, finX + 1, casillaSize):
    dibujante.penup()
    dibujante.goto(x, inicioY)
    dibujante.pendown()
    dibujante.goto(x, finY)

# Líneas horizontales
for y in range(inicioY, finY + 1, casillaSize):
    dibujante.penup()
    dibujante.goto(inicioX, y)
    dibujante.pendown()
    dibujante.goto(finX, y)


# Creamos un diccionario de tortugas invisibles que actuarán como "baldosas" de pasto
baldosas_pasto = {
}

for i in range(TableroSizeX):
    for j in range(TableroSizeY):
        coordenada_casilla = (i, j)
        nueva_baldosa = tr.Turtle()
        nueva_baldosa.hideturtle()
        nueva_baldosa.speed(0)
        nueva_baldosa.penup()
        nueva_baldosa.shape(grass)  # Le asignamos la imagen del pasto
        nueva_baldosa.goto(inicioX + (i * casillaSize) + (casillaSize // 2), inicioY + (j * casillaSize) + (casillaSize // 2))
        nueva_baldosa.showturtle()  # Mostramos la tortuga para que se vea el pasto
        baldosas_pasto[coordenada_casilla] = nueva_baldosa

def registrar_clic(x, y):
    if inicioX <= x <= finX and inicioY <= y <= finY:
        # Calcular los índices lógicos de la casilla (columna y fila)
        col = int((x - inicioX) // casillaSize)
        fila = int((y - inicioY) // casillaSize)
        coordenada_casilla = (col, fila)
        
        # Centro de la casilla en píxeles
        casilla_x = inicioX + (col * casillaSize) + (casillaSize // 2)
        casilla_y = inicioY + (fila * casillaSize) + (casillaSize // 2)
        
        # Si no existe una tortuga de pasto en esta casilla, la creamos
        if coordenada_casilla not in baldosas_pasto:
            nuevo_pasto = tr.Turtle()
            nuevo_pasto.speed(0)
            nuevo_pasto.penup()
            nuevo_pasto.goto(casilla_x, casilla_y)
            nuevo_pasto.shape(grass)  # Le asignamos la imagen del pasto
            # Guardamos la referencia
            baldosas_pasto[coordenada_casilla] = nuevo_pasto

# Activar detección de clics
pantalla.onclick(registrar_clic)


# --- CAPA DE TRAMPAS ---
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


# --- CAPA SUPERIOR: CONFIGURACIÓN DE JUGADORES ---
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

# Diccionario de posiciones
posiciones = {
    "J1": {"x": 0, "y": 0, "turtle": jugador1},
    "J2": {"x": 0, "y": 0, "turtle": jugador2}
}

turno_actual = "J1"  # Control de turnos

def lanzar_dado():
    pasos = rd.randint(1, 6)
    print(f"Turno de {turno_actual}: Sacó un {pasos}")
    mover_jugador(pasos)

def mover_jugador(pasos):
    global turno_actual
    jugador = posiciones[turno_actual]
    
    posicion_lineal_actual = jugador["y"] * TableroSizeX + jugador["x"]
    nueva_posicion_lineal = posicion_lineal_actual + pasos
    
    max_casillas = TableroSizeX * TableroSizeY
    if nueva_posicion_lineal >= max_casillas:
        nueva_posicion_lineal = max_casillas - 1
    if nueva_posicion_lineal < 0:
        nueva_posicion_lineal = 0
        
    jugador["x"] = nueva_posicion_lineal % TableroSizeX
    jugador["y"] = nueva_posicion_lineal // TableroSizeX

    if (jugador["x"], jugador["y"]) in casillas_trampa:
        print(f"¡¡MALA SUERTE!! {turno_actual} cayó en una trampa. Regresa al inicio.")
        jugador["x"] = 0
        jugador["y"] = 0

    pixel_x = inicioX + (jugador["x"] * casillaSize) + (casillaSize // 2)
    pixel_y = inicioY + (jugador["y"] * casillaSize) + (casillaSize // 2)
    
    jugador["turtle"].goto(pixel_x, pixel_y)
    
    turno_actual = "J2" if turno_actual == "J1" else "J1"

# Configurar el teclado para jugar
pantalla.listen()
pantalla.onkey(lanzar_dado, "space")

# Colocar jugadores en la salida al iniciar el juego
mover_jugador(0)
mover_jugador(0)

pantalla.mainloop()
