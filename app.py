import requests
import json
import datetime
import calendar
import src.config as config
import src.validate as validate

GOOGLE_MAPS_ENDPOINT = "https://maps.googleapis.com"
TOMORROW_ENDPOINT = "https://api.tomorrow.io"

def get_zip_from_user():
    zip = input("Enter zipcode: ")
    while (not validate.validate_zip(zip)):
        zip = input("Enter zipcode: ")

    return zip

def get_location(zip):
    # Validate zip
    if (not validate.validate_zip(zip)):
        return None, None

    # Get lat and long from zip
    res = requests.get(f"{GOOGLE_MAPS_ENDPOINT}/maps/api/geocode/json?address={zip}&key={config.GEOCODE_API_KEY}")

    if (res.status_code != 200):
        print("Failed to get location from zipcode")
        return None, None

    # Validate address
    try:
        data = json.loads(res.content)
        if (not validate.validate_address(data)):
            print("Failed to get location from zipcode")
            return None, None
        
        # Check if components are there
        city = data["results"][0]["address_components"][1]["long_name"]
        lat = data["results"][0]["geometry"]["location"]["lat"]
        long = data["results"][0]["geometry"]["location"]["lng"]

        # Validate lat and long
        if (not validate.validate_lat_long(lat, long)):
            print("Failed to get location from zipcode")
            return None, None
    except:
        # If this errors out, it means the response is invalid
        # I didn't put this in validate.py since it does both validation and getting
        # the variables at the same time.
        print("Failed to get location from zipcode")
        return None, None

    location = f"{lat},{long}"
    return location, city

def get_weather(location):
    # Get weather info
    res = requests.get(f"{TOMORROW_ENDPOINT}/v4/weather/forecast?location={location}&apikey={config.TOMORROW_API_KEY}&units=imperial")

    if (res.status_code != 200):
        print("Failed to get weather from zipcode")
        return None
    
    if (not validate.validate_weather(res.content)):
        print("Failed to get weather from zipcode")
        return None
    
    return res.content

def print_day(day):
    try:
        date_string = day["time"].split('T')[0].split('-')
        date = datetime.datetime(int(date_string[0]), int(date_string[1]), int(date_string[2]))

        if (date.date() == datetime.date.today()):
            print(f"Today ({calendar.day_name[date.weekday()]}, {calendar.month_name[date.month]} {date.day}):")
        else:
            print(f"{calendar.day_name[date.weekday()]}, {calendar.month_name[date.month]} {date.day}:")
        
        print(f"    Temperature: Avg {round(day["values"]["temperatureAvg"])}{chr(176)}F ({round(day["values"]["temperatureMin"])}{chr(176)}F / {round(day["values"]["temperatureMax"])}{chr(176)}F)")
        print(f"    Chance of Precipitation: {day["values"]["precipitationProbabilityMax"]}%")
        print(f"    Wind Speed: Avg {day["values"]["windSpeedAvg"]} MPH ({day["values"]["windSpeedMin"]} MPH / {day["values"]["windSpeedMax"]} MPH)")
        print("")
    except:
        print("Failed to print weather")

def print_weather(data, city):
    try:
        data = json.loads(data)
        daily = data["timelines"]["daily"]
        print(f"---------- Forecast for {city}: ----------")
        print_day(daily[0])
        print_day(daily[1])
        print_day(daily[2])
    except:
        print("Invalid weather response")

def main():
    # Get zip from user
    data = None
    while (data == None):
        zip = get_zip_from_user()

        location, city = get_location(zip)
        if (location == None):
            continue

        data = get_weather(location)
    
    print_weather(data, city)


if __name__ == "__main__":
    main()