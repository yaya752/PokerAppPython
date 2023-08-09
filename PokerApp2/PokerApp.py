#!/usr/bin/env python3

"""! @brief Defines the Endpoints file"""
##
# @mainpage 7 Stud Hi Lo
#
# @section description_MAIN Description
# Project of my internship for my second year in ISIMA for Trinity College Dublin, I had to recreate a game of 7 Stud Hi-Lo and give the different probabilities
#
# @section notes_MAIN Notes
# - It's a python project using flask, it's for running on your own machine not on a server (no database).
#
# @section todo_MAIN TODO
# - Implement a database to make the App useable by many users at the same time.
#
# @section author_MAIN Author
# - Created by Yassine Khiara on 15/04/2023.
# - Modified by Yassine Khiara on 07/08/2023.

##
# @file PokerApp.py
#   
# @brief EndPoints file
#
# @section libraries_PokerApp Libraries/Modules
# - os library (https://docs.python.org/3/library/os.html)
#   - Access to directory creation and delation function.
#   - Access to read file from directory
#
# @section notes_PokerApp Notes
# - If you have a different name than Hero refere to the /name endpoint
#
# @section todo_PokerApp TODO
# - None
#
# Imports
from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
import os

from Playing_game import Summary_Chips ,Average, Generalities, Summary_Hands, Init, Play


# Global Constants
## Definie the specificities of the Flask app, like the folder of the statics files (css files)
app = Flask(__name__, static_folder='static')
## Dictionnary of the allowed files extensions.
ALLOWED_EXTENSIONS = {'txt'}
## Argument of the App run commande, "0.0.0.0" means that the app will run on the public ip and the localhost of the computer
host ="0.0.0.0"
## Debug Mode
debug=True
app.secret_key = "PokerApp"
# Functions
def allowed_file(filename):
    """! Look if the game file has the txt extension.
    @param filename : the file name with the extension
    @return  bool : True if the extension is txt , False otherwise"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
#EndPoint
## Define the main route (first page)
@app.route('/', methods=['GET', 'POST']) 
def upload_file():
    """! Allow to upload a file, it takes the reponse of the POST request to upload the 
    differents save of games to study them.
    @return  The Summary page of all games select is given when games are selected and validated
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
                    new_directory = "./New_File/"
                    os.makedirs(new_directory, exist_ok=True)
                    file.save('./New_File/' + file.filename)
                    session['new'] = True
                    count_file += 1
        if count_file == 0:
            session['new'] = False
        return redirect(url_for('Summary'))
    return render_template('uploads.html')

#EndPoint
## Define the /name route 
@app.route('/name', methods=['GET', 'POST']) # define the name route
def name():
    """! Hiden endpoint, most of the code was made for my tutor so the name will be always the same,
      but if an other person want to use my app he will have to look at this endpoint to match names.
      @return  Store the name of the user in the session
    """
    if request.method == 'POST':
        main_player = request.form['main_player']
        if main_player != 'Hero': 
            main_player = 'Hero'
        session['main_player'] = main_player
        return redirect(url_for('Summary'))
    return render_template('index.html')



#EndPoint
## Define the /Summary route
@app.route('/Summary')
def Summary():
    """! Summaries all the game, if the user didn't upload files it will summarise games of the game_file folder.
   This end point shows the average of chips won/lost during the games, end hand , end amount of chips won/lost by the main player.
   @return Display  the summary of all the games
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
#EndPoint
## Define the /Delete/name_of_the_files_to_delete route
@app.route('/Delete/<filename>')
def delete_file(filename):
    """! As the user has the possibility to add a game he can also delete it.  
     @param filename : the file to delete """
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

#EndPoint
## Define the /Delete/index_of_the_game_to_display route
@app.route('/Play/<int:index>')
def phase(index):
    """! The main endpoint, for each games that are summarise , the user has the possibility to remake the game, 
    it will have access to the game itself, and to the probabilities of each possible hand.

    @param index take the index of the game to display.
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

#EndPoint
## Define the /static route
@app.route('/static/Phase.js')
def phase_js():
    """! js files have to have their own endpoint to be used
    """
    return send_from_directory(app.static_folder, 'Phase.js')
 

if __name__ == '__main__':
    app.run(host = "0.0.0.0",debug = True)
