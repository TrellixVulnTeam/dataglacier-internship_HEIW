from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/predict", methods=['POST'])
def predict():





if __name__ == "__main__":
    app.run(debug=True)