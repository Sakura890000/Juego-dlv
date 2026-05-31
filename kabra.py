from PIL import Image, ImageTk
import turtle as tr
import random as rd
import tkinter as tk
import time  # Importamos time para manejar pausas breves
import winsound as ws
import os

P1 = 0
P2 = 0


# --- VENTANA DADO (Tkinter) ---

ventana_dado = tk.Tk()
ventana_dado.title("Lanzar Dado")
ventana_dado.geometry("200x200")

def lanzar_dado():
    global turno_actual

    # NUEVO: Verificar si el jugador actual tiene el turno perdido
    if posiciones[turno_actual]["pierde_turno"]:
        print(f"{turno_actual} salta su turno por caer en Soul.")
        label_dado.config(text=f"{turno_actual} salta su turno...")
        posiciones[turno_actual]["pierde_turno"] = False # Se limpia la penalización
        turno_actual = "J2" if turno_actual == "J1" else "J1" # Pasa el turno al otro
        return # Cancela el resto del lanzamiento
        
    # Deshabilita el botón inmediatamente para evitar spam de clics
    boton_lanzar.config(state="disabled")
        # Encuentra la ruta exacta de la carpeta actual del script
    ruta_sonido = os.path.join(os.path.dirname(__file__), "Voicy_awdasd.wav")
    
    # Reproduce el sonido correctamente usando ambas banderas unidas por el operador '|'
    ws.PlaySound(ruta_sonido, ws.SND_FILENAME | ws.SND_ASYNC)

    # Deshabilita el botón inmediatamente para evitar spam de clics
    boton_lanzar.config(state="disabled")
    
    # --- ANIMACIÓN DEL DADO (Efecto Ruleta) ---
    # Cambia rápidamente de cara 6 veces para simular que está girando
    for _ in range(6):
        cara_aleatoria = rd.randint(1, 6)
        display_dado.shape(f"{cara_aleatoria}.gif")
        pantalla.update()
        time.sleep(0.1) # Pausa de 100 milisegundos entre giros
    
    # Resultado definitivo
    pasos = rd.randint(1, 6)
    print(f"Turno de {turno_actual}: Sacó un {pasos}")
    label_dado.config(text=f"¡{turno_actual} sacó un {pasos}!")
    
    # Muestra el resultado final en el display
    display_dado.shape(f"{pasos}.gif")
    pantalla.update()
    
    # Breve pausa con el número final antes de que el jugador empiece a moverse
    time.sleep(0.4)
    
    # Mueve al jugador
    mover_jugador(pasos)

label_dado = tk.Label(ventana_dado, text="Presiona el botón para lanzar el dado")
label_dado.pack(pady=20)
boton_lanzar = tk.Button(ventana_dado, text="Lanzar Dado", command=lanzar_dado)
boton_lanzar.pack()

puntos_label1 = tk.Label(ventana_dado, text=f"Puntos J1: {P1}")
puntos_label1.pack(side="left", padx=10)
puntos_label2 = tk.Label(ventana_dado, text=f"Puntos J2: {P2}")
puntos_label2.pack(side="right", padx=10)

# --- CONFIGURACIÓN PANTALLA (Turtle) ---
sculk = "sculk.gif"
perro = "perro.gif"
girar = "girar.gif"
box = "box.gif"
soul = "soul.gif"
portal = "portal.gif"
luck= "luck.gif"

pantalla = tr.Screen()
pantalla.tracer(0)  # Carga instantánea

# Registrar sprites
pantalla.register_shape(luck)
pantalla.register_shape(portal)
pantalla.register_shape("1.gif")
pantalla.register_shape("2.gif")
pantalla.register_shape("3.gif")
pantalla.register_shape("4.gif")
pantalla.register_shape("5.gif")
pantalla.register_shape("6.gif")
pantalla.register_shape(soul)
pantalla.register_shape(sculk)
pantalla.register_shape(girar)
pantalla.register_shape(perro)
pantalla.register_shape(box)

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
            nueva_baldosa.shape(box)
        else:
            nueva_baldosa.shape(sculk)
            
        nueva_baldosa.goto(inicioX + (i * casillaSize) + (casillaSize // 2), inicioY + (j * casillaSize) + (casillaSize // 2))
        nueva_baldosa.showturtle()
        baldosas_pasto[coordenada_casilla] = nueva_baldosa

# --- ESCRITOR DE ALERTAS EN PANTALLA ---
escritor_alertas = tr.Turtle()
escritor_alertas.hideturtle()
escritor_alertas.penup()
escritor_alertas.color("orange") # Color llamativo para la trampa
escritor_alertas.goto(0, 50)

alertas_lucky = tr.Turtle()
alertas_lucky.hideturtle()
alertas_lucky.penup()
alertas_lucky.color("yellow") # Color llamativo para el lucky
alertas_lucky.goto(0, 20)



# --- CAPA DE JUEGOS ---
CANTIDAD_MINIJUEGOS = 12 
casillas_juego = set()

pintor_juego = tr.Turtle()
pintor_juego.hideturtle()
pintor_juego.speed(0)
pintor_juego.shape(portal)

opciones_juego = CAMINO_CASILLAS[1:-1]

while len(casillas_juego) < CANTIDAD_MINIJUEGOS and opciones_juego:
    candidata = rd.choice(opciones_juego)
    if candidata not in casillas_juego:
        casillas_juego.add(candidata)
        
        tx, ty = candidata
        px = inicioX + (tx * casillaSize) + (casillaSize // 2)
        py = inicioY + (ty * casillaSize) + (casillaSize // 2)
        
        pintor_juego.penup()
        pintor_juego.goto(px, py)
        pintor_juego.stamp()

# --- CAPA DE TRAMPAS (SOUL) ---
CANTIDAD_TRAMPAS = 14
casillas_trampa = set()

pintor_trampa = tr.Turtle()
pintor_trampa.hideturtle()
pintor_trampa.speed(0)
pintor_trampa.shape(soul)

# Filtrar opciones para no pisar las casillas iniciales, finales ni los minijuegos actuales
opciones_trampa = [c for c in CAMINO_CASILLAS[1:-1] if c not in casillas_juego]

while len(casillas_trampa) < CANTIDAD_TRAMPAS and opciones_trampa:
    candidata = rd.choice(opciones_trampa)
    if candidata not in casillas_trampa:
        casillas_trampa.add(candidata)
        
        tx, ty = candidata
        px = inicioX + (tx * casillaSize) + (casillaSize // 2)
        py = inicioY + (ty * casillaSize) + (casillaSize // 2)
        
        pintor_trampa.penup()
        pintor_trampa.goto(px, py)
        pintor_trampa.stamp()

# --- CAPA DE Lucky ---
CANTIDAD_LUCKYS = 14
casillas_lucky = set()

pintor_lucky = tr.Turtle()
pintor_lucky.hideturtle()
pintor_lucky.speed(0)
pintor_lucky.shape(luck)

# Filtrar opciones para no pisar las casillas iniciales, finales ni los minijuegos actuales
opciones_lucky = [c for c in CAMINO_CASILLAS[1:-1] if c not in casillas_juego]

while len(casillas_lucky) < CANTIDAD_LUCKYS and opciones_lucky:
    candidata = rd.choice(opciones_lucky)
    if candidata not in casillas_lucky:
        casillas_lucky.add(candidata)
        
        tx, ty = candidata
        px = inicioX + (tx * casillaSize) + (casillaSize // 2)
        py = inicioY + (ty * casillaSize) + (casillaSize // 2)
        
        pintor_lucky.penup()
        pintor_lucky.goto(px, py)
        pintor_lucky.stamp()

# --- DISPLAY VISUAL DEL DADO ---
display_dado = tr.Turtle()
display_dado.penup()
display_dado.goto(0, 0) 
display_dado.shape("1.gif")

# --- CONFIGURACIÓN DE JUGADORES ---
jugador1 = tr.Turtle()
jugador1.shape(girar)
jugador1.penup()
jugador1.speed(3)

jugador2 = tr.Turtle()
jugador2.shape(perro)
jugador2.penup()
jugador2.speed(3)

posiciones = {
    "J1": {"casilla_actual": 0, "turtle": jugador1, "pierde_turno": False},
    "J2": {"casilla_actual": 0, "turtle": jugador2, "pierde_turno": False}
}

turno_actual = "J1"

def mover_jugador(pasos):
    global turno_actual
    jugador = posiciones[turno_actual]
    
    if pasos > 0:
        nueva_casilla = jugador["casilla_actual"] + pasos
        max_casillas = len(CAMINO_CASILLAS)
        
        if nueva_casilla >= max_casillas - 1:
            nueva_casilla = max_casillas - 1
            print(f"¡Felicidades! {turno_actual} ha llegado a la meta.")
            
        jugador["casilla_actual"] = nueva_casilla
    
    coordenada_logica = CAMINO_CASILLAS[jugador["casilla_actual"]]

    if pasos > 0 and coordenada_logica in casillas_juego:
        escritor_alertas.write(f"¡{turno_actual} CAIÓ EN UN MINIJUEGO!", align="center", font=("Arial", 24, "bold"))
        ventana_dado.after(2000, escritor_alertas.clear)
        print(f"{turno_actual} cayó en un minijuego. ¡A jugar!.")

# NUEVO: Evaluar si el jugador cayó en una casilla trampa soul
    if pasos > 0 and coordenada_logica in casillas_trampa:
        escritor_alertas.write(f"¡{turno_actual} CAIÓ EN UN SOUL!", align="center", font=("Arial", 24, "bold"))
        ventana_dado.after(2000, escritor_alertas.clear)
        print(f"¡OH NO! {turno_actual} cayó en un Soul. ¡Perdiste un turno!")
        label_dado.config(text=f"¡{turno_actual} cayó en Soul!\nPerdiste un turno")
        jugador["pierde_turno"] = True
        # NUEVO: Escribe el texto gigante en el centro de la pantalla de Turtle
        escritor_alertas.write(f"¡{turno_actual} PERDIÓ UN TURNO!", align="center", font=("Arial", 24, "bold"))
        ventana_dado.after(2000, escritor_alertas.clear)

    if pasos > 0 and coordenada_logica in casillas_lucky:
        escritor_alertas.write(f"¡{turno_actual} ENCONTRÓ UN LUCKY!", align="center", font=("Arial", 24, "bold"))
        ventana_dado.after(2000, escritor_alertas.clear)
        print(f"¡UY! {turno_actual} encontró un Lucky. ¡Avanza o retrocede 2 casillas extra!")
        label_dado.config(text=f"¡{turno_actual} encontró un Lucky!\nAvanza o retrocede 2 casillas extra")
        opcion = rd.choice(["avanzar", "retroceder"])
        if opcion == "avanzar":
            jugador["casilla_actual"] += 2
            alertas_lucky.write(f"¡{turno_actual} eligió avanzar!", align="center", font=("Arial", 24, "bold"))
            ventana_dado.after(2000, alertas_lucky.clear)
        else:
            jugador["casilla_actual"] -= 2
            alertas_lucky.write(f"¡{turno_actual} eligió retroceder!", align="center", font=("Arial", 24, "bold"))
            ventana_dado.after(2000, alertas_lucky.clear)
        if jugador["casilla_actual"] >= len(CAMINO_CASILLAS) - 1:
            jugador["casilla_actual"] = len(CAMINO_CASILLAS) - 1
            print(f"¡Felicidades! {turno_actual} ha llegado a la meta.")

    pixel_x = inicioX + (coordenada_logica[0] * casillaSize) + (casillaSize // 2)
    pixel_y = inicioY + (coordenada_logica[1] * casillaSize) + (casillaSize // 2)
    
    jugador["turtle"].goto(pixel_x, pixel_y)
    
    if pasos > 0:
        turno_actual = "J2" if turno_actual == "J1" else "J1"
        
    pantalla.update()
    boton_lanzar.config(state="normal")

pantalla.listen()

def gta():
    screen = tr.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("#333333") # Fondo gris como el asfalto de la ciudad
    screen.title("Mini GTA 2D - Concepto")
    gato="girar.gif"
    screen.register_shape(gato)


    # Crear el auto del jugador
    jugador = tr.Turtle()
    jugador.shape(gato) # Representa el auto
    jugador.color("#ff007f") # Auto rosa neón
    jugador.shapesize(1,1) # Forma alargada de auto
    jugador.penup()
    jugador.speed(0)

    # Variables de física simple
    velocidad = 0
    max_velocidad = 6

    # Funciones de control del vehículo
    def acelerar():
        global velocidad
        if velocidad < max_velocidad:
            velocidad += 1

    def frenar():
        global velocidad
        if velocidad > -2: # Marcha atrás
            velocidad -= 1

    def girar_izquierda():
        if velocidad != 0:
            jugador.left(15)

    def girar_derecha():
        if velocidad != 0:
            jugador.right(15)

    # Conectar el teclado con el juego
    screen.listen()
    screen.onkeypress(acelerar, "Up")
    screen.onkeypress(frenar, "Down")
    screen.onkeypress(girar_izquierda, "Left")
    screen.onkeypress(girar_derecha, "Right")

    # Bucle principal del juego
    while True:
        # Mover el auto hacia adelante según su velocidad actual
        jugador.forward(velocidad)
        
        # Sistema básico de fricción para que se detenga solo si no aceleras
        if velocidad > 0:
            velocidad -= 0.02
        elif velocidad < 0:
            velocidad += 0.02
            
        screen.update()


def iniciar_juego():
    juego=rd.randint(1,8)
    match juego:
        case 1:
            print("¡Minijuego 1: Adivina el número!")
        case 2:
            print("¡Minijuego 2: Carrera de tortugas!")
        case 3:
            print("¡Minijuego 3: Memoria visual!")
        case 4:
            print("¡Minijuego 4: Piedra, papel o tijera!")
        case 5:
            print("¡Minijuego 5: Laberinto!")
        case 6:
            print("¡Minijuego 6: Rompecabezas!")
        case 7:
            print("¡Minijuego 7: Trivia rápida!")
        case 8:
            print("¡Minijuego 8: Carrera de dados!")


# Inicializar jugadores en el bloque START (casilla 0)
mover_jugador(0)
turno_actual = "J2"
mover_jugador(0)
turno_actual = "J1"

pantalla.update()
gta()  # Inicia el mini GTA en una ventana aparte
pantalla.mainloop()
ventana_dado.mainloop()


