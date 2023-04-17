from flask import Flask, render_template, request, redirect, url_for
from PIL import Image, ImageDraw
import io
import Card
import Table
import Player
import base64
import random


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def save():
    if request.method == 'POST':
        file_name = request.form['file_name']
        return redirect(url_for('poker_table', file_name=file_name))
    return render_template('index.html')
@app.route('/table')
def index():
    # Créer une image de fond
    width, height = 800, 600
    im = Image.new('RGB', (width, height), (0, 0, 0))
    
    # Dessiner un ovale rempli de vert
    draw = ImageDraw.Draw(im)
    draw.ellipse((width/4, height/4, width*3/4, height*3/4), fill=(0, 255, 0))
    
    # Convertir l'image en PNG encodé en base64
    img_bytes = io.BytesIO()
    im.save(img_bytes, format='PNG')
    img_data = base64.b64encode(img_bytes.getvalue()).decode('ascii')
    
    # Renvoyer la page HTML avec l'image de fond et l'ovale centré
    return render_template('Main.html', img_data=img_data)

@app.route('/Poker', methods=['GET', 'POST'])
def poker_table():
    file_name = request.args['file_name']
    with open(file_name, "r") as f:
        for ligne in f:
            mots = ligne.split()
            for mot in mots:
                print(mot)
    return render_template('Main.html')

if __name__ == '__main__':
    app.run(debug=True)