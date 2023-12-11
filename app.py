import os
from flask import Flask, render_template, url_for
import cv2
from extras import randomPalabras

app = Flask(__name__)

def capture_camera():
    cap = cv2.VideoCapture(0)  # Utiliza la cámara por defecto
    if not cap.isOpened():
        return None

    ret, frame = cap.read()
    if ret:
        # Obtén la ruta completa para guardar la imagen en la carpeta 'static'
        ruta_imagen = os.path.join(app.static_folder, 'captura_camara.png')
        cv2.imwrite(ruta_imagen, frame)
        return 'captura_camara.png'

    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capturar')
def capturar():
    imagen = capture_camera()
    palabra = randomPalabras.getWordRandom()
    if imagen:
        return render_template('captura.html', imagen=imagen,palabra=palabra)
    return "No se pudo capturar la imagen"

if __name__ == '__main__':
    app.run()
