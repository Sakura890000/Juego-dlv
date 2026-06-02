import turtle
import os

# Configuración de la pantalla de juego
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#333333")  # Fondo gris como el asfalto de la ciudad
screen.title("Mini GTA 2D - Concepto")

gato = os.path.join("assets", "girar.gif")
try:
    screen.register_shape(gato)
except Exception:
    pass


# Crear el auto del jugador
jugador = turtle.Turtle()
try:
    jugador.shape(gato)  # Representa el auto
except Exception:
    pass
jugador.color("#ff007f")  # Auto rosa neón
jugador.shapesize(1, 1)  # Forma alargada de auto
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
    if velocidad > -2:  # Marcha atrás
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

screen.tracer(0)

def game_loop():
    global velocidad
    # Mover el auto hacia adelante según su velocidad actual
    jugador.forward(velocidad)

    # Sistema básico de fricción para que se detenga solo si no aceleras
    if velocidad > 0:
        velocidad -= 0.02
        if velocidad < 0:
            velocidad = 0
    elif velocidad < 0:
        velocidad += 0.02
        if velocidad > 0:
            velocidad = 0

    screen.update()
    # Llamar de nuevo en ~20ms (50 FPS)
    screen.ontimer(game_loop, 20)

# Iniciar bucle sin bloquear el hilo de eventos
game_loop()
screen.mainloop()
