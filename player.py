from pyscript import display, document
#  function name
def display_players(e):
    document.getElementById('output').innerHTML = " "  #  clears previous messages

    # Initialize a counter variable to 0 before the loop starts.
    players = ['Abdullah','Abeleda','Arce','Arias','Bonzon','Cajucom','Catimbang', 'Choi', 'Cotioco','Daradal','Enriquez','Escobar', 'Espina', 'Gano','Garcia','Kaur','Ong','Rufo','Sanchez','Santos','Tan','Vilale','Yao','Zosa']
    count = 1 

    # Used FOR LOOPS iterating over a sequence. example: Lists
    for p in players: 
        display(f"{count}) {p}", target="output")
        count += 1 


