from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import requests
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)
CORS(app)

# ---------------- MODEL TRAINING ----------------

data = pd.read_csv("climate_data.csv")

def classify_risk(row):
    if row['temperature'] > 40 or row['AQI'] > 4:
        return "High"
    elif row['temperature'] > 35 or row['AQI'] > 2:
        return "Medium"
    else:
        return "Low"

data['Risk_Level'] = data.apply(classify_risk, axis=1)

X = data[['temperature', 'humidity', 'wind_speed', 'AQI']]
y = data['Risk_Level']

le = LabelEncoder()
y = le.fit_transform(y)

model = RandomForestClassifier()
model.fit(X, y)

# 🔴 ADD YOUR API KEY HERE
API_KEY = "5df5b923ed83a5eccda0a8d300c52aaf"

@app.route("/")
def home():
    return "Climate Risk API Running"

@app.route("/predict", methods=["GET"])
def predict():
    city = request.args.get("city")

    if not city:
        return jsonify({"error": "City required"})

    try:
        # Get coordinates
        geo_url = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
        geo_response = requests.get(geo_url)
        geo_data = geo_response.json()

        if not geo_data:
            return jsonify({"error": "City not found"})

        lat = geo_data[0]["lat"]
        lon = geo_data[0]["lon"]

        # Get weather
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}"
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()

        temp = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind = weather_data["wind"]["speed"]
        condition = weather_data["weather"][0]["main"]

        # Get AQI
        aqi_url = f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
        aqi_response = requests.get(aqi_url)
        aqi_data = aqi_response.json()

        AQI = aqi_data["list"][0]["main"]["aqi"]

        # Predict risk
        input_df = pd.DataFrame(
            [[temp, humidity, wind, AQI]],
            columns=['temperature', 'humidity', 'wind_speed', 'AQI']
        )

        prediction = model.predict(input_df)
        risk = le.inverse_transform(prediction)[0]

        return jsonify({
            "temperature": temp,
            "humidity": humidity,
            "wind_speed": wind,
            "AQI": AQI,
            "risk_level": risk,
            "lat": lat,
            "lon": lon,
            "weather_condition": condition
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
