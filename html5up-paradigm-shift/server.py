#import flask 
from flask import Flask,render_template

app=Flask(__name__)

#path to portfolio
@app.route('/portfolio')
def my_portfolio():
    return render_template("index.html")

if __name__=="__main__":
    app.run()
