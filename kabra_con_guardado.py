from PIL import Image, ImageTk
import turtle as tr
import random as rd
import tkinter as tk
from tkinter import messagebox
import time
import winsound as ws
import os
from guardar_juego import guardar_partida, cargar_partida, listar_partidas_guardadas, eliminar_partida

P1 = 0
P2 = 0

# --- VENTANA DADO (Tkinter) ---
ventana_dado = tk.Tk()
ventana_dado.title("🎲 Juego del Tablero 🎲")
ventana_dado.geometry("400x300")

def guardar_estado_actual():
#Guarda el estado actual del juego
    guardar_partida(P1, P2, turno_actual, posiciones, casillas_juego, casillas_trampa, casillas_lucky)
    messagebox.showinfo("Guardado", "✓ Partida guardada correctamente")

def cargar_estado_anterior():
    """Carga una partida anterior"""
    global P1, P2, turno_actual, posiciones, casillas_juego, casillas_trampa, casillas_lucky
    
    datos = cargar_partida()
    if datos is None:
        messagebox.showwarning("Error", "No hay partida guardada")
        return
    
    # Restaurar datos
    P1 = datos["puntos"]["P1"]
    P2 = datos["puntos"]["P2"]
    turno_actual = datos["turno_actual"]
    
    posiciones["J1"]["casilla_actual"] = datos["posiciones"]["J1"]["casilla_actual"]
    posiciones["J1"]["pierde_turno"] = datos["posiciones"]["J1"]["pierde_turno"]
    posiciones["J2"]["casilla_actual"] = datos["posiciones"]["J2"]["casilla_actual"]
    posiciones["J2"]["pierde_turno"] = datos["posiciones"]["J2"]["pierde_turno"]
    
    casillas_juego.clear()
    casillas_juego.update(datos["tablero"]["casillas_juego"])
    casillas_trampa.clear()
    casillas_trampa.update(datos["tablero"]["casillas_trampa"])
    casillas_lucky.clear()
    casillas_lucky.update(datos["tablero"]["casillas_lucky"])
    
    # Actualizar visualización
    puntos_label1.config(text=f"Puntos J1: {P1}")
    puntos_label2.config(text=f"Puntos J2: {P2}")
    label_dado.config(text=f"Turno: {turno_actual}\n(Partida Cargada)")
    
    # Redibujar casillas con sus posiciones guardadas
    redibujar_casillas()
    
    # Recrear el dado y las fichas para que queden encima de las casillas
    recrear_tokens()

    # Redibujar ambos jugadores en sus posiciones correctas
    temp_turno = turno_actual
    turno_actual = "J1"
    mover_jugador(0)
    turno_actual = "J2"
    mover_jugador(0)
    turno_actual = temp_turno
    
    # Asegurar que los jugadores y el dado queden visibles
    posiciones["J1"]["turtle"].showturtle()
    posiciones["J2"]["turtle"].showturtle()
    
    pantalla.update()
    
    messagebox.showinfo("Cargado", "✓ Partida cargada correctamente")

def lanzar_dado():
    global turno_actual

    if posiciones[turno_actual]["pierde_turno"]:
        print(f"{turno_actual} salta su turno por caer en Soul.")
        label_dado.config(text=f"{turno_actual} salta su turno...")
        posiciones[turno_actual]["pierde_turno"] = False
        turno_actual = "J2" if turno_actual == "J1" else "J1"
        return
        
    boton_lanzar.config(state="disabled")
    ruta_sonido = os.path.join(os.path.dirname(__file__), "dice (mp3cut.net).wav")
    
    if os.path.exists(ruta_sonido):
        try:
            ws.PlaySound(ruta_sonido, ws.SND_FILENAME | ws.SND_ASYNC)
        except:
            pass
    
    for _ in range(6):
        cara_aleatoria = rd.randint(1, 6)
        display_dado.shape(f"{cara_aleatoria}.gif")
        pantalla.update()
        time.sleep(0.1)
    
    pasos = rd.randint(1, 6)
    print(f"Turno de {turno_actual}: Sacó un {pasos}")
    label_dado.config(text=f"¡{turno_actual} sacó un {pasos}!")
    
    display_dado.shape(f"{pasos}.gif")
    pantalla.update()
    
    time.sleep(0.4)
    
    mover_jugador(pasos)

# --- BOTONES ---
frame_botones = tk.Frame(ventana_dado)
frame_botones.pack(pady=10)

label_dado = tk.Label(ventana_dado, text="Presiona el botón para lanzar el dado", font=("Arial", 10))
label_dado.pack(pady=10)

boton_lanzar = tk.Button(frame_botones, text="🎲 Lanzar Dado", command=lanzar_dado, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
boton_lanzar.pack(side="left", padx=5)

boton_guardar = tk.Button(frame_botones, text="💾 Guardar", command=guardar_estado_actual, bg="#2196F3", fg="white", font=("Arial", 10, "bold"))
boton_guardar.pack(side="left", padx=5)

boton_cargar = tk.Button(frame_botones, text="📂 Cargar", command=cargar_estado_anterior, bg="#FF9800", fg="white", font=("Arial", 10, "bold"))
boton_cargar.pack(side="left", padx=5)

frame_puntos = tk.Frame(ventana_dado)
frame_puntos.pack(pady=10)

puntos_label1 = tk.Label(frame_puntos, text=f"Puntos J1: {P1}", bg="#E8F5E9", fg="#2E7D32", font=("Arial", 11, "bold"), padx=10, pady=5)
puntos_label1.pack(side="left", padx=10)

puntos_label2 = tk.Label(frame_puntos, text=f"Puntos J2: {P2}", bg="#E3F2FD", fg="#1565C0", font=("Arial", 11, "bold"), padx=10, pady=5)
puntos_label2.pack(side="left", padx=10)

info_label = tk.Label(ventana_dado, text=listar_partidas_guardadas(), font=("Arial", 9), fg="#666")
info_label.pack(pady=5)

# --- CONFIGURACIÓN PANTALLA (Turtle) ---
sculk = "assets/sculk.gif"
perro = "assets/perro.gif"
girar = "assets/girar.gif"
box = "assets/box.gif"
soul = "assets/soul.gif"
portal = "assets/portal.gif"
luck = "assets/luck.gif"
finale = "assets/finale.gif"
inizio="assets/beacon.gif"
pantalla = tr.Screen()
pantalla.tracer(0)

# Registrar sprites
pantalla.register_shape(luck)
pantalla.register_shape(portal)
for i in range(1, 7):
    pantalla.register_shape(f"{i}.gif")
pantalla.register_shape(inizio)
pantalla.register_shape(finale)
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

# --- CAMINITO DE 120 CASILLAS ---
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

# --- ESCRITOR DE ALERTAS ---
escritor_alertas = tr.Turtle()
escritor_alertas.hideturtle()
escritor_alertas.penup()
escritor_alertas.color("orange")
escritor_alertas.goto(0, 50)

alertas_lucky = tr.Turtle()
alertas_lucky.hideturtle()
alertas_lucky.penup()
alertas_lucky.color("yellow")
alertas_lucky.goto(0, 20)

# --- CAPA DE MINIJUEGOS ---
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

# --- CASILLA INICIAL Y FINAL (turtles separados) ---
pintor_inicial = tr.Turtle()
pintor_inicial.hideturtle()
pintor_inicial.speed(0)
pintor_inicial.shape(finale)

pintor_final = tr.Turtle()
pintor_final.hideturtle()
pintor_final.speed(0)
pintor_final.shape(inizio)

# Dibujar casilla inicial
tx, ty = CAMINO_CASILLAS[0]
px = inicioX + (tx * casillaSize) + (casillaSize // 2)
py = inicioY + (ty * casillaSize) + (casillaSize // 2)
pintor_inicial.penup()
pintor_inicial.goto(px, py)
pintor_inicial.stamp()

# Dibujar casilla final
tx, ty = CAMINO_CASILLAS[-1]
px = inicioX + (tx * casillaSize) + (casillaSize // 2)
py = inicioY + (ty * casillaSize) + (casillaSize // 2)
pintor_final.penup()
pintor_final.goto(px, py)
pintor_final.stamp()


# --- CAPA DE LUCKY ---
CANTIDAD_LUCKYS = 14
casillas_lucky = set()

pintor_lucky = tr.Turtle()
pintor_lucky.hideturtle()
pintor_lucky.speed(0)
pintor_lucky.shape(luck)

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

# Placeholders for display and player turtles; will be (re)created
display_dado = None
jugador1 = None
jugador2 = None

posiciones = {
    "J1": {"casilla_actual": 0, "turtle": None, "pierde_turno": False},
    "J2": {"casilla_actual": 0, "turtle": None, "pierde_turno": False}
}

turno_actual = "J1"



def redibujar_casillas():
    """Redibuja todas las casillas del tablero (minijuegos, trampas y lucky)"""
    # Limpiar stamps anteriores
    pintor_juego.clearstamps()
    pintor_trampa.clearstamps()
    pintor_lucky.clearstamps()
    pintor_inicial.clearstamps()
    pintor_final.clearstamps()
    
    # Redibujar casillas de minijuegos
    for casilla in casillas_juego:
        tx, ty = casilla
        px = inicioX + (tx * casillaSize) + (casillaSize // 2)
        py = inicioY + (ty * casillaSize) + (casillaSize // 2)
        pintor_juego.penup()
        pintor_juego.goto(px, py)
        pintor_juego.stamp()
    
    # Redibujar casillas de trampas
    for casilla in casillas_trampa:
        tx, ty = casilla
        px = inicioX + (tx * casillaSize) + (casillaSize // 2)
        py = inicioY + (ty * casillaSize) + (casillaSize // 2)
        pintor_trampa.penup()
        pintor_trampa.goto(px, py)
        pintor_trampa.stamp()
    
    # Redibujar casillas lucky
    for casilla in casillas_lucky:
        tx, ty = casilla
        px = inicioX + (tx * casillaSize) + (casillaSize // 2)
        py = inicioY + (ty * casillaSize) + (casillaSize // 2)
        pintor_lucky.penup()
        pintor_lucky.goto(px, py)
        pintor_lucky.stamp()
    
    # Redibujar casilla inicial
    tx, ty = CAMINO_CASILLAS[0]
    px = inicioX + (tx * casillaSize) + (casillaSize // 2)
    py = inicioY + (ty * casillaSize) + (casillaSize // 2)
    pintor_inicial.penup()
    pintor_inicial.goto(px, py)
    pintor_inicial.stamp()
    
    # Redibujar casilla final
    tx, ty = CAMINO_CASILLAS[-1]
    px = inicioX + (tx * casillaSize) + (casillaSize // 2)
    py = inicioY + (ty * casillaSize) + (casillaSize // 2)
    pintor_final.penup()
    pintor_final.goto(px, py)
    pintor_final.stamp()

def recrear_tokens():
    """(Re)crea el dado y las fichas para garantizar que queden en primer plano."""
    global display_dado, jugador1, jugador2, posiciones
    try:
        if display_dado:
            display_dado.hideturtle()
    except Exception:
        pass

    display_dado = tr.Turtle()
    display_dado.penup()
    display_dado.goto(390, 250)
    display_dado.shape("1.gif")
    display_dado.showturtle()

    try:
        if jugador1:
            jugador1.hideturtle()
        if jugador2:
            jugador2.hideturtle()
    except Exception:
        pass

    jugador1 = tr.Turtle()
    jugador1.shape(girar)
    jugador1.penup()
    jugador1.speed(3)

    jugador2 = tr.Turtle()
    jugador2.shape(perro)
    jugador2.penup()
    jugador2.speed(3)

    posiciones["J1"]["turtle"] = jugador1
    posiciones["J2"]["turtle"] = jugador2




def mover_jugador(pasos):
    global turno_actual, P1, P2
    jugador = posiciones[turno_actual]
    
    if pasos > 0:
        nueva_casilla = jugador["casilla_actual"] + pasos
        max_casillas = len(CAMINO_CASILLAS)
        
        if nueva_casilla >= max_casillas - 1:
            nueva_casilla = max_casillas - 1
            if turno_actual == "J1":
                P1 += 1
            else:
                P2 += 1
            print(f"¡Felicidades! {turno_actual} ha llegado a la meta.")
            puntos_label1.config(text=f"Puntos J1: {P1}")
            puntos_label2.config(text=f"Puntos J2: {P2}")
            
        jugador["casilla_actual"] = nueva_casilla
    
    coordenada_logica = CAMINO_CASILLAS[jugador["casilla_actual"]]

    if pasos > 0 and coordenada_logica in casillas_juego:
        escritor_alertas.write(f"¡{turno_actual} CAYÓ EN UN MINIJUEGO!", align="center", font=("Arial", 24, "bold"))
        ventana_dado.after(2000, escritor_alertas.clear)
        print(f"{turno_actual} cayó en un minijuego. ¡A jugar!.")
        ruta_sonido = os.path.join(os.path.dirname(__file__), "Jijija.wav")
    
        if os.path.exists(ruta_sonido):
            try:
                ws.PlaySound(ruta_sonido, ws.SND_FILENAME | ws.SND_ASYNC)
            except:
                pass

    if pasos > 0 and coordenada_logica in casillas_trampa:
        escritor_alertas.write(f"¡{turno_actual} CAYÓ EN UN SOUL!", align="center", font=("Arial", 24, "bold"))
        ventana_dado.after(2000, escritor_alertas.clear)
        print(f"¡OH NO! {turno_actual} cayó en un Soul. ¡Perdiste un turno!")
        label_dado.config(text=f"¡{turno_actual} cayó en Soul!\nPerdiste un turno")
        jugador["pierde_turno"] = True
        alertas_lucky.write(f"¡{turno_actual} PERDIÓ UN TURNO!", align="center", font=("Arial", 24, "bold"))
        ventana_dado.after(2000, alertas_lucky.clear)
        ruta_sonido = os.path.join(os.path.dirname(__file__), "Bruh.wav")
    
        if os.path.exists(ruta_sonido):
            try:
                ws.PlaySound(ruta_sonido, ws.SND_FILENAME | ws.SND_ASYNC)
            except:
                pass

    if pasos > 0 and coordenada_logica in casillas_lucky:
        ruta_sonido = os.path.join(os.path.dirname(__file__), "China.wav")
    
        if os.path.exists(ruta_sonido):
            try:
                ws.PlaySound(ruta_sonido, ws.SND_FILENAME | ws.SND_ASYNC)
            except:
                pass
        escritor_alertas.write(f"¡{turno_actual} ENCONTRÓ UN LUCKY!", align="center", font=("Arial", 24, "bold"))
        ventana_dado.after(2000, escritor_alertas.clear)
        print(f"¡UY! {turno_actual} encontró un Lucky. ¡Avanza o retrocede 2 casillas extra!")
        label_dado.config(text=f"¡{turno_actual} encontró un Lucky!\nAvanza o retrocede 2 casillas extra")
        opcion = rd.choice(["avanzar", "retroceder"])
        if opcion == "avanzar":
            alertas_lucky.write(f"¡{turno_actual} eligió avanzar!", align="center", font=("Arial", 24, "bold"))
        else:
            alertas_lucky.write(f"¡{turno_actual} eligió retroceder!", align="center", font=("Arial", 24, "bold"))
        ventana_dado.after(2000, alertas_lucky.clear)

        def aplicar_lucky():
            global turno_actual, P1, P2
            if opcion == "avanzar":
                jugador["casilla_actual"] += 2
            else:
                jugador["casilla_actual"] -= 2

            max_casillas = len(CAMINO_CASILLAS)
            if jugador["casilla_actual"] >= max_casillas - 1:
                ruta = os.path.join(os.path.dirname(__file__), "winner.wav")
                if os.path.exists(ruta):
                    try:
                        ws.PlaySound(ruta, ws.SND_FILENAME | ws.SND_ASYNC)
                    except:
                        pass
                jugador["casilla_actual"] = max_casillas - 1
                if turno_actual == "J1":
                    P1 += 1
                else:
                    P2 += 1
                puntos_label1.config(text=f"Puntos J1: {P1}")
                puntos_label2.config(text=f"Puntos J2: {P2}")
                print(f"¡Felicidades! {turno_actual} ha llegado a la meta.")
            elif jugador["casilla_actual"] < 0:
                jugador["casilla_actual"] = 0

            coordenada_lucky = CAMINO_CASILLAS[jugador["casilla_actual"]]
            pixel_x = inicioX + (coordenada_lucky[0] * casillaSize) + (casillaSize // 2)
            pixel_y = inicioY + (coordenada_lucky[1] * casillaSize) + (casillaSize // 2)
            jugador["turtle"].goto(pixel_x, pixel_y)
            turno_actual = "J2" if turno_actual == "J1" else "J1"
            pantalla.update()
            boton_lanzar.config(state="normal")

        ventana_dado.after(4000, aplicar_lucky)
        return

            

    pixel_x = inicioX + (coordenada_logica[0] * casillaSize) + (casillaSize // 2)
    pixel_y = inicioY + (coordenada_logica[1] * casillaSize) + (casillaSize // 2)
    
    jugador["turtle"].goto(pixel_x, pixel_y)
    
    if pasos > 0:
        turno_actual = "J2" if turno_actual == "J1" else "J1"
        
    pantalla.update()
    boton_lanzar.config(state="normal")

pantalla.listen()

# Inicializar jugadores en el bloque START (casilla 0)

# (Re)crear tortugas para que queden visibles encima de las casillas
recrear_tokens()

mover_jugador(0)
turno_actual = "J2"
mover_jugador(0)
turno_actual = "J1"

pantalla.update()
pantalla.mainloop()
ventana_dado.mainloop()
