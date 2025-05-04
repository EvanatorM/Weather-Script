# Hardened Weather Application
This weather application shows basic knowledge of Python, API usage, and security fundamentals. To use it, you simply type in your zip code and it will give you the weather for 3 days.

## Running the application
To run, I would recommend creating a venv to install the requirements in. In a terminal set to the project directory, run:
```bash
python -m venv .venv
.venv/scripts/activate
```

Then, install the requirements from requirements.txt:
```bash
pip install -r requirements.txt
```

Then you can run the script using this command:
```bash
python weather.py
```

## API Keys
API keys are not included in this repository. Instead, they should be put in a config.py file (ignored by gitignore) inside of the src folder. The API key variables in config.py are as follows:

`GEOCODE_API_KEY`: Google Geocode API key

`TOMORROW_API_KEY`: Tomorrow.io API key

## Dependencies
Python was used for this project with the following dependencies:
- certifi 2024.12.14
- charset-normalizer 3.4.1
- idna 3.10
- requests 2.32.3
- urllib3 2.3.0

## APIs Used
I used the following APIs in this project:
- Google Geocode - This API gives location data. I use it here to get the latitude and longitude of the given zip code. It is also used to verify that the zip code exists.
- Tomorrow.io - This API takes lat and long values and returns a weather forecast.

## Threat Modeling
### Threats mitigated

### Threats not handled
