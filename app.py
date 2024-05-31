from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/parking_data')
def get_parking_data():
    # Call an API to fetch parking data
    api_url = 'https://api.example.com/parking'
    response = requests.get(api_url)
    parking_data = response.json()

    # Process the data as needed
    processed_data = process_parking_data(parking_data)

    return jsonify(processed_data)

def process_parking_data(data):
    processed_data = []
    for parking in data:
        processed_data.append({
            'name': parking['name'],
            'latitude': parking['latitude'],
            'longitude': parking['longitude'],
            'available_slots': parking['available_slots']
        })
    return processed_data

if __name__ == '__main__':
    app.run(debug=True)