
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load the trained model and vectorizer
model = joblib.load('phishing_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']
    data = [url]
    vect = vectorizer.transform(data)
    prediction = model.predict(vect)
    result = 'Phishing' if prediction[0] == 1 else 'Legitimate'
    return render_template('index.html', prediction_text=f'The URL is {result}')

if __name__ == '__main__':
    app.run(port=5000)
