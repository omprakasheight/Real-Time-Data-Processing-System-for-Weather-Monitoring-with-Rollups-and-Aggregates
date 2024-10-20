# Real-Time Weather Monitoring System

## Project Overview
This project is a real-time data processing system that monitors weather conditions in major Indian cities using the OpenWeatherMap API. It retrieves weather data at configurable intervals, processes the data to provide daily rollups and aggregates, and raises alerts based on user-defined thresholds.

The system is developed using Python and includes visualizations and a simple alerting mechanism to summarize weather trends and notify users of significant conditions.

## Features
- **Weather Data Retrieval**: Fetches real-time weather data for cities like Delhi, Mumbai, Chennai, Bangalore, Kolkata, and Hyderabad.
- **Data Processing**: Converts temperature values from Kelvin to Celsius and extracts relevant weather parameters.
- **Daily Rollups and Aggregates**: Calculates average, maximum, and minimum temperatures and identifies the dominant weather condition for each day.
- **Alerting System**: Allows users to define thresholds for weather conditions (e.g., temperature) and raises alerts when thresholds are breached.
- **Visualization**: Displays daily summaries, historical trends, and alerts using visual tools.

## Requirements
- Python 3.x
- Python Libraries:
  - `requests`: For making API requests to OpenWeatherMap.
  - `python-dotenv`: For managing environment variables.
  - `matplotlib` (optional): For visualizations.
  - `pandas` (optional): For data processing.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/omprakasheight/real-time-weather-monitoring.git
cd real-time-weather-monitoring
```

### 2. Create and Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
- Create a `.env` file in the project root with the following content:
  ```
  API_KEY=os.getenv(6027866698d0c4a0e2b6a0f4218ae673)
  ```
  Replace `os.getenv(6027866698d0c4a0e2b6a0f4218ae673)` with your actual OpenWeatherMap API key.

### 5. Run the Application
```bash
python3 main.py
```

## Usage
- The script fetches weather data for predefined cities every 5 minutes.
- It calculates daily summaries, such as average, maximum, and minimum temperatures, as well as the dominant weather condition.
- Alerts are printed to the console or can be extended to send email notifications.

## Example Output
```
City: Delhi, Temp: 30.5°C, Feels Like: 32.0°C, Condition: Clear
City: Mumbai, Temp: 28.0°C, Feels Like: 29.5°C, Condition: Rain
...
```

## Configurable Alerting System
- Users can set custom thresholds for weather conditions, such as:
  - Alert if the temperature exceeds 35°C for two consecutive readings.
- Alerts can be customized to send notifications (e.g., emails).

## Visualizations
- Daily weather summaries and trends can be visualized using tools like `matplotlib`.
- Example visualizations include line charts for temperature trends and bar charts for dominant weather conditions.

## Testing
- **Unit Tests**: Validate temperature conversion and data processing.
- **Mocking API Responses**: Use mock data to test the application without hitting the actual OpenWeatherMap API.
