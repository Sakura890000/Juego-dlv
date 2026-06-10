import tkinter as tk
import random 
from PIL import Image, ImageTk
import os

ventana = tk.Tk()
ventana.title("Silence into the Cave")
ventana.geometry("700x700")
ventana.configure(background="black")
ventana.resizable(False, False)

ventana.iconbitmap("Ico.ico")

pil_imagen = Image.open("titulo.jpg")
imagen_tk = ImageTk.PhotoImage(pil_imagen)
label_imagen = tk.Label(ventana, image=imagen_tk, bg="black").pack()

def inicio():
    ventana.withdraw()
    nueva = tk.Toplevel()
    nueva.title("Menu")
    nueva.geometry("700x700")
    nueva.configure(background="black")

    def nuevojuego():
        nueva.withdraw()
        cont = tk.Toplevel()
        cont.title("Holaaaa")
        cont.geometry("700x700")
        cont.configure(background="blue")
    tk.Button(nueva, text= "Nuevo Juego", command=nuevojuego, font= ("Arial", 16), fg= "white", bg= "#000000", bd=0 ,activebackground="black", activeforeground= "#ffff00").pack()
        
    def volver():
        nueva.destroy()
        ventana.deiconify()
    tk.Button(nueva, text= "volver", command=volver, font= ("Arial", 16), fg= "white", bg= "#000000", bd=0 ,activebackground="black", activeforeground= "#ffff00").pack()


def creditos():
    ventana.withdraw()
    ditos = tk.Toplevel()
    ditos.title("Creditos")
    ditos.geometry("700x700")
    ditos.configure(background="black")

    canvas = tk.Canvas(ditos, bg="black", width=700, height=630, highlightthickness=0)
    canvas.grid(row=0, column=0, columnspan=2)

    texto = """
    Silence into the Cave

    
    Desarrollado por:
    Esteban martines como gay


    
    Kabra como kabra



    Juan Pablo como el Furry Lover



    Juan como Juan



    Duran como Mr_Blandin




    Institución
    Univalle sede Tuluá



    Con Cariño para 
    


    Gracias por jugar :)
    """

    
    credito = canvas.create_text(350, 650, text=texto, fill="white", font=("Arial", 16), justify="center")

    def mover():
        canvas.move(credito, 0, -1) 
        pos = canvas.bbox(credito)  
        if pos and pos[3] > 0:       
            ditos.after(20, mover)   
    mover()

    def volver():
        ditos.destroy()
        ventana.deiconify()
    tk.Button(ditos, text="Volver", command=volver,
               font= ("Arial", 16), fg= "white", bg= "#000000", 
               bd=0 ,activebackground="black", 
               activeforeground= "#ffff00").grid(row=1, column=0, columnspan=2, pady=10)
    

def atras():
    boton_height = 2 
    boton_width = 10
    ventana.withdraw()
    cecil = tk.Toplevel()
    cecil.title("Volver")
    cecil.geometry("1080x720")
    cecil.configure(background="black")
    
    def mover_salir(evento=None):
        alto_boton = boton_salir.winfo_height()
        ancho_boton = boton_salir.winfo_width()
        x = random.randint(0, 1080 - ancho_boton)
        y = random.randint(0, 720 - alto_boton)
        boton_salir.place(x=x, y=y)

    boton_salir = tk.Button(
        cecil, 
        text="Salir", 
        command=mover_salir, 
        bg="black", 
        fg="white", 
        font=("Arial", 12, "bold"), 
        highlightbackground="white", bd=0, 
        activebackground="black",
          activeforeground= "#ffff00"
    )

    boton_salir.place(x=500, y=350)
    

    def volver():
        cecil.destroy(); ventana.deiconify()
    tk.Button(cecil, text="Volver",  command=volver,
               font= ("Arial", 16), fg= "white", 
               bg= "#000000", bd=0, 
               highlightthickness=5,
               activebackground="black", 
               activeforeground= "#ffff00").pack(pady=10)
   


boton_width = 10
boton_height = 4

caja = tk.Frame(ventana, bg= "black", highlightbackground="white", highlightthickness=5)
caja.pack(pady=40, padx=50)


boton_iniciar = tk.Button(caja, text= "- Iniciar",  command= inicio, font= ("Arial", 18), fg="white", bg="#000000",bd=0 ,activebackground="black", activeforeground= "#ffff00")
boton_iniciar.pack(pady= 12,padx=50)

boton_salir = tk.Button(caja, text= "- Salir", command=atras, font= ("Arial", 16), fg="white", bg="#000000", bd=0 ,activebackground="black", activeforeground= "#ffff00")
boton_salir.pack(pady= 12, padx=50)  

boton_creditos = tk.Button(caja, text= "- Creditos", command=creditos, font= ("Arial", 16), fg= "white", bg= "#000000", bd=0 ,activebackground="black", activeforeground= "#ffff00")
boton_creditos.pack(pady= 12,padx= 50) 


ventana.mainloop()