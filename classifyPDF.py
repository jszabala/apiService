from pdf2image import convert_from_path # pdf2image: Esta librería nos permitirá transformar el pdf en imagenes (No es lo único que hace, pero eso la usaremos)
from PyPDF2 import PdfFileReader
import pytesseract # Esta librería nos permite usar Tesseract desde python, así que podremos identificar texto en una imagen.
import os
import shutil # Para mover los pdf UwU
import time # Para tomar los tiempos de ejecución
import re
from datetime import datetime, date # Para los tiempos de los logs

mensajeFinal = ""
print("ejecutando_python")
# Estos son los directorios que manejaremos, si se desean agregar categorias, deben crear una nueva key:
directorios = {
    "pdfs":os.path.dirname(os.path.abspath(__file__))+"/../pdfs", # Carpeta general de los pdfs

    "categorias":{
        # Si se desea agregar una nueva categoría, se debe agregar la siguiente linea: 
        # "(Nombre key)":os.path.dirname(os.path.abspath(__file__))+"\\categorias\\(Nombre carpeta)",
        # Donde, (Nombre key) es la referencia a ese directorio y (Nombre carpeta) es el nombre de la categoría que se desea añadir.
        # Se debe aseguras que el (Nombre carpeta) que se puso, exista dentro de categorias y esté escrito correctamente
        "factura":os.path.dirname(os.path.abspath(__file__))+"/../categorias/Facturas",
        "factuCre":os.path.dirname(os.path.abspath(__file__))+"/../categorias/Facturas_credito", 
        "factuDeb":os.path.dirname(os.path.abspath(__file__))+"/../categorias/Facturas_debito",
        "ordenPed":os.path.dirname(os.path.abspath(__file__))+"/../categorias/Ordenes_de_pedido",
        "ordenRem":os.path.dirname(os.path.abspath(__file__))+"/../categorias/Ordenes_de_remision",
        "epiCrisis":os.path.dirname(os.path.abspath(__file__))+"/../categorias/Epi_crisis",
        "histoCli":os.path.dirname(os.path.abspath(__file__))+"/../categorias/Historias_clinicas",
        "otro":os.path.dirname(os.path.abspath(__file__))+"/../categorias/Sin_clasificar",
        "vacio":os.path.dirname(os.path.abspath(__file__))+"/../categorias/Vacios"
    },

    "images":os.path.dirname(os.path.abspath(__file__))+"/images", # Carpeta donde se generará la imagen temporal en caso de necesitarlo.
    "logs":os.path.dirname(os.path.abspath(__file__))+"/logs"
}

lista_pdfs = os.listdir(directorios["pdfs"]) # Lista con los nombres de los archivos.

if lista_pdfs:
    mensajeFinal += "("+str(datetime.now())[:-7]+") EMPEZANDO EL PROCESO: \n\n"
    for doc in lista_pdfs:
        try:
            if doc.split(".")[-1] == "pdf": # Esto comprueba si el documento es formato pdf, esto se puede cambiar/reemplazar/eliminar si se requiere

                inicio = time.time() # Inicio toma del tiempo.

                rutaPDF = directorios["pdfs"]+'/'+doc # Ruta del pdf.
                archivo = open(rutaPDF, 'rb')
                texto = PdfFileReader(archivo).getPage(0).extractText().lower() # Esto guardará en texto cualquier texto que pueda haber en la página 1 del pdf, y lo convierte a minusculas.
                archivo.close()

                mensajeFinal += "("+str(datetime.now())[:-7]+") Detectando tipo de contenido del pdf: "+doc+"...\n"
                if not texto: # Evalua si texto viene vacío, en caso de venir vacío, debe evaluarlo como imagen:
                    images = convert_from_path(rutaPDF, last_page=1) # Rescata la página 1 del pdf
                    images[0].save(directorios["images"]+'/page0.jpg', 'JPEG')
                    texto = pytesseract.image_to_string(directorios["images"]+"/page0.jpg").lower() # Esto guarda en texto el texto analizado en la imagen.
                    
                if texto: # Revisa finalmente que texto tenga contenido

                    if re.search('(factura)', texto):

                        if re.search('(factura cr.dito)', texto):
                            # Mover a la carpeta de Facturas credito
                            shutil.move(rutaPDF, directorios["categorias"]["factuCre"]+"/"+doc)
                            mensajeFinal += "("+str(datetime.now())[:-7]+") El archivo "+doc+" se movio a la ruta: "+directorios["categorias"]["factuCre"]+" (Tiempo: "+str(round(time.time()-inicio, 2))+" segundo/s)\n"
                        
                        elif re.search('(factura d.bito)', texto):
                            # Mover a la carpeta de Facturas debito
                            shutil.move(rutaPDF, directorios["categorias"]["factuDeb"]+"/"+doc)
                            mensajeFinal += "("+str(datetime.now())[:-7]+") El archivo "+doc+" se movio a la ruta: "+directorios["categorias"]["factuDeb"]+" (Tiempo: "+str(round(time.time()-inicio, 2))+" segundo/s)\n"

                        else:
                            # Mover a la carpeta de Facturas
                            shutil.move(rutaPDF, directorios["categorias"]["factura"]+"/"+doc)
                            mensajeFinal += "("+str(datetime.now())[:-7]+") El archivo "+doc+" se movio a la ruta: "+directorios["categorias"]["factura"]+" (Tiempo: "+str(round(time.time()-inicio, 2))+" segundo/s)\n"

                    elif "orden de pedido" in texto:
                        # Mover a la carpeta de facturas
                        shutil.move(rutaPDF, directorios["categorias"]["ordenPed"]+"/"+doc)
                        mensajeFinal += "("+str(datetime.now())[:-7]+") El archivo "+doc+" se movio a la ruta: "+directorios["categorias"]["ordenPed"]+" (Tiempo: "+str(round(time.time()-inicio, 2))+" segundo/s)\n"

                    elif "epi crisis" in texto:
                        # Mover a la carpeta de facturas
                        shutil.move(rutaPDF, directorios["categorias"]["epiCrisis"]+"/"+doc)
                        mensajeFinal += "("+str(datetime.now())[:-7]+") El archivo "+doc+" se movio a la ruta: "+directorios["categorias"]["epiCrisis"]+" (Tiempo: "+str(round(time.time()-inicio, 2))+" segundo/s)\n"

                    elif re.search('(historia cl.nica)', texto):
                        # Mover a la carpeta de facturas
                        shutil.move(rutaPDF, directorios["categorias"]["histoCli"]+"/"+doc)
                        mensajeFinal += "("+str(datetime.now())[:-7]+") El archivo "+doc+" se movio a la ruta: "+directorios["categorias"]["histoCli"]+" (Tiempo: "+str(round(time.time()-inicio, 2))+" segundo/s)\n"

                    else:
                        # En caso de no identificar a qué pertenese
                        shutil.move(rutaPDF, directorios["categorias"]["otro"]+"/"+doc)
                        mensajeFinal += "("+str(datetime.now())[:-7]+") El archivo "+doc+" se movio a la ruta: "+directorios["categorias"]["otro"]+" (Tiempo: "+str(round(time.time()-inicio, 2))+" segundo/s)\n"

                else:
                    # Mover a la carpeta de vacios, en caso de que no se haya detectado texto de ninguna de las dos formas
                    shutil.move(rutaPDF, directorios["categorias"]["vacio"]+"/"+doc)
                    mensajeFinal += "("+str(datetime.now())[:-7]+") No se identificó texto en el archivo "+doc+" se movio a la ruta: "+directorios["categorias"]["vacio"]+" (Tiempo: "+round(time.time()-inicio, 2)+" segundo/s)\n"
        
            else:
               mensajeFinal += "("+str(datetime.now())[:-7]+") El archivo "+doc+" no es extensión '.pdf'.\n"

        except Exception as e:
            mensajeFinal += "("+str(datetime.now())[:-7]+") Error: "+str(e)+"\n"
    
    os.remove(directorios["images"]+"/page0.jpg")

else: 
    mensajeFinal += "("+str(datetime.now())[:-7]+") Carpeta general vacía, no hay nada que mover."

fecha = date.today() # Obtiene fecha de hoy
agno = str(fecha.year) # Año actual
mes = str(fecha.month) # Mes actual

listaLogs = os.listdir(directorios["logs"]) # Lista con los logs que existan

if "log-"+agno+"-"+mes+".txt" in listaLogs: # En caso de que el archivo ya exista.
    # Adicionar contenido
    log = open(directorios["logs"]+"/log-"+agno+"-"+mes+".txt", 'a') # Abre el archivo en método Append, es decir, en caso de dar el método .write(text), adiciona el texto al final.
    after = "\n\n"
else:
    # Empezar a escribir
    log = open(directorios["logs"]+"/log-"+agno+"-"+mes+".txt", 'w') # Abre el archivo en método Write, es decir, reemplaza el contenido a la hora de usar .write(text), pero en estes caso, creará el archivo.
    after = ""

log.write(after+mensajeFinal) # Escribe en el archivo, esto no cambia a pesar de abrirlo como Append o Write
log.close() # Cierra el log

# Mensaje para el desarrollador
print("Finalizado.")