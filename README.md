🌍 Urban Climate Risk Intelligence System

An AI-powered web application that predicts urban climate risk levels using real-time weather and air quality data.
This system analyzes environmental parameters and provides smart recommendations to improve public awareness and sustainability.

🚀 Project Overview

Urban Climate Risk Intelligence is a full-stack Machine Learning project designed to:
🌡 Analyze real-time temperature, humidity, and wind speed
🌫 Monitor Air Quality Index (AQI)
🤖 Predict environmental risk level (Low / Medium / High)
📊 Visualize data with interactive charts
📍 Display location using map integration
💡 Provide actionable safety recommendations
🎨 Show dynamic animated UI with smooth transitions
This project demonstrates the practical application of AI for Sustainability and Smart City concepts.

🛠 Technologies Used
🔹 Backend
Python
Flask
Flask-CORS
Scikit-learn (Random Forest)
Pandas
OpenWeather API

🔹 Frontend
HTML5
CSS3 (Glass UI + Smooth Animations)
JavaScript
Chart.js
Leaflet.js (Map Visualization)

🔹 Tools
Git & GitHub
Command Prompt
VS Code

🧠 How It Works
1️⃣ User enters a city name
2️⃣ Backend fetches real-time data from OpenWeather API
3️⃣ Data collected:
Temperature
Humidity
Wind Speed
AQI
4️⃣ Random Forest ML model predicts risk level
5️⃣ Frontend displays:
Risk level
Animated progress bar
Bullet-point safety suggestions
Chart visualization
Interactive map

📊 Risk Classification Logic
Condition	Risk Level
High temperature or AQI	🔴 High
Moderate conditions	🟡 Medium
Safe environmental conditions	🟢 Low
📁 Project Structure
climate-prediction/
│
├── backend/
│   ├── app.py
│   ├── climate_data.csv
│   ├── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│
├── README.md
└── .gitignore

⚙ Installation & Setup

🔹 Clone Repository
git clone https://github.com/sachinv302/climate-prediction.git
cd climate-prediction

🔹 Backend Setup
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
Backend runs at:
http://127.0.0.1:5000

🔹 Frontend Setup
Open new terminal:
cd frontend
python -m http.server 5500
Open browser:
http://127.0.0.1:5500

🎯 Key Features
✔ Real-time climate monitoring
✔ AI-based risk prediction
✔ Smooth animated UI
✔ Interactive map visualization
✔ Bullet-point smart suggestions
✔ Refresh button
✔ Professional website design

🌱 Sustainability Impact
This system helps:
Increase environmental awareness
Support smart city planning
Improve public health monitoring
Provide preventive safety guidance

🔮 Future Improvements
📱 Convert to mobile app
☁ Deploy on cloud (Render / Railway)
📄 Downloadable climate report (PDF)
📊 5-day forecast prediction
🌙 Dark / Light mode toggle
🧠 Deep Learning risk forecasting

👨‍💻 Author

Sachin V
AI & Full-Stack Developer
GitHub: https://github.com/sachinv302

📜 License
This project is licensed under the MIT License.
