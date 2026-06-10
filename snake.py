import turtle as tr
import random as rd
import time
import sys

# Configuración de la pantalla
screen = tr.Screen()
screen.title("Mi piton")
screen.bgcolor("#78DF6E")
screen.tracer(0)

tableroSizeX = 15
tableroSizeY = 15
casillaSize = 32

PuntosNece=5
Puntos=0

inicioTabX = -((casillaSize * tableroSizeX) / 2)
inicioTabY = -((casillaSize * tableroSizeY) / 2)


def mostrar_instrucciones_snake():
    instr = tr.Turtle()
    instr.hideturtle()
    instr.penup()
    instr.color("white")
    try:
        y = screen.window_height() // 2 - 160
    except Exception:
        y = 200
    instr.goto(0, y)
    instr.write("Snake: Flechas para mover. Come la manzana. Evita chocar.", align="center", font=("Arial", 14, "bold"))
    screen.update()
    screen.ontimer(instr.clear, 2500)

# Rutas
perro = "assets/box.gif"
prota = "assets/criper.gif"
apple = "assets/gapple.gif"
ba = "assets/criperba.gif"

# Registrar figuras
try:
    screen.register_shape(perro)
    screen.register_shape(prota)
    screen.register_shape(apple)
    screen.register_shape(ba)
except tr.TurtleGraphicsError:
    print("Nota: No se encontraron los archivos .gif, usando figuras por defecto.")
    perro = "square"
    prota = "circle"

# Función para convertir coordenadas lógicas (0,0) a píxeles de pantalla
def obtener_pixeles(coord_logica):
    i, j = coord_logica
    pixel_x = inicioTabX + (i * casillaSize) + (casillaSize // 2)
    pixel_y = inicioTabY + (j * casillaSize) + (casillaSize // 2)
    return pixel_x, pixel_y

# Dibujar Tabero
Tablero = []
for i in range(tableroSizeX):
    for j in range(tableroSizeY):
        NuevBald = tr.Turtle()
        NuevBald.hideturtle()
        NuevBald.speed(0)
        NuevBald.penup()
        
        NuevBald.shape(perro)
        
        coordenada = (i, j)
        px, py = obtener_pixeles(coordenada)
        NuevBald.goto(px, py)
        NuevBald.showturtle()
        Tablero.append(coordenada)
# Score dibujadol

ScoreDib=tr.Turtle()
ScoreDib.hideturtle()
ScoreDib.color("#14442C")
ScoreDib.penup()
ScoreDib.goto(-250,250)
ScoreDib.write("Sin puntos",font=23)

#ScoreMax

ScoreNec=tr.Turtle()
ScoreNec.hideturtle()
ScoreNec.color("#14442C")
ScoreNec.penup()
ScoreNec.goto(150,250)
ScoreNec.write(f"Para pasar {PuntosNece} puntos",font=23)

#RESULTADODIBUJADORRR

Resultado=tr.Turtle()
Resultado.hideturtle()
Resultado.color("#14441A")
Resultado.penup()
Resultado.goto(0,100)
# Jugador
jugador = tr.Turtle()
jugador.shape(prota)
jugador.penup()
jugador.speed(0)

# Posición inicial
snake_coords = [(2, 2)] 
jugador.goto(obtener_pixeles(snake_coords[0]))

# Cuerpo de la serpiente
cuerpo = []

#comidinga
comida = tr.Turtle()
comida.shape(apple)
comida.penup()
comida.speed(0)

def colocar_comida():
    while True:
        nueva_pos = (rd.randint(0, tableroSizeX - 1), rd.randint(0, tableroSizeY - 1))
        if nueva_pos not in snake_coords:  # Que no aparezca encima de la serpiente
            comida.goto(obtener_pixeles(nueva_pos))
            return nueva_pos

comida_logica = colocar_comida()

# Movimiento
direccion = "stop"

def ir_arriba():
    global direccion
    if direccion != "abajo": direccion = "arriba"

def ir_abajo():
    global direccion
    if direccion != "arriba": direccion = "abajo"

def ir_izquierda():
    global direccion
    if direccion != "derecha": direccion = "izquierda"

def ir_derecha():
    global direccion
    if direccion != "izquierda": direccion = "derecha"

# Teclado
screen.listen()
screen.onkey(ir_arriba, "Up")
screen.onkey(ir_abajo, "Down")
screen.onkey(ir_izquierda, "Left")
screen.onkey(ir_derecha, "Right")

#añadil puntito

def anadirpunto():
    global Puntos
    Puntos+=1
    ScoreDib.clear()
    ScoreDib.write(f"kabra{Puntos}",font=23)

#  Bucle Principal del Juego

def perder(Pts, PtsNec):
    global juego_activo
    juego_activo = False # Frena el bucle automático

    if Pts >= PtsNec:
        Resultado.color("#61fa82")
        Resultado.write(f"Pasaste con {Puntos} Puntoss!!", font=("Arial", 24, "bold"), align="center")
        print("GANO", flush=True)
    else:
        Resultado.color("#fa6161")
        Resultado.write(f"Perdiste con {Puntos} Puntoss", font=("Arial", 24, "bold"), align="center")
        print("PERDIO", flush=True)
        
    # TRUCO AQUÍ: Fuerza a Turtle a renderizar el texto en pantalla AHORA MISMO
    screen.update() 
    
    # Espera 2 segundos mostrando el texto y luego cierra
    screen.ontimer(screen.bye, 1000) 


def paso_del_juego():
    global comida_logica

    if direccion != "stop":
        # Calcular la siguiente posición de la cabeza
        cabeza_x, cabeza_y = snake_coords[0]
        if direccion == "arriba":    cabeza_y += 1
        if direccion == "abajo":     cabeza_y -= 1
        if direccion == "izquierda": cabeza_x -= 1
        if direccion == "derecha":   cabeza_x += 1

        nueva_cabeza = (cabeza_x, cabeza_y)

        # Colisión 1: Bordes del tablero o morderse a sí misma
        if (cabeza_x < 0 or cabeza_x >= tableroSizeX or 
            cabeza_y < 0 or cabeza_y >= tableroSizeY or 
            nueva_cabeza in snake_coords):
            perder(Puntos,PuntosNece)
            screen.update()
            return

        # Insertar nueva cabeza al inicio de la lista lógica
        snake_coords.insert(0, nueva_cabeza)

        # Colisión 2: Comer la fruta
        if nueva_cabeza == comida_logica:
            comida_logica = colocar_comida()
            anadirpunto()

            # Crear un nuevo segmento para el cuerpo visual
            nuevo_segmento = tr.Turtle()
            nuevo_segmento.shape(ba)
            nuevo_segmento.penup()
            nuevo_segmento.speed(0)
            cuerpo.append(nuevo_segmento)
        else:
            # Si no come, se elimina el último elemento lógico (movimiento regular)
            snake_coords.pop()

        # Mover la cabeza de la serpiente
        jugador.goto(obtener_pixeles(snake_coords[0]))

        # Mover los segmentos del cuerpo
        for index in range(len(cuerpo)):
            px, py = obtener_pixeles(snake_coords[index + 1])
            cuerpo[index].goto(px, py)

    screen.update()
    screen.ontimer(paso_del_juego, 200)

# Inicia el bucle de juego
mostrar_instrucciones_snake()
paso_del_juego()
screen.mainloop()