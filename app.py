"""
Example Flask Application
"""
from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    """ Render index """
    return render_template('index.html')



@app.errorhandler(404)
def page_not_found(_):
    """ Render 404 page """
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run()
