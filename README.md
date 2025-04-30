# Hardened Weather Application
This weather application shows basic knowledge of Python, API usage, and security fundamentals.



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

## API Tokens
API tokens are not included in this repository. Instead, they should be put in a config.py file (ignored by gitignore) inside of the src folder. The API key variables in config.py are as follows:

`GEOCODE_API_KEY`: Google Geocode API key

`TOMORROW_API_KEY`: Tomorrow.io API key