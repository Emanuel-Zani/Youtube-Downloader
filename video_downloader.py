import tkinter as tk
from tkinter import filedialog
import yt_dlp as youtube_dl

window = tk.Tk()
window.title("Video Downloader")

ancho_ventana = 500
alto_ventana = 350

ancho_pantalla = window.winfo_screenwidth()
alto_pantalla = window.winfo_screenheight()

x = (ancho_pantalla // 2) - (ancho_ventana // 2)
y = (alto_pantalla // 2) - (alto_ventana // 2)

window.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

carpeta_destino = ""

def seleccionar_carpeta():
    global carpeta_destino
    carpeta_destino = filedialog.askdirectory()  
    if carpeta_destino:  
        etiqueta_carpeta.config(text=f"Carpeta seleccionada: {carpeta_destino}")

def descargar():
    url = entrada.get()  
    if url and carpeta_destino:  
        opciones = {
            'format': 'best',  
            'outtmpl': f'{carpeta_destino}/%(title)s.%(ext)s',  
        }
        
        try:
            with youtube_dl.YoutubeDL(opciones) as ydl:
                ydl.download([url])
            resultado.config(text="Descarga completada correctamente!")
        except Exception as e:
            resultado.config(text=f"Error: {e}")
    else:
        resultado.config(text="Por favor, ingresa un URL válido y selecciona una carpeta.")

marco = tk.Frame(window)
marco.pack(expand=True, fill='both')

marco.grid_rowconfigure(0, weight=1)
marco.grid_rowconfigure(1, weight=1)
marco.grid_rowconfigure(2, weight=1)
marco.grid_rowconfigure(3, weight=1)
marco.grid_rowconfigure(4, weight=1)
marco.grid_columnconfigure(0, weight=1)

etiqueta_titulo = tk.Label(marco, text="Introduce el URL del video:")
etiqueta_titulo.grid(row=0, column=0, pady=10)
etiqueta_titulo.config(font=("Helvetica",12))

entrada = tk.Entry(marco, width=50)
entrada.grid(row=1, column=0, pady=10)
entrada.config(font=("Helvetica",12))

boton_carpeta = tk.Button(marco, text="Seleccionar carpeta de destino", command=seleccionar_carpeta)
boton_carpeta.grid(row=2, column=0, pady=10)
boton_carpeta.config(font=("Helvetica",12))
boton_carpeta.config(bg=("#6fcf49"))

etiqueta_carpeta = tk.Label(marco, text="Carpeta no seleccionada")
etiqueta_carpeta.grid(row=3, column=0, pady=10)
etiqueta_carpeta.config(font=("Helvetica",12))

boton = tk.Button(marco, text="Descargar", command=descargar)
boton.grid(row=4, column=0, pady=10)
boton.config(font=("Helvetica", 12))
boton.config(bg=("#6fcf49"))

resultado = tk.Label(marco, text="")
resultado.grid(row=5, column=0, pady=10)
resultado.config(font=("Helvetica",12))

window.mainloop()
