# Se importan las librerias del sistema, open cv, tesseract y csv
import cv2
import os
import pytesseract
import csv

# se especifica la ruta de instalación de pytesseract
pytesseract.pytesseract.tesseract_cmd = r'D:/tesseract/tesseract'
# Se leen las imagnes desde el directorio que hayamos creado
directorioImagenes = "D:\jtoxqui\Escritorio\Fichas_manual"
# Listas para almacenar los datos de las fichas
datos = []
ficha = []
# Se hace una lista de las imagenes
nombresImgs = os.listdir(directorioImagenes)
# Se imprime la lsita de imagenes
# print(nombresImgs)
# Se colcoa el nombre los atributos que tendrá las columnas
ficha = ['Nombre del archivo', ' , Texto']
# Se agrega
datos.append(ficha)
# Se crea el bucle para leer cada imagen
for nombreImagen in nombresImgs:
    # Se accede a la ruta / nombre de la imagen
    img = directorioImagenes + "/" + nombreImagen
    # Se lee la imagen
    imagen = cv2.imread(img)
    # Se escala
    nuevaImg = cv2.resize(imagen, (1250, 750))
    # Se hace a gris
    nuevaImgGris = cv2.cvtColor(nuevaImg, cv2.COLOR_RGB2GRAY)
    # Se añande un filtro binario
    ret, imgBinaria = cv2.threshold(nuevaImgGris, 127, 255, cv2.THRESH_BINARY)
    # Se estrae la información por cada ficha
    text = img
    text = pytesseract.image_to_string(imgBinaria, lang='spa')
    # Al leer cada ficha, esta leer caracteres innecesarios que se omiten por lo cual se colocan los siguientes: ,:/=%$<>+
    characters = ",:/=%$<>+"
    # Se crear otro bucle para remmplazar esos caracteres por un espacio en blanco.
    for x in range(len(characters)):
        text = text.replace(characters[x], " ")
    # Una vez limpiado, la variable text amamacena primero el nombrel del archivo que se está leyendo para despues concatenar
    # su información extraida
    text = nombreImagen+' , '+text
    # La lista ficha guardará lo que extrajo de la variable text y a esa variable se aplica el método split()
    # para separar el texto en palabras.
    ficha = text.split()
    # La lista datos, guarda la lista ficha.
    datos.append(ficha)
    # Se indica que se almacenó la información
    print("Información almacenada")
    # Se imprime dicha infomación
    print(ficha)

# Se crea el archivo csv con el nombre datos
with open('Reto2A.csv', 'w', newline='') as file:
    # Se determina que por cada lectura de palabra se agregue un ; para delimitar
    writer = csv.writer(file, quoting=csv.QUOTE_ALL, delimiter=';')
    # Finalmente se alamcena la información de todas las fichas.
    writer.writerows(datos)
