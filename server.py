from flask import Flask,render_template,request

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
    
if __name__ == "__main__":
    app.run()