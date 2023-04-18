from flask import Flask, render_template, request, redirect, url_for, session
from PIL import Image, ImageDraw
import io
from Card import Card
from Table import Table
from Player import Player
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
Function Name: phase

Parameters:
 - file_name : Name of the text file that we want to use to generate a new game (this file has to be put in the " Game_File" folder)
 - session : allow to save the name file between

Returns: 
 - Html file that allow us to choose the phase that we want to play
Description:
    phase allow to choose what phase we want to try
'''
@app.route('/Phases', methods=['GET', 'POST'])
def phase():
    file_name = request.args['file_name']
    file_name = "Game_File\\" + file_name
    session['file_name'] = file_name
    return render_template('Phase.html')
'''
Function Name: phase 3

Parameters:
    
Returns: 
    HTML of the firs Phase
Description:
    Create the first phase

'''
@app.route('/phase3', methods=['GET', 'POST'])
def phase3():
    file_name = session['file_name']
    Table_game = Table([],0,0)
    with open(file_name, "r") as f:
        ligne = f.readline()
        while ligne[:5] != "*** 4":
            mots = ligne.split()
            if mots[0] == "Seat":
                chips_str = mots[3][1:]
                chips = int(chips_str)
                player = Player(mots[2],[],[],chips)
                player.display()
                Table_game.AppendPlayer(player)
            else:
                if ligne[:4] == "Dealt":
                    mots = ligne.split()
                    if mots[2] == "Hero":
                        card1 = Card(int(mots[3][1]),mots[3][2])
                        card2 = Card(int(mots[4][0]),mots[4][1])
                        card3 = Card(int(mots[5][0]),mots[5][1])
                        Table_game.DealtAllCards("Hero",card1)
                        Table_game.DealtAllCards("Hero",card2)
                        Table_game.DealtSeenCards("Hero",card3)
                    else:
                        Table_game.DealtAllCards(mots[2],Card(int(mots[3][1]),mots[3][2]))
            ligne = f.readline()
    Table_game.display()
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