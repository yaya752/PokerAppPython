
##
# @mainpage 7 Stud Hi Lo
#
# @section description_PokerApp Description
# Project for Trinty College Dublin, I had to recreate a game of 7 Stud Hi-Lo and give the different probability
#
# @section notes_main Notes
# - it's a pyhton project using flask, it's for running on your own machine not on a server (no database)
#
##
# @file PokerApp.py
#
# @brief Python Project for Trinity Colege Dublin
#
# @section description_PokerApp Description
# Python Project for Trinity Colege Dublin
#
# @section libraries_main Libraries/Modules
# - os library (https://docs.python.org/3/library/os.html)
#   - Access to directory creation and delation function.
#   - Access to read file from directory
#
# @section notes_doxygen_example Notes
# - Comments are Doxygen compatible.
#
# @section todo_doxygen_example TODO
# - None.
#
# @section author_doxygen_example Author(s)
# - Created by Yassine Khiara on 04/08/2023.
# - Modified by John Woolsey on 04/08/2023.

# Imports

from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
import os

from Playing_game import Summary_Chips ,Average, Generalities, Summary_Hands, Init, Play, Max_Bet
from Odds import Table
# Functions
Table()
app = Flask(__name__, static_folder='static')

app.secret_key = "PokerApp"

ALLOWED_EXTENSIONS = {'txt'}

def allowed_file(filename):
    """! Look if the game file has the txt extension"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST']) # define the main route (first page)
def upload_file():
    """! Sets the temperature unit.
    @param unit  The temperature unit ("F", "C", or "K"),
            defaults to "F" if a valid unit is not provided.
    """
    if request.method == 'POST':
        uploaded_files = request.files.getlist('files')
        count_file = 0
        session['main_player'] = 'Hero'
        for file in uploaded_files:
            if file.filename =='' :
                session['new'] = False  
            else:
                if allowed_file(file.filename):
                    new_directory = "./New_File"
                    os.makedirs(new_directory, exist_ok=True)
                    file.save('./New_File/' + file.filename)
                    session['new'] = True
                    count_file += 1
        if count_file == 0:
            session['new'] = False
        return redirect(url_for('Summary'))
    return render_template('uploads.html')
@app.route('/save', methods=['GET', 'POST']) # define the main route (first page)
def save():
    """! Sets the temperature unit.
    @param unit  The temperature unit ("F", "C", or "K"),
            defaults to "F" if a valid unit is not provided.
    """
    if request.method == 'POST':
        file_name = request.form['file_name']
        main_player = request.form['main_player']
        return redirect(url_for('phase', file_name=file_name, main_player=main_player))
    return render_template('save.html')

@app.route('/name', methods=['GET', 'POST']) # define the main route (first page)
def index():
    """! Sets the temperature unit.
    @param unit  The temperature unit ("F", "C", or "K"),
            defaults to "F" if a valid unit is not provided.
    """
    if request.method == 'POST':
        main_player = request.form['main_player']
        if main_player != 'Hero': 
            main_player = 'Hero'
        session['main_player'] = main_player
        return redirect(url_for('Summary'))
    return render_template('index.html')




@app.route('/Summary')
def Summary():
    """! Sets the temperature unit.
    @param unit  The temperature unit ("F", "C", or "K"),
            defaults to "F" if a valid unit is not provided.
    """
    if session['new']:
        path = './New_File/'
    else:
        path = './Game_File/'
    uploads_dir = os.path.join(app.root_path, path)
    files = os.listdir(uploads_dir)
    session['files'] = files
    session['path'] = path
    main_player = session['main_player']
    
    summary_table = []
    first_lines = []
    generalities_list = []
    hand_table = []
    for f in files:
        Chips = Summary_Chips(f,main_player,path)
        if Chips != -1:
            summary_table.append(Summary_Chips(f,main_player,path))
            hand_table.append(Summary_Hands(f,main_player,path) )  
            with open(path + f, "r") as f:
                line = f.readline()
                
                first_lines.append(line.strip())
                generalities_list.append(Generalities(line.strip()))
        else:
            summary_table.append(-1)
            hand_table.append([])
            generalities_list.append([[],[],[]])
    mean = round(Average(summary_table),2)
    if session['new']:
        return render_template('summary.html',files=files,first_lines = first_lines,hand_table = hand_table, generalities_list = generalities_list ,summary_table = summary_table, main_player = main_player, mean = mean)
    else:
        return render_template('summary_game.html',files=files,first_lines = first_lines,hand_table = hand_table, generalities_list = generalities_list ,summary_table = summary_table, main_player = main_player, mean = mean)

@app.route('/Delete/<filename>')
def delete_file(filename):
    path = session['path']
    if path != "./Game_File/":
        file_path = os.path.join(path, filename)
        os.remove(file_path)
        uploads_dir = os.path.join(app.root_path, path)
        files = os.listdir(uploads_dir)
        if len(files) == 0:
            return redirect(url_for('upload_file'))
        else:
            return redirect(url_for('Summary'))
    else:
        return redirect(url_for('Summary'))
'''Function Name: phase

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
    """! Sets the temperature unit.
    @param unit  The temperature unit ("F", "C", or "K"),
            defaults to "F" if a valid unit is not provided.
    """
    files = session['files']
    file_name = files[index]
    main_player = session['main_player']
    session['file_name'] = file_name
    session['main_player'] = main_player
   
    path = session['path'] 
    decision = -1
    (initialisation,list_numplayers,Players) = Init(file_name,path)
    (list_actions,tab_street,decision,maxbet) = Play(file_name,main_player,list_numplayers,path)    
    return render_template('Phase_test.html',list_actions = list_actions,
                          initialisation = initialisation, tab_street = tab_street , decision = decision , maxbet = maxbet)
'''
Function Name: phase 3

Parameters:
     
Returns: 
    HTML of the first Phase, 
Description:
    Create the first phase

'''
@app.route('/static/Phase3.js')
def serve_js():
    """! Sets the temperature unit.
    @param unit  The temperature unit ("F", "C", or "K"),
            defaults to "F" if a valid unit is not provided.
    """
    return send_from_directory(app.static_folder, 'Phase3.js')


@app.route('/static/Phase.js')
def phase_js():
    """! Sets the temperature unit.
    @param unit  The temperature unit ("F", "C", or "K"),
            defaults to "F" if a valid unit is not provided.
    """
    return send_from_directory(app.static_folder, 'Phase.js')
 
@app.route('/Phases/phase3', methods=['GET', 'POST'])
def phase3():
    """! Sets the temperature unit.
    @param unit  The temperature unit ("F", "C", or "K"),
            defaults to "F" if a valid unit is not provided.
    """
    return render_template('Phase3.html')
if __name__ == '__main__':
    app.run(host ="0.0.0.0", debug=True)
