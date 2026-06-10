import random as rd
import turtle as tl
from playsound3 import playsound as ps
import sys

lista_bloques = []
lista_pinchos = []
lista_bloques_v = []
lista_pinchos_vn = []
lista_pinchos_vb = []

juego_iniciado = False
bloques_v_estado = False
pinchos_vn_estado = False
pinchos_vb_estado = False
brillo_fondo = 15
distancia = 64
can_key = True
timing_bloques = 900
timing_pinchos = 650
timing_pinchos_vb = 1500


tl.colormode(225)

ventana = tl.Screen()


ventana.bgcolor(0.05,0,0.15)
ventana.setup(1300,700)
#fondo arcoiris

def dibujar_cuadro_inicio():
    # Usamos meta temporalmente para escribir el texto de inicio
    meta.penup()
    meta.goto(0, 50)
    meta.pencolor("white")
    meta.write("¡BIENVENIDO AL JUEGO!", align="center", font=("Arial", 24, "bold"))
    
    meta.goto(0, -20)
    meta.write("Presiona ENTER para comenzar...", align="center", font=("Arial", 16, "normal"))
    meta.goto(-256, 64) # Regresa la meta a su posición original de juego

def comenzar_juego():
    global juego_iniciado
    if juego_iniciado == False:
        juego_iniciado = True
        meta.clear() # Borra el texto de bienvenida que escribió meta
        
        # Arranca todo el juego
        mapa1()
        ciclo_bloques_v()
        ciclo_pinchos_vn()
        ciclo_pinchos_vb()
        musik_loop()
def ciclo_bloques_v():
    global bloques_v_estado
    if bloques_v_estado == False:
        for v in lista_bloques_v:
            v.shape("bloque.gif")
    elif bloques_v_estado == True:
        for v in lista_bloques_v:
            v.shape("inactivo.gif")
    if bloques_v_estado == True:
        bloques_v_estado = False
    else:
        bloques_v_estado = True
    ventana.ontimer(ciclo_bloques_v, timing_bloques)
       
def ciclo_pinchos_vn():
    global pinchos_vn_estado
    if pinchos_vn_estado == False:
        for v in lista_pinchos_vn:
            v.shape("pinchos.gif")
    elif pinchos_vn_estado == True:
        for v in lista_pinchos_vn:
            v.shape("inactivo.gif")
    if pinchos_vn_estado == True:
        pinchos_vn_estado = False
    else:
        pinchos_vn_estado = True
    ventana.ontimer(ciclo_pinchos_vn, timing_pinchos)


def ciclo_pinchos_vb():
    global pinchos_vb_estado
    if pinchos_vb_estado == False:
        for v in lista_pinchos_vb:
            v.shape("pinchos.gif")
    elif pinchos_vb_estado == True:
        for v in lista_pinchos_vb:
            v.shape("bloque.gif")
    if pinchos_vb_estado == True:
        pinchos_vb_estado = False
    else:
        pinchos_vb_estado = True
    ventana.ontimer(ciclo_pinchos_vb, timing_pinchos_vb)

#rastro rgb


#sprites
#----el prota-----#
ventana.register_shape("prota.gif")
ventana.register_shape("prota muerto.gif")
ventana.register_shape("prota dash.gif")

#----el bloque----#
ventana.register_shape("bloque.gif")

#----- el pincho-----#
ventana.register_shape("pinchos.gif")

#------ bloque variable -------#
ventana.register_shape("inactivo.gif")

#------- LA META (br ba) --------#
ventana.register_shape("meta.gif")





def mapa1():
    #---declaracion del bloque----#
    bloque = tl.Turtle()
    bloque.shape("bloque.gif")
    bloque.penup()
    bloque.speed(0)
    lista_bloques.append(bloque)

    # -----constructor del mapa 1-------
    #===== cubo pt 1 ======#
    bloque.bk(64)
    distancia = 0
    for f in range(3):
        f = bloque.clone()
        f.seth(270)
        f.fd(distancia)
        distancia = distancia + 64
        lista_bloques.append(f)
    
    #===== cubo pt 2 ======#
    distancia = 0
    bloque.seth(270)
    bloque.fd(192)
    bloque.seth(0)
    for f in range(4):
        f = bloque.clone()
        f.fd(distancia)
        distancia = distancia + 64
        lista_bloques.append(f)

    #===== cubo pt 3 ======#    
    bloque.fd(256)
    bloque.seth(90)
    r = bloque.clone()
    lista_bloques.append(r)
    bloque.fd(128)
    
    #===== cubo pt 4 ======#
    distancia = 0
    for f in range(4):
        f = bloque.clone()
        f.fd(distancia)
        distancia = distancia + 64
        lista_bloques.append(f)

    #===== cubo pt 5 ======#    
    distancia = 0
    bloque.fd(256)
    bloque.seth(180)
    for f in range(6):
        f = bloque.clone()
        f.fd(distancia)
        distancia = distancia + 64
        lista_bloques.append(f)
    
    #===== cubo pt 6 ======#
    bloque.goto(0,0)
    bloque.seth(0)
    bloque.fd(128)
    bloquesito = bloque.clone()
    lista_bloques.append(bloquesito)
    
    #===== cubo pt 7 ======#
    bloque.goto(-192,192)
    bloque.seth(270)
    distancia = 0
    for f in range(9):
        f = bloque.clone()
        f.fd(distancia)
        distancia = distancia + 64
        lista_bloques.append(f)
    
    #===== cubo pt 8 ======#
    distancia = 0
    bloque.goto(-128,-320)
    bloque.seth(0)
    for f in range(12):
        f = bloque.clone()
        f.fd(distancia)
        distancia = distancia + 64
        lista_bloques.append(f)

    #===== cubo pt 9 ======#
    distancia = 0
    bloque.goto(576,-192)
    bloque.seth(90)
    for f in range(9):
        f = bloque.clone()
        f.fd(distancia)
        distancia = distancia + 64
        lista_bloques.append(f)
    
    #===== cubo pt 10 ======#
    distancia = 0
    bloque.goto(448,-192)
    bloque.seth(180)
    for f in range(4):
        f = bloque.clone()
        f.fd(distancia)
        lista_bloques.append(f)
        distancia = distancia + 64
    
    #===== cubo pt 11 ======#
    distancia = 0
    bloque.seth(90)
    for f in range(7):
        f = bloque.clone()
        f.fd(distancia)
        distancia = distancia + 64
        lista_bloques.append(f)

    #===== cubo pt 12 ======#
    distancia = 0
    bloque.goto(640,320)
    bloque.seth(180)
    bloque.fd(128)

    tung = bloque.clone()
    lista_bloques.append(tung)
    tung2 = tung.clone()
    tung2.seth(180)
    tung2.fd(64)
    #===== cubo pt 13 ======#
    distancia = 0
    tung3 = tung2.clone()
    tung3.seth(180)
    tung3.fd(128)
    for f in range(15):
        f = tung3.clone()
        f.fd(distancia)
        lista_bloques.append(f)
        distancia = distancia + 64
    #===== cubo pt 14 ======#
    distancia = 0
    tung3.fd(896)
    tung3.seth(270)
    tung3.fd(128)
    for f in range(9):
        f = tung3.clone()
        f.fd(distancia)
        distancia =  distancia + 64
        lista_bloques.append(f)

    #====== cubo 15 =====#
    distancia = 0
    tung3.fd(512)
    tung3.seth(0)
    for f in range(6):
        f = tung3.clone()
        f.fd(distancia)
        distancia = distancia + 64
        lista_bloques.append(f)

    #====== cubo 16 ====#
    tung4 = tung3.clone()
    tung4.goto(-256,192)
    lista_bloques.append(tung4)
    tung4.seth(180)
    distancia = 0
    for f in range(4):
        f = tung4.clone()
        f.fd(distancia)
        distancia = distancia + 64
        lista_bloques.append(f)

    #====== culo 17 ====#
    distancia = 0
    tung5 = tung4.clone()
    tung5.seth(180)
    tung5.fd(192)
    tung5.seth(270)
    for f in range(7):
        f = tung5.clone()
        f.fd(distancia)
        distancia = distancia + 64
        lista_bloques.append(f)

    #====== cul0wo  18====#
    distancia = 0
    tung5.fd(384)
    tung5.seth(0)
    for f in range(3):
        f = tung5.clone()
        f.fd(distancia)
        distancia = distancia + 64
        lista_bloques.append(f)
    # ----- declaracion pinchos-------#
    #===== pincho pt 1  ======#
    pincho = tl.Turtle()
    pincho.shape("pinchos.gif")
    pincho.penup()
    pincho.speed(0)
    lista_pinchos.append(pincho)
    pincho.fd(128)
    pincho.seth(270)
    pincho.fd(64)
    pincho.seth(0)

    #===== pincho pt 2  ======#
    p = pincho.clone()
    lista_pinchos.append(p)
    pincho.bk(64)
    p2 = pincho.clone()
    lista_pinchos.append(p2)

    #===== pincho pt 3  ======#
    pincho.goto(-128,128)
    pincho.seth(0)
    distance = 0
    for p in range(3):
        p = pincho.clone()
        p.fd(distance)
        distance = distance + 64
        lista_pinchos.append(p)

    #===== pincho pt 4 ======#
    piji = pincho.clone()
    piji.goto(384,320)
    lista_pinchos.append(piji)


    # ----- bloque variable declaracion -----#
    #===== bloque v pt 1  ======#
    bloque_v = tl.Turtle()
    bloque_v.shape("inactivo.gif")
    bloque_v.speed(0)
    bloque_v.penup()
    bloque_v.goto(192,-128)
    lista_bloques_v.append(bloque_v)
    
    #===== bloque v pt 2  ======#
    v = bloque_v.clone()
    lista_bloques_v.append(v)
    
    #===== bloque v pt 3  ======#
    v2 = bloque_v.clone()
    v2.goto(-64,64)
    lista_bloques_v.append(v2)

    #====== bloque v pt 4 =======#
    v69 = v2.clone()
    v69.goto(384,128)
    lista_bloques_v.append(v69)
    

    #========pinchos variables/nada======#
    #===== pinchos vn pt 1  ======#
    pincho_vn = tl.Turtle()
    pincho_vn.shape("inactivo.gif")
    pincho_vn.speed(0)
    pincho_vn.penup()
    pincho_vn.goto(-128,-128)
    lista_pinchos_vn.append(pincho_vn)
    vn4 = pincho_vn.clone()
    vn4.goto(256,0)
    lista_pinchos_vn.append(vn4)

    distancia = 0
    for pinga in range(3):
        pinga = vn4.clone()
        pinga.fd(distancia)
        distancia = distancia + 64
        lista_pinchos_vn.append(pinga)

    #===== pinchos vn pt 2  ======#
    vn67 = pincho_vn.clone()
    vn67.goto(512,192)
    lista_pinchos_vn.append(vn67)

    # ====== pinchos vn pt3 ======#
    rappi = vn67.clone()
    rappi.goto(192,256)
    lista_pinchos_vn.append(rappi)

    #======= pinchos vn pt4 =====#
    rappi2 = rappi.clone()
    rappi2.seth(180)
    rappi2.fd(384)
    lista_pinchos_vn.append(rappi2)

    #====pinchos ya casito acabo ======#
    rappi3 = rappi2.clone()
    rappi3.goto(-320,64)
    lista_pinchos_vn.append(rappi3)

    #===== acabe ======#
    rappi4 = rappi3.clone()
    rappi4.goto(-512,0)
    lista_pinchos_vn.append(rappi4)


    #-------pinchos variables/bloque-------#
    #===== pinchos vb pt 1  ======#
    pincho_vb = tl.Turtle()
    pincho_vb.shape("bloque.gif")
    pincho_vb.speed(0)
    pincho_vb.penup()
    pincho_vb.goto(576,-256)
    lista_pinchos_vb.append(pincho_vb)
    
    #===== pimchos vb pt2 =====#
    pichita = pincho_vb.clone()
    pichita.goto(-576,256)
    lista_pinchos_vb.append(pichita)

    #=======pinchos vb=======#
    pichota =  pichita.clone()
    pichota.goto(-384,128)
    lista_pinchos_vb.append(pichota)

    #pinchos vb 7w7#
    elimbecil =  pichota.clone()
    elimbecil.goto(-256,0)
    lista_pinchos_vb.append(elimbecil)


 #=====! LA META !=======#
meta = tl.Turtle()
meta.shape("meta.gif")
meta.penup()
meta.speed(0)
meta.goto(-256,64)

dibujar_cuadro_inicio()


#lapiz
lapiz = tl.Turtle()
lapiz.width(5)
lapiz.speed(0)
lapiz.hideturtle()

#-------bloque-----#


#------declaracion prota------#
prota = tl.Turtle()
prota.width(5)
prota.speed(0)
prota.penup()
prota.shape("prota.gif")
lapiz.pencolor(0,0,0)

#------ funcion de movimineto y colision-----3
def avanzar():
    for pichas in lista_pinchos:
        if prota.distance(pichas) < 0.5:
            prota.shape("prota muerto.gif")
            lapiz.clear()
            print("PERDIO")
            sys.stdout.flush()
            ventana.ontimer(ventana.bye, 600)
            return
    for bloques in lista_bloques:
        if prota.distance(bloques) < 0.5:
            ps("crash.wav", block = False)
            prota.bk(64)
            lapiz.bk(64)
            lapiz.clear()
            prota.shape("prota.gif")
            return
    for bloquesv in lista_bloques_v:
        if prota.distance(bloquesv) < 0.5 and bloques_v_estado == True:
            prota.bk(64)
            lapiz.bk(64)
            lapiz.clear()
            prota.shape("prota.gif")
            return
    for pinchosv in lista_pinchos_vn:
        if prota.distance(pinchosv) < 0.5 and pinchos_vn_estado == True:
            prota.shape("prota muerto.gif")
            lapiz.clear()
            print("PERDIO")
            sys.stdout.flush()
            ventana.ontimer(ventana.bye, 600)
            return
         
    for pinchosb in lista_pinchos_vb:
        if prota.distance(pinchosb) < 0.5 and pinchos_vb_estado == True:
            prota.shape("prota muerto.gif")
            lapiz.clear()
            print("PERDIO")
            sys.stdout.flush()
            ventana.ontimer(ventana.bye, 600)
            return
        elif prota.distance(pinchosb) < 0.5 and pinchos_vb_estado == False:
            ps("crash.wav", block = False)
            prota.bk(64)
            lapiz.bk(64)
            lapiz.clear()
            prota.shape("prota.gif")
            return
    

    if prota.distance(meta) < 0.5:
            print("GANO")
            sys.stdout.flush()
            ventana.ontimer(ventana.bye, 750)
    prota.fd(64)
    lapiz.fd(64)
    
    avanzar()



def reseteo_teclas():
    global can_key
    can_key = True


#-------movimiento------#
def right():
    global can_key
    if can_key ==True:
        ps("move.wav", block = False)
        can_key = False
        prota.seth(0)
        lapiz.seth(0)
        prota.shape("prota dash.gif")
        avanzar()
        ventana.ontimer(reseteo_teclas, 75)

def up():
    global can_key
    if can_key ==True:
        ps("move.wav", block = False)
        can_key = False
        prota.seth(90)
        lapiz.seth(90)
        prota.shape("prota dash.gif")
        avanzar()
        ventana.ontimer(reseteo_teclas, 75)


def left():
    global can_key
    if can_key ==True:
        ps("move.wav", block = False)
        can_key = False
        prota.seth(180)
        lapiz.seth(180)
        prota.shape("prota dash.gif")
        avanzar()
        ventana.ontimer(reseteo_teclas, 75)


def down():
    global can_key
    if can_key ==True:
        ps("move.wav", block = False)
        can_key = False
        prota.seth(270)
        lapiz.seth(270)
        prota.shape("prota dash.gif")
        avanzar()
        ventana.ontimer(reseteo_teclas, 75)

#--------controles--------#

#musikita
def musik_loop():
    ps("Musik.wav", block = False)
    ventana.ontimer(musik_loop, 175600)
musik_loop()
ventana.listen()

ventana.onkey(comenzar_juego, "Return")     

ventana.onkey(right,"d")
ventana.onkey(up,"w")
ventana.onkey(left,"a")
ventana.onkey(down,"s")




ventana.mainloop()
