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
      bhk = request.form.get('rooms')
      bath = request.form.get('bathrooms')
      sqft = request.form.get('areainsqft')
      with open("./model/locations.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
      with open('./model/model.pickle', 'rb') as f:
            __model = pickle.load(f)
            
      try:
        loc_index = __data_columns.index(location.lower())
      except:
        loc_index = -1

      x = np.zeros(len(__data_columns))
      x[0] = float(sqft)
      x[1] = bath
      x[2] = bhk
      if loc_index >= 0:
        x[loc_index] = 1
      finalRate = round(__model.predict([x])[0], 2)  
      return render_template("prediction.html",locationStr=finalRate)
      
      
@app.route('/locations',methods=['get'])
def locations():
    with open("./model/locations.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    response = jsonify({
        'locations': __locations 
    })
    return response
    
if __name__ == "__main__":
    app.run()