from pyscript import display, document


def account_creation(e):   # function name
    document.getElementById('output').innerHTML = " "   # clears previous messages

    #gets the values from the ids
    username = document.getElementById('username').value
    password = document.getElementById('pass').value

    # checks to see if username is more than 7 characters to meet the requirements
    if len(username) >= 7: 
        if password.isdigit() or password.isalpha():   # chekcs to see if password contains both numbers and letters
            display(f"your password is too weak. please include both numbers and letters", target="output")
        elif len(password) < 10:    # checks to see if the password is less than 10 chracters (in order to enter you need more than 10 characters)
            display(f"password must be at least 10 characters", target="output")
        else:  #  if all applies, the account is created successfully
            display(f"your account has been created successfully!", target="output")
    else:  # connects to the username, if it doesn't meet the requirements then the else condition will appear
        display(f"your username is too short.", target="output")

