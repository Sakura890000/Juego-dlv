import turtle as tl
import random as rd
import tkinter as tk
from tkinter import messagebox

ataques_posibles = ["right","left","up", "down"]
estados_posibles = ["rojo","verde"]

shield_pos = "left"
can_block = True
shield_reset = 70
velocidad_proyectiles = 3
estadofinal="PERDIO"
juego_activo = True
tiempo_restante = 20

ventana = tl.Screen()
ventana.setup(1200,700)
ventana.bgcolor("black")

ventana.register_shape("alma.gif")
ventana.register_shape("alma verde rota.gif")
ventana.register_shape("arrow down.gif")
ventana.register_shape("arrow up.gif")
ventana.register_shape("arrow left.gif")
ventana.register_shape("arrow right.gif")
ventana.register_shape("green arrow left.gif")
ventana.register_shape("green arrow right.gif")
ventana.register_shape("green arrow up.gif")
ventana.register_shape("green arrow down.gif")
ventana.register_shape("shield_left.gif")
ventana.register_shape("shield right.gif")
ventana.register_shape("shield up.gif")
ventana.register_shape("shield down.gif")


# --- Texto del Temporizador ---
reloj_texto = tl.Turtle()
reloj_texto.hideturtle()
reloj_texto.penup()
reloj_texto.color("white")
reloj_texto.goto(0, 300)
reloj_texto.write(f"TIEMPO: {tiempo_restante}", align="center", font=("Arial", 24, "bold"))


def mostrar_instrucciones_tk():
    texto = (
        "Undyne\n\n"
        "Cómo jugar:\n"
        "- Usa W/A/S/D o las flechas para colocar el escudo en la dirección deseada.\n"
        "- Bloquea las flechas VERDES. Si bloqueas una flecha ROJA o no bloqueas una VERDE, pierdes.\n"
        "- Sobrevive hasta que el temporizador llegue a 0.\n\n"
        "Pulsa Aceptar para comenzar."
    )
    try:
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Instrucciones - Undyne", texto, parent=root)
        root.destroy()
    except Exception:
        messagebox.showinfo("Instrucciones - Undyne", texto)

escudo = tl.Turtle()
escudo.penup()
escudo.shape("shield_left.gif")

flecha1 = tl.Turtle()
flecha1.penup()
flecha1.speed(0)
flecha1.goto(1400,0)
flecha1.shape("arrow left.gif")

# --- Función del Temporizador ---
def actualizar_tiempo():
    global tiempo_restante, estadofinal, juego_activo
    if not juego_activo:
        return
        
    if tiempo_restante > 0:
        tiempo_restante -= 1
        reloj_texto.clear()
        reloj_texto.write(f"TIEMPO: {tiempo_restante}", align="center", font=("Arial", 24, "bold"))
        ventana.ontimer(actualizar_tiempo, 1000)
    else:
        juego_activo = False
        estadofinal = "GANO"
        reloj_texto.clear()
        reloj_texto.color("green")
        reloj_texto.write("¡GANASTE!", align="center", font=("Arial", 30, "bold"))
        print(estadofinal)

def terminar_juego():
    ventana.bye()

def flecha_1():
    global shield_pos, juego_activo
    if not juego_activo:
        return
        
    estado = rd.choice(estados_posibles)
    ubicacion = rd.choice(ataques_posibles)
    if ubicacion  == "right":
        if estado == "rojo":
            flecha1.shape("arrow left.gif")
        if estado == "verde":
            flecha1.shape("green arrow left.gif")
        flecha1.goto(900,0)
        flecha1.speed(velocidad_proyectiles)
        angulo = flecha1.towards(alma_player)
        flecha1.seth(angulo)
        if juego_activo: flecha1.fd(900)

    elif ubicacion  == "left":
        if estado == "rojo":
            flecha1.shape("arrow right.gif")
        if estado == "verde":
            flecha1.shape("green arrow right.gif")
        flecha1.goto(-900,0)
        flecha1.speed(velocidad_proyectiles)
        angulo = flecha1.towards(alma_player)
        flecha1.seth(angulo)
        if juego_activo: flecha1.fd(900)

    elif ubicacion  == "up":
        if estado == "rojo":
            flecha1.shape("arrow down.gif")
        if estado == "verde":
            flecha1.shape("green arrow down.gif")
        flecha1.goto(0,650)
        flecha1.speed(velocidad_proyectiles - 1)
        angulo = flecha1.towards(alma_player)
        flecha1.seth(angulo)
        if juego_activo: flecha1.fd(650)

    elif ubicacion  == "down":
        if estado == "rojo":
            flecha1.shape("arrow up.gif")
        if estado == "verde":
            flecha1.shape("green arrow up.gif")
        flecha1.goto(0,-650)
        flecha1.speed(velocidad_proyectiles - 1)
        angulo = flecha1.towards(alma_player)
        flecha1.seth(angulo)
        if juego_activo: flecha1.fd(650)

    if juego_activo and flecha1.distance(alma_player) < 25:
        flecha1.speed(0)
        flecha1.goto(2000,2000)
        if shield_pos != ubicacion:
            if estado == "rojo":
                juego_activo = False
                alma_player.shape("alma verde rota.gif")
                reloj_texto.clear()
                reloj_texto.color("red")
                reloj_texto.write("PERDISTE", align="center", font=("Arial", 30, "bold"))
                ventana.ontimer(terminar_juego, 1200)
                print("PERDIO")
        elif shield_pos == ubicacion:
            if estado == "verde":
                juego_activo = False
                alma_player.shape("alma verde rota.gif")
                reloj_texto.clear()
                reloj_texto.color("red")
                reloj_texto.write("PERDISTE", align="center", font=("Arial", 30, "bold"))
                ventana.ontimer(terminar_juego, 1200)
                print("PERDIO")
            
    if juego_activo:
        ventana.ontimer(flecha_1,10)

alma_player = tl.Turtle()
alma_player.penup()
alma_player.shape("alma.gif")
alma_player.shapesize(1)

def reseteo_escudo():
    global can_block
    can_block = True

def derecha():
    global can_block, shield_pos
    if can_block and juego_activo:
        can_block = False
        ventana.ontimer(reseteo_escudo, shield_reset)
        shield_pos = "right"
        escudo.shape("shield right.gif")

def izquierda():
    global can_block, shield_pos
    if can_block and juego_activo:
        can_block = False
        ventana.ontimer(reseteo_escudo, shield_reset)
        shield_pos = "left"
        escudo.shape("shield_left.gif")

def arriba():
    global can_block, shield_pos
    if can_block and juego_activo:
        can_block = False
        ventana.ontimer(reseteo_escudo, shield_reset)
        shield_pos = "up"
        escudo.shape("shield up.gif")

def abajo():
    global can_block, shield_pos
    if can_block and juego_activo:
        can_block = False
        ventana.ontimer(reseteo_escudo, shield_reset)
        shield_pos = "down"
        escudo.shape("shield down.gif")

ventana.listen()
ventana.onkey(derecha, "d")
ventana.onkey(derecha, "Right")
ventana.onkey(izquierda, "a")
ventana.onkey(izquierda, "Left")
ventana.onkey(arriba, "w")
ventana.onkey(arriba, "Up")
ventana.onkey(abajo, "s")
ventana.onkey(abajo, "Down")

# Mostrar instrucciones en ventana modal antes de iniciar el juego
mostrar_instrucciones_tk()

ventana.ontimer(flecha_1, 10)
ventana.ontimer(actualizar_tiempo, 1000)

ventana.mainloop()
