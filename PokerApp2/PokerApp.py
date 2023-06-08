from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
import os

from Playing_game import Summary_Chips ,Average, Generalities, Summary_Hands, Init, Play
from Odds import Table

Table()
app = Flask(__name__, static_folder='static')

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
@app.route('/save', methods=['GET', 'POST']) # define the main route (first page)
def save():
    if request.method == 'POST':
        file_name = request.form['file_name']
        main_player = request.form['main_player']
        return redirect(url_for('phase', file_name=file_name, main_player=main_player))
    return render_template('save.html')

@app.route('/', methods=['GET', 'POST']) # define the main route (first page)
def index():
    if request.method == 'POST':
        main_player = request.form['main_player']
        session['main_player'] = main_player
        return redirect(url_for('Summary'))
    return render_template('index.html')

@app.route('/Summary')
def Summary():
    uploads_dir = os.path.join(app.root_path, 'Game_File\\')
    files = os.listdir(uploads_dir)
    session['files'] = files
    main_player = session['main_player']
    summary_table = []
    first_lines = []
    generalities_list = []
    hand_table = []
    for f in files:
        summary_table.append(Summary_Chips(f,main_player))
        hand_table.append(Summary_Hands(f,main_player) )  
        with open("Game_File\\" + f, "r") as f:
            line = f.readline()
            first_lines.append(line.strip())
            generalities_list.append(Generalities(line.strip()))
    mean = round(Average(summary_table),2)
    return render_template('summary.html',files=files,first_lines = first_lines,hand_table = hand_table, generalities_list = generalities_list ,summary_table = summary_table, main_player = main_player, mean = mean)
'''
Function Name: phase

Parameters:
 - file_name : Name of the text file that we want to use to generate a new game
        (this file has to be put in the " Game_File" folder)
 - session : allow to save the name file between

Returns: 
 - Html file that allow us to choose the phase that we want to play
Description:
    allow to choose what phase we want to try
'''
@app.route('/Play/<int:index>')
def phase(index):
    files = session['files']
    file_name = files[index]
    main_player = session['main_player']
    session['file_name'] = file_name
    session['main_player'] = main_player
    decision = -1
    (initialisation,list_numplayers) = Init(file_name)
    (list_actions,tab_street,decision) = Play(file_name,main_player,list_numplayers)
    print(decision)
    return render_template('Phase.html',list_actions = list_actions,
                          initialisation = initialisation, tab_street = tab_street , decision = decision)
'''
Function Name: phase 3

Parameters:
     
Returns: 
    HTML of the first Phase
Description:
    Create the first phase

'''
@app.route('/static/Phase3.js')
def serve_js():
    return send_from_directory(app.static_folder, 'Phase3.js')


@app.route('/static/Phase.js')
def phase_js():
    return send_from_directory(app.static_folder, 'Phase.js')

@app.route('/Phases/phase3', methods=['GET', 'POST'])
def phase3():
    
    return render_template('Phase3.html')
if __name__ == '__main__':
    app.run(host ="0.0.0.0",debug= True)