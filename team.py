from pyscript import display, document # type: ignore (quick fix feature)


def team_signup(e):
    document.getElementById('output').innerHTML=""
    Online_reg = document.querySelector('input[name="Onlinereg"]:checked').value
    Med_clear = document.querySelector('input[name="Medclear"]:checked').value
    Grade = document.getElementById('Grlvl').value
    Section = document.getElementById('Section').value


    if Online_reg == "yes":
        display("Proceed to the next part", target="output")
    elif Online_reg == "no":
        display("Please fill out the online registration", target="output")
    if Med_clear == "Yes":
        display("Proceed to the last part", target="output")
    elif Med_clear == "No":
        display("Please obtain a Medical clearance", target="output")
   
    if Grade == "7" and Section == "Eme":
        display("You are Green Hornets!", target="output")
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
        display("Please select an option!", target="output")
   

   
