import base64
import os
from flask import Flask, render_template, url_for,request

from extras import randomPalabras

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardar_foto', methods=['POST'])
def guardar_foto():
    image_data = request.json['image']
    # Decodificar la imagen base64 y guardarla en la carpeta 'static'
    try:
        image_data_bytes = base64.b64decode(image_data.split(',')[1])
        # Ruta relativa a la carpeta 'static'
        ruta_guardado = os.path.join(app.root_path, 'static', 'foto.png')
        with open(ruta_guardado, 'wb') as img_file:
            img_file.write(image_data_bytes)
        return 'Foto recibida y guardada correctamente en la carpeta static'
    except Exception as e:
        return f'Error al guardar la foto: {str(e)}'
    
@app.route("/view")
def verFoto():
    palabra =randomPalabras.getWordRandom()
    return render_template("captura.html",palabra = palabra)
        
if __name__ == '__main__':
    app.run(debug=True)
