import turtle

# Configuración de la pantalla
win = turtle.Screen()
win.title("Tomb of the Mask - Turtle Edition")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)

# Variables de control de movimiento
dx = 0
dy = 0
is_moving = False

# El Laberinto: W = Pared, P = Punto, espacio blanco = Vacío
maze_layout = [
    "WWWWWWWWWWWWWWW",
    "W P P P P W P W",
    "W W W W W W P W",
    "W P P P P W P W",
    "W P W W P W P W",
    "W P P W P P W W",
    "W W P W W W P W",
    "W P P P P P P W",
    "W P W W W W W W",
    "W P P P W P P W",
    "W W W P W P W W",
    "W P P P P P P W",
    "WWWWWWWWWWWWWWW"
]

walls = []
dots = []

# Dibujante para las paredes y puntos
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# Configuración del Jugador
player = turtle.Turtle()
player.shape("square")
player.color("cyan")
player.penup()
player.speed(0)
player.goto(-200, 130) # Posición inicial

# Dibujar el mapa basado en la matriz
def setup_maze():
    for row_idx, row in enumerate(maze_layout):
        for col_idx, char in enumerate(row):
            # Calcular coordenadas de Turtle
            x = -240 + (col_idx * 35)
            y = 220 - (row_idx * 35)
            
            if char == "W":
                walls.append((x, y))
                pen.penup()
                pen.goto(x, y)
                pen.color("purple")
                pen.begin_fill()
                for _ in range(4):
                    pen.forward(30)
                    pen.right(90)
                pen.end_fill()
            elif char == "P":
                # Guardar posición para los puntos comestibles
                dots.append((x + 15, y - 15))

# Dibujar los puntos en la pantalla
dots_pen = turtle.Turtle()
dots_pen.hideturtle()
dots_pen.speed(0)
dots_pen.color("yellow")

def draw_dots():
    dots_pen.clear()
    for dot in dots:
        dots_pen.penup()
        dots_pen.goto(dot[0], dot[1] - 4)
        dots_pen.pendown()
        dots_pen.begin_fill()
        dots_pen.circle(4)
        dots_pen.end_fill()

# Detectar colisión con las paredes (Cajas de 30x30)
def check_wall_collision(nx, ny):
    for wx, wy in walls:
        # Verifica si el jugador entra en los límites físicos de la pared
        if nx + 15 > wx and nx - 15 < wx + 30:
            if ny + 15 > wy - 30 and ny - 15 < wy:
                return True
    return False

# Funciones de dirección (Mecánica Tomb of the Mask: solo cambia si está quieto)
def go_up():
    global dx, dy, is_moving
    if not is_moving:
        dx, dy = 0, 8
        is_moving = True

def go_down():
    global dx, dy, is_moving
    if not is_moving:
        dx, dy = 0, -8
        is_moving = True

def go_left():
    global dx, dy, is_moving
    if not is_moving:
        dx, dy = -8, 0
        is_moving = True

def go_right():
    global dx, dy, is_moving
    if not is_moving:
        dx, dy = 8, 0
        is_moving = True

# Asignar controles del teclado
win.listen()
win.onkeypress(go_up, "Up")
win.onkeypress(go_down, "Down")
win.onkeypress(go_left, "Left")
win.onkeypress(go_right, "Right")

# Inicializar escenario
setup_maze()
draw_dots()

# Bucle principal del juego
while True:
    win.update()
    
    if is_moving:
        # Calcular siguiente posición tentativa
        next_x = player.xcor() + dx
        next_y = player.ycor() + dy
        
        if not check_wall_collision(next_x, next_y):
            player.goto(next_x, next_y)
            
            # Recolectar puntos durante el deslizamiento
            for dot in dots[:]:
                if player.distance(dot) < 18:
                    dots.remove(dot)
                    draw_dots()
        else:
            # Detener el deslizamiento al chocar con una pared
            is_moving = False
            dx = 0
            dy = 0
            
    # Condición de Victoria
    if len(dots) == 0:
        dots_pen.keyup()
        dots_pen.goto(-100, 0)
        dots_pen.color("lime")
        dots_pen.write("¡VICTORIA!", font=("Arial", 24, "bold"))
        win.update()
        break
