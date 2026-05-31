from PIL import Image, ImageTk
import turtle as tr
import random as rd
import tkinter as tk

# --- VENTANA DADO (Tkinter) ---
ventana_dado = tk.Tk()
ventana_dado.title("Lanzar Dado")
ventana_dado.geometry("200x100")

def lanzar_dado():
    pasos = rd.randint(1, 6)
    print(f"Turno de {turno_actual}: Sacó un {pasos}")
    mover_jugador(pasos)

label_dado = tk.Label(ventana_dado, text="Presiona ESPACIO para lanzar el dado")
label_dado.pack(pady=20)
boton_lanzar = tk.Button(ventana_dado, text="Lanzar Dado", command=lanzar_dado)
boton_lanzar.pack()

# --- CONFIGURACIÓN PANTALLA (Turtle) ---
sculk = "sculk.gif"
perro = "perro.gif"
girar = "girar.gif"
grass = "grass.gif"
soul = "soul.gif"

pantalla = tr.Screen()
pantalla.tracer(0)  # Carga instantánea

# Registrar sprites
pantalla.register_shape(soul)
pantalla.register_shape(sculk)
pantalla.register_shape(girar)
pantalla.register_shape(perro)
pantalla.register_shape(grass)

pantalla.title("Tablero")
pantalla.bgcolor("#142750")
pantalla.setup(width=900, height=700)

# Variables de dimensiones
TableroSizeX = 20
TableroSizeY = 20
casillaSize = 32

inicioX = -(TableroSizeX * casillaSize) // 2
finX = (TableroSizeX * casillaSize) // 2
inicioY = -(TableroSizeY * casillaSize) // 2
finY = (TableroSizeY * casillaSize) // 2

# --- CAMINITO DISTRIBUIDO DE EXACTAMENTE 120 CASILLAS ---
# Aprovecha el perímetro y serpentea orgánicamente hacia el interior.
CAMINO_CASILLAS = [
    (0, 0), (1,0), (2, 0), (2, 1), (2, 2), (3,2), (4,2),
    (5,2), (6,2), (7,2), (8,2), (8,1),(9,1), (10,1), 
    (11,1), (12,1), (13,1), (14,1), (14, 2), (14,3), 
    (15,3), (16,3), (16,4), (16,5), (17,5), (18,5), 
    (18,6), (18,7), (18,8), (17,8), (16,8), (15,8),
    (14,8),(14,7),(14,6),(13,6),(12,6),(11,6),(10,6),
    (10,5),(10,4),(9,4),(8,4),(8,5),(8,6),(8,7),(8,8),
    (8,9),(8,10),(8,11),(7,11),(6,11),(5,11),(5,10),(5,9),
    (5,8),(5,7),(5,6),(5,5),(4,5),(3,5),(2,5),(1,5),(1,6),
    (1,7),(1,8),(1,9),(1,10),(1,11),(1,12),(2,12),(3,12),
    (3,13),(3,14),(4,14),(5,14),(6,14),(6,13),(7,13),
    (8,13),(9,13),(10,13),(10,12),(10,11),(10,10),(10,9),
    (10,8),(11,8),(12,8),(12,9),(12,10),(13,10),(14,10),
    (15,10),(16,10),(17,10),(17,11),(17,12),(17,13),
    (17,14),(17,15),(16,15),(15,15),(14,15),(13,15),
    (12,15),(11,15),(10,15),(9,15),(9,16),(8,16),(7,16),
    (6,16),(5,16),(4,16),(3,16),(2,16),(2,17),(2,18),
    (3,18),(4,18),(5,18),(6,18),(7,18),(8,18),(9,18),
    (10,18),(11,18),(12,18),(13,18),(14,18),(15,18),
    (16,18),(17,18),(17,19)
]

# --- DIBUJANTE DE CUADRÍCULA ---
dibujante = tr.Turtle()
dibujante.hideturtle()
dibujante.speed(0)
dibujante.color("black")

for x in range(inicioX, finX + 1, casillaSize):
    dibujante.penup()
    dibujante.goto(x, inicioY)
    dibujante.pendown()
    dibujante.goto(x, finY)

for y in range(inicioY, finY + 1, casillaSize):
    dibujante.penup()
    dibujante.goto(inicioX, y)
    dibujante.pendown()
    dibujante.goto(finX, y)

# --- GENERACIÓN VISUAL DEL TABLERO ---
baldosas_pasto = {}

for i in range(TableroSizeX):
    for j in range(TableroSizeY):
        coordenada_casilla = (i, j)
        nueva_baldosa = tr.Turtle()
        nueva_baldosa.hideturtle()
        nueva_baldosa.speed(0)
        nueva_baldosa.penup()
        
        if coordenada_casilla in CAMINO_CASILLAS:
            nueva_baldosa.shape(grass)
        else:
            nueva_baldosa.shape(sculk)
            
        nueva_baldosa.goto(inicioX + (i * casillaSize) + (casillaSize // 2), inicioY + (j * casillaSize) + (casillaSize // 2))
        nueva_baldosa.showturtle()
        baldosas_pasto[coordenada_casilla] = nueva_baldosa

def registrar_clic(x, y):
    if inicioX <= x <= finX and inicioY <= y <= finY:
        col = int((x - inicioX) // casillaSize)
        fila = int((y - inicioY) // casillaSize)
        coordenada_casilla = (col, fila)
        
        casilla_x = inicioX + (col * casillaSize) + (casillaSize // 2)
        casilla_y = inicioY + (fila * casillaSize) + (casillaSize // 2)
        
        if coordenada_casilla not in baldosas_pasto:
            nuevo_pasto = tr.Turtle()
            nuevo_pasto.speed(0)
            nuevo_pasto.penup()
            nuevo_pasto.goto(casilla_x, casilla_y)
            nuevo_pasto.shape(grass)
            baldosas_pasto[coordenada_casilla] = nuevo_pasto
            pantalla.update()

pantalla.onclick(registrar_clic)

# --- CAPA DE Juegos ---
CANTIDAD_MINIJUEGOS = 12 
casillas_juego = set()

pintor_juego = tr.Turtle()
pintor_juego.hideturtle()
pintor_juego.speed(0)
pintor_juego.shape(soul)

opciones_juego = CAMINO_CASILLAS[1:-1]

while len(casillas_juego) < CANTIDAD_MINIJUEGOS and opciones_juego:
    candidata = rd.choice(opciones_juego)
    if candidata not in casillas_juego:
        casillas_juego.add(candidata)
        
        tx, ty = candidata
        px = inicioX + (tx * casillaSize)
        py = inicioY + (ty * casillaSize)
        
        pintor_juego.penup()
        pintor_juego.goto(px, py)
        pintor_juego.pendown()
        pintor_juego.stamp()
        for _ in range(4):
            pintor_juego.forward(casillaSize)
            pintor_juego.left(90)
        pintor_juego.end_fill()

# --- CONFIGURACIÓN DE JUGADORES ---
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

posiciones = {
    "J1": {"casilla_actual": 0, "turtle": jugador1},
    "J2": {"casilla_actual": 0, "turtle": jugador2}
}

turno_actual = "J1"

def mover_jugador(pasos):
    global turno_actual
    jugador = posiciones[turno_actual]
    
    nueva_casilla = jugador["casilla_actual"] + pasos
    max_casillas = len(CAMINO_CASILLAS)
    
    if nueva_casilla >= max_casillas - 1:
        nueva_casilla = max_casillas - 1
        print(f"¡Felicidades! {turno_actual} ha llegado a la meta.")
        
    jugador["casilla_actual"] = nueva_casilla
    coordenada_logica = CAMINO_CASILLAS[nueva_casilla]

    if coordenada_logica in casillas_juego:
        print(f"¡¡MALA SUERTE!! {turno_actual} cayó en una juego. Regresa al inicio.")
        jugador["casilla_actual"] = 0
        coordenada_logica = CAMINO_CASILLAS[0]

    pixel_x = inicioX + (coordenada_logica[0] * casillaSize) + (casillaSize // 2)
    pixel_y = inicioY + (coordenada_logica[1] * casillaSize) + (casillaSize // 2)
    
    jugador["turtle"].goto(pixel_x, pixel_y)
    
    turno_actual = "J2" if turno_actual == "J1" else "J1"
    pantalla.update()

pantalla.listen()

# Inicializar jugadores en el bloque START (casilla 0)
mover_jugador(0)
mover_jugador(0)

pantalla.update()  # Renderizado rápido

pantalla.mainloop()
ventana_dado.mainloop()
