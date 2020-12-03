"""
Example Flask Application
"""
from flask import Flask, render_template, url_for, request, redirect


app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    """ Render index """
    return render_template('index.html')



@app.route('/quiz')
def quiz():
    
    return render_template('quiz.html')



@app.route('/about',methods=['GET'])
def about():
    
    return render_template('about.html')
    
    
    

@app.errorhandler(404)
def page_not_found(_):
    """ Render 404 page """
    return render_template('404.html')

if __name__ == "__main__":
    app.run(debug=True)
