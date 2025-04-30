import requests
import json
import datetime
import calendar
import src.config as config
import src.validate as validate

GOOGLE_MAPS_ENDPOINT = "https://maps.googleapis.com"
TOMORROW_ENDPOINT = "https://api.tomorrow.io"

def getZipFromUser():
    zip = input("Enter zipcode: ")
    while (not validate.validateZip(zip)):
        zip = input("Enter zipcode: ")

    return zip

def getLocation(zip):
    # Get lat and long from zip
    res = requests.get(f"{GOOGLE_MAPS_ENDPOINT}/maps/api/geocode/json?address={zip}&key={config.GEOCODE_API_KEY}")

    if (res.status_code != 200):
        print("Failed to get location from zipcode")
        return None, None

    # Validate address
    data = json.loads(res.content)
    if (not validate.validateAddress(data)):
        return None, None
    
    try:
        # Check if components are there
        city = data["results"][0]["address_components"][1]["long_name"]
        lat = data["results"][0]["geometry"]["location"]["lat"]
        long = data["results"][0]["geometry"]["location"]["lng"]

        # Check if lat and long are valid floats
        float(lat)
        float(long)
    except:
        print("Failed to get location from zipcode")
        return None, None

    location = f"{lat},{long}"
    return location, city

def getWeather(location):
    # Get weather info
    res = requests.get(f"{TOMORROW_ENDPOINT}/v4/weather/forecast?location={location}&apikey={config.TOMORROW_API_KEY}&units=imperial")

    if (res.status_code != 200):
        print("Failed to get weather from zipcode")
        return None
    
    return res.content

def printDay(day):
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

def printWeather(data, city):
    data = json.loads(data)
    daily = data["timelines"]["daily"]
    print(f"---------- Forecast for {city}: ----------")
    printDay(daily[0])
    printDay(daily[1])
    printDay(daily[2])

def main():
    # Get zip from user
    data = None
    while (data == None):
        zip = getZipFromUser()

        location, city = getLocation(zip)
        if (location == None):
            continue

        data = getWeather(location)
    
    printWeather(data, city)


if __name__ == "__main__":
    main()