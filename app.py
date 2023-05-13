import json
import jinja2 
import requests # To sends HTTP requests => GET,POST 
from flask import render_template
from jinja2 import TemplateNotFound
from flask import Flask
app = Flask(__name__)

@app.route('/',methods=['GET', 'POST']) # .route tells @app That whenever user visits app domain execute index() function
def index():
   req = requests.get('https://jsonplaceholder.typicode.com/todos/') # Fetch Data From API Into Req
   reqdata = req.json() # Converts Data To JSON Format
   # for i in range(len(reqdata)):
   #  print(reqdata)
   return render_template('index.html', newdata=reqdata) # Passes API Data as "newdata" Into File index.html


if __name__ == '__main__':
   app.run(debug=True)
