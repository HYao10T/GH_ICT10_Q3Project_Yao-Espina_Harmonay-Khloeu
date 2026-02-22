from pyscript import display, document

def display_players(e):
    document.getElementById('output').innerHTML = " "

    players = ['Abdullah','Abeleda','Arce','Arias','Bonzon','Cajucom','Catimbang', 'Choi', 'Cotioco','Daradal','Enriquez','Escobar', 'Espina', 'Gano','Garcia','Kaur','Ong','Rufo','Sanchez','Santos','Tan','Vilale','Yao','Zosa']
    count = 1

    for p in players: 
        display(f"{count}) {p}", target="output")
        count += 1

