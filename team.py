from pyscript import display, document # type: ignore (quick fix feature)


def team_signup(e):
    document.getElementById('output').innerHTML="" # clears prebvious message
    Online_reg = document.querySelector('input[name="Onlinereg"]:checked').value # checks if it is selected then gets the value
    Med_clear = document.querySelector('input[name="Medclear"]:checked').value # checks if it is selected then gets the value
    Grade = document.getElementById('Grlvl').value # gets the value
    Section = document.getElementById('Section').value # gets the value


    if Online_reg == "yes":
        display("Proceed to the next part", target="output") # the input has two values with two choices. If yes is clicked, this code will occur
    elif Online_reg == "no":
        display("Please fill out the online registration", target="output") # if no is clicked, this code will occur
    if Med_clear == "Yes": 
        display("Proceed to the last part", target="output")# the input has two values with two choices. If yes is clicked, this code will occur
    elif Med_clear == "No":
        display("Please obtain a Medical clearance", target="output")# if no is clicked, this code will occur
   
    if Grade == "7" and Section == "Eme": 
        display("You are Green Hornets!", target="output") # the code will check the values applied in the input and determine if it's fit.
    elif Grade == "7" and Section == "Ruby":
        display("You are Blue Bears!", target="output") 
    elif Grade == "7" and Section == "Sapph":
        display("You are Yellow Tigers!", target="output")
    elif Grade == "7" and Section == "Topaz":
        display("You are Red Bulldogs!", target="output")

    elif Grade == "8" and Section == "Eme":
        display("You are Green Hornets!", target="output")
    elif Grade == "8" and Section == "Ruby":
        display("You are Blue Bears!", target="output")
    elif Grade == "8" and Section == "Sapph":
        display("You are Yellow Tigers!", target="output")
    elif Grade == "8" and Section == "Topaz":
        display("You are Red Bulldogs!", target="output")

    elif Grade == "9" and Section == "Eme":
        display("You are Green Hornets!", target="output")
    elif Grade == "9" and Section == "Ruby":
        display("You are Blue Bears!", target="output")
    elif Grade == "9" and Section == "Sapph":
        display("You are Yellow Tigers!", target="output")
    elif Grade == "9" and Section == "Topaz":
        display("You are Red Bulldogs!", target="output")

    elif Grade == "10" and Section == "Eme":
        display("You are Green Hornets!", target="output")
    elif Grade == "10" and Section == "Ruby":
        display("You are Blue Bears!", target="output")
    elif Grade == "10" and Section == "Sapph":
        display("You are Yellow Tigers!", target="output")
    elif Grade == "10" and Section == "Topaz":
        display("You are Red Bulldogs!", target="output")
    else:
        display("Please select an option!", target="output") # if nothing is selected, this code will occur
   

   

