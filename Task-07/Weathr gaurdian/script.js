const apiKey = 'ef073c45d0e9b11ee96b26af2d395974'; 
const apiUrl = 'https://api.openweathermap.org/data/2.5/weather';

document.getElementById('city-input-btn').addEventListener('click', function() {
    const cityName = document.getElementById('city-input').value;
    if (cityName) {
        fetchWeather(cityName);
    }
});

async function fetchWeather(cityName) {
    const url = `${apiUrl}?q=${cityName}&appid=${apiKey}&units=metric`;
    try {
        const response = await fetch(url);
        const data = await response.json();
        if (response.ok) {
            displayWeather(data);
        } else {
            alert('City not found. Please try again.');
        }
    } catch (error) {
        console.error('Error fetching weather data:', error);
    }
}

function displayWeather(data) {
    document.getElementById('city-name').textContent = data.name;
    document.getElementById('temperature').textContent = `${Math.round(data.main.temp)}°C`;
    document.getElementById('description').textContent = data.weather[0].description;
    document.getElementById('wind-speed').textContent = `Wind Speed: ${data.wind.speed} m/s`;
    document.getElementById('weather-icon').src = `http://openweathermap.org/img/wn/${data.weather[0].icon}.png`;
    document.getElementById('weather-info').style.display = 'block';
}