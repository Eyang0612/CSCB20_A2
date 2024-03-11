from flask import Flask

app = Flask(__name__)


def simplify_string(string):
    simplified = ""
    for i in string:
        if i.isalpha():
            simplified += i

    return simplified

def propernaming(string):
    propername = ""
    for i in range(len(string)):
        if i == 0:
            propername += string[i].upper()
        else:
            propername += string[i].lower()
    return propername


@app.route("/<username>")
def home(username):
    encrpted= ""
    if username.isalpha():
        if username.isupper():
            encrpted = username.lower()
        elif username.islower():
            encrpted = username.upper()
        else:
            encrpted = propernaming(username)
    else:
        encrpted = simplify_string(username)
    
    
       
    
    return "Welcome, "+ encrpted +", to my CSCB20 website!"


if __name__ == '__main__':
    app.run(debug=True)