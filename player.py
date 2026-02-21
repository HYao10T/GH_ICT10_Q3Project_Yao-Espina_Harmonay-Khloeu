from pyscript import display, document

def display_players(e):
    document.getElementById('output').innerHTML = " "

    players = ['Abdullah','Abeleda','Arce','Arias','Bonzon','Cajucom','Catimbang', 'Choi', 'Cotioco','Daradal','Enriquez','Escobar', 'Espina', 'Gano','Garcia','Kaur','Ong','Rufo','Sanchez','Santos','Tan','Vilale','Yao','Zosa']

    for p in players: 
        display(f"-{p}", target="output")
