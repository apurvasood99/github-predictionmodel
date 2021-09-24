from flask import Flask,render_template,request, jsonify
import pickle
import json
import numpy as np


app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return render_template("index.html")
    
@app.route('/prediction', methods=['GET','POST'])
def prediction():
    if request.method == 'GET':
        return render_template("prediction.html",locationStr="Nothing")
    if request.method == 'POST':
      location = request.form.get('location')
      return render_template("prediction.html",locationStr=location)
      
      
@app.route('/locations',methods=['get'])
def locations():
    with open("./model/locations.json", "r") as f:
        __locations = json.load(f)['locations']
    response = jsonify({
        'locations': __locations 
    })
    return response
    
if __name__ == "__main__":
    app.run()