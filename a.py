'''from flask import Flask, render_template

app = Flask(__name__)





@app.route("/")

def home():

    return render_template('home.html')





if __name__ == '__main__':

    app.run(debug=True)'''
from flask import Flask, render_template 
 
app = Flask(__name__) 
 
@app.route('/')
def home():
    return render_template("home.html")
    return "Hey there,this is Thanh's website"
@app.route('/about-me')
def about():
    return render_template('about.html')
 
if __name__ == '__main__': app.run(debug=True) 
 
