from flask import Flask, render_template, request, redirect, url_for, session
from PIL import Image, ImageDraw
import io
import Card
import Table
import Player
import base64
import random


app = Flask(__name__)
app.secret_key = "PokerApp"

'''
Function Name: save

Parameters:
- file_name: name of the file that you want to use ()

Returns: 
- Redirect the user to the page to choose the phase of the game he want to play

Description:
- This function get the file name by using a post method, the file have to be in the Game_File Folder

'''
@app.route('/', methods=['GET', 'POST']) # define the main route (first page)
def save():
    if request.method == 'POST':
        file_name = request.form['file_name']
        
        return redirect(url_for('phase', file_name=file_name))
    return render_template('save.html')

'''
Function Name:

Parameters:

Returns: 

Description:

'''
@app.route('/Phases', methods=['GET', 'POST'])
def phase():
    file_name = request.args['file_name']
    file_name = "Game_File\\" + file_name
    session['file_name'] = file_name
    return render_template('Phase.html')
'''
Function Name:

Parameters:

Returns: 

Description:

'''
@app.route('/phase3', methods=['GET', 'POST'])
def phase3():
    file_name = session['file_name']
    Table_game = Table()
    
    print(3)
    print(file_name)
    with open(file_name, "r") as f:
        for ligne in f:
            if ligne[:4] == "Seat":
                mots = ligne.split()
                for mot in mots:
                    print(mot)
    session['Table'] = Table_game
    return render_template('Phase.html')

@app.route('/phase4', methods=['GET', 'POST'])
def phase4():
    
    print(4)
    return render_template('Phase.html')

@app.route('/phase5', methods=['GET', 'POST'])
def phase5():
    
    print(5)
    return render_template('Phase.html')

@app.route('/phase6', methods=['GET', 'POST'])
def phase6():
    
    print(6)
    return render_template('Phase.html')

@app.route('/phase7', methods=['GET', 'POST'])
def phase7():

    print(7)
    return render_template('Phase.html')
@app.route('/Summary', methods=['GET', 'POST'])
def phaseS():
    print("s")
    return render_template('Phase.html')
'''
Function Name:

Parameters:

Returns: 

Description:

'''

@app.route('/Poker', methods=['GET', 'POST'])
def poker_table():
    file_name = request.args['file_name']
    file_name = "Game_File\\" + file_name
    # Background image
    width, height = 800, 600
    im = Image.new('RGB', (width, height), (0, 0, 0))
    
    # Ddraw the shape of table
    draw = ImageDraw.Draw(im)
    draw.ellipse((width/4, height/4, width*3/4, height*3/4), fill=(0, 255, 0))
    
    # Convert  PNG image and encoded it in base64
    img_bytes = io.BytesIO()
    im.save(img_bytes, format='PNG')
    img_data = base64.b64encode(img_bytes.getvalue()).decode('ascii')
    with open(file_name, "r") as f:
        for ligne in f:
            mots = ligne.split()
            for mot in mots:
                print(mot)
    return render_template('Main.html', img_data=img_data)

if __name__ == '__main__':
    app.run(debug=True)