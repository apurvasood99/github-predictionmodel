from flask import Flask,render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return render_template("index.html")
    
@app.route('/prediction', methods=['GET'])
def predictionpage():
    return render_template("prediction.html")
    
    
if __name__ == "__main__":
    app.run()