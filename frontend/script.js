let map;
let chart;

function getClimate() {
    const city = document.getElementById("city").value;

    fetch(`http://127.0.0.1:5000/predict?city=${city}`)
    .then(res => res.json())
    .then(data => {

        const resultDiv = document.getElementById("result");
        resultDiv.innerHTML = `
            <h3>🌡 Temperature: ${data.temperature} °C</h3>
            <h3>💧 Humidity: ${data.humidity}%</h3>
            <h3>💨 Wind Speed: ${data.wind_speed} m/s</h3>
            <h3>🌫 AQI: ${data.AQI}</h3>
            <h2>🚨 Risk Level: ${data.risk_level}</h2>
        `;

        /* Smooth Risk Bar */
        let percent = data.risk_level === "High" ? 90 :
                      data.risk_level === "Medium" ? 60 : 30;

        let color = data.risk_level === "High" ? "#dc3545" :
                    data.risk_level === "Medium" ? "#ff9800" : "#28a745";

        const bar = document.getElementById("riskFill");
        bar.style.background = color;
        setTimeout(() => bar.style.width = percent + "%", 100);

        /* Professional Suggestions */
        const suggestion = document.getElementById("suggestionText");

        if (data.risk_level === "Low") {
            suggestion.innerHTML = `
                <ul>
                    <li>✔ Safe for outdoor activities</li>
                    <li>✔ Maintain hydration</li>
                    <li>✔ Ideal conditions for exercise</li>
                </ul>
            `;
        }
        else if (data.risk_level === "Medium") {
            suggestion.innerHTML = `
                <ul>
                    <li>⚠ Limit prolonged exposure</li>
                    <li>⚠ Stay hydrated frequently</li>
                    <li>⚠ Sensitive individuals wear mask</li>
                </ul>
            `;
        }
        else {
            suggestion.innerHTML = `
                <ul>
                    <li>🚨 Avoid outdoor activity</li>
                    <li>🚨 Stay indoors</li>
                    <li>🚨 Use air purifier</li>
                    <li>🚨 Follow official health advisory</li>
                </ul>
            `;
        }

        /* Map */
        if (map) map.remove();
        map = L.map('map').setView([data.lat, data.lon], 10);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
        L.marker([data.lat, data.lon]).addTo(map);

        /* Chart */
        if (chart) chart.destroy();
        chart = new Chart(document.getElementById("tempChart"), {
            type: 'bar',
            data: {
                labels: ["Temperature", "Humidity", "Wind"],
                datasets: [{
                    label: "Climate Metrics",
                    data: [data.temperature, data.humidity, data.wind_speed],
                    backgroundColor: ["#00c6ff","#ff9f43","#1cc88a"]
                }]
            }
        });

    });
}

function refreshPage() {
    location.reload();
}
