from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_flask():
    return "Dude it works!!!"

@app.route('/game')
def gogame():
    return"Hey put a game here sometime!...maybe? Please? Pretty please with a muffin on top?"
    #STOP TYPING NONSENSE AND GET TO WORK!!! /:[
    