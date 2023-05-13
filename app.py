import json
import jinja2
import requests # To sends HTTP requests => GET,POST 
from flask import render_template
from jinja2 import TemplateNotFound
from flask import Flask
app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
   req = requests.get('https://jsonplaceholder.typicode.com/todos/')
   reqdata = req.json()
   # for i in range(len(reqdata)):
   #  print(reqdata)
   return render_template('index.html', newdata=reqdata)


if __name__ == '__main__':
   app.run(debug=True)