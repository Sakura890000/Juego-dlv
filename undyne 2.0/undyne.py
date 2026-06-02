import turtle as tl
import random as rd
# listas listicas sahur
ataques_posibles = ["right","left","up", "down"]
estados_posibles = ["rojo","verde"]
#tung tung tung variables
shield_pos = "left"
can_block = True
shield_reset = 70
velocidad_proyectiles = 3

ventana = tl.Screen()
ventana.setup(1200,700)
# six seven
ventana.bgcolor("black")

#/////sprites//////

#alma sprites
ventana.register_shape("alma.gif")
ventana.register_shape("alma verde rota.gif")

#proyectiles sprites
ventana.register_shape("arrow down.gif")
ventana.register_shape("arrow up.gif")
ventana.register_shape("arrow left.gif")
ventana.register_shape("arrow right.gif")
#proyectiles verdes sprites
ventana.register_shape("green arrow left.gif")
ventana.register_shape("green arrow right.gif")
ventana.register_shape("green arrow up.gif")
ventana.register_shape("green arrow down.gif")

#escudo sprites
ventana.register_shape("shield_left.gif")
ventana.register_shape("shield right.gif")
ventana.register_shape("shield up.gif")
ventana.register_shape("shield down.gif")

#sprites barra de vida
# de nuevo no se uso al final

#health bar
#al final no se uso, puto turtle de mrd y sus limitaciones

#escudo
escudo = tl.Turtle()
escudo.penup()
escudo.shape("shield_left.gif")
# declaracion de proyectiles

# --- proyectil 1 ---
flecha1 = tl.Turtle()
flecha1.penup()
flecha1.speed(0)
flecha1.goto(1400,0)
flecha1.shape("arrow left.gif")

# --- proyectil 2 ---
#ivan a aver varias flechas en la pantalla al mismo tiempo pero turtle est MUY limitado

def restar_vida():
    global vida
    vida = vida - 1

#ciclo de ataque flecha 1
def flecha_1():
    global vida
    global shield_pos
    estado = rd.choice(estados_posibles)
    ubicacion = rd.choice(ataques_posibles)
    if ubicacion  == "right":
        if estado == "rojo":
            flecha1.shape("arrow left.gif")
        if estado == "verde":
            flecha1.shape("green arrow left.gif")
        flecha1.goto(900,0)
        flecha1.speed(velocidad_proyectiles)
        flecha1.towards(alma_player)
        angulo = flecha1.towards(alma_player)
        flecha1.seth(angulo)
        flecha1.fd(900)

    elif ubicacion  == "left":
        if estado == "rojo":
            flecha1.shape("arrow right.gif")
        if estado == "verde":
            flecha1.shape("green arrow right.gif")
        flecha1.goto(-900,0)
        flecha1.speed(velocidad_proyectiles)
        flecha1.towards(alma_player)
        angulo = flecha1.towards(alma_player)
        flecha1.seth(angulo)
        flecha1.fd(900)

    elif ubicacion  == "up":
        if estado == "rojo":
            flecha1.shape("arrow down.gif")
        if estado == "verde":
            flecha1.shape("green arrow down.gif")
        flecha1.goto(0,650)
        flecha1.speed(velocidad_proyectiles - 1)
        flecha1.towards(alma_player)
        angulo = flecha1.towards(alma_player)
        flecha1.seth(angulo)
        flecha1.fd(650)

    elif ubicacion  == "down":
        if estado == "rojo":
            flecha1.shape("arrow up.gif")
        if estado == "verde":
            flecha1.shape("green arrow up.gif")
        flecha1.goto(0,-650)
        flecha1.speed(velocidad_proyectiles - 1)
        angulo = flecha1.towards(alma_player)
        flecha1.seth(angulo)
        flecha1.fd(650)

    if flecha1.distance(alma_player) < 25:
        flecha1.speed(0)
        flecha1.goto(2000,2000)
        if shield_pos != ubicacion:
            if estado == "rojo":
                alma_player.shape("alma verde rota.gif")
                ventana.ontimer(ventana.bye, 700)
        elif shield_pos == ubicacion:
            if estado == "verde":
                alma_player.shape("alma verde rota.gif")
                ventana.ontimer(ventana.bye, 700)
            
        ventana.ontimer(flecha_1,10)






    
#alma
alma_player = tl.Turtle()
alma_player.penup()
alma_player.shape("alma.gif")
alma_player.shapesize(1)

# reseteo para que no se pueda espamear el escudo tan rapdio almenos no tanto
def reseteo_escudo():
    global can_block
    can_block = True




#controles escudo
def derecha():
    global can_block
    global shield_pos
    if can_block == True:
        can_block = False
        ventana.ontimer(reseteo_escudo, shield_reset)
        shield_pos = "right"
        escudo.shape("shield right.gif")

def izquierda():
     global can_block
     global shield_pos
     if can_block == True:
        can_block = False
        ventana.ontimer(reseteo_escudo, shield_reset)
        shield_pos = "left"
        escudo.shape("shield_left.gif")

def arriba():
    global can_block
    global shield_pos
    if can_block == True:
        can_block = False
        ventana.ontimer(reseteo_escudo, shield_reset)
        shield_pos = "up"
        escudo.shape("shield up.gif")

def abajo():
    global can_block
    global shield_pos
    if can_block == True:
        can_block = False
        ventana.ontimer(reseteo_escudo, shield_reset)
        shield_pos = "down"
        escudo.shape("shield down.gif")


#teclas escudo
ventana.listen()
ventana.onkey(derecha, "d")
ventana.onkey(derecha, "Right")
ventana.onkey(izquierda, "a")
ventana.onkey(izquierda, "Left")
ventana.onkey(arriba, "w")
ventana.onkey(arriba, "Up")
ventana.onkey(abajo, "s")
ventana.onkey(abajo, "Down")


#iniciar con las flechas
ventana.ontimer(flecha_1, 10)



ventana.mainloop()