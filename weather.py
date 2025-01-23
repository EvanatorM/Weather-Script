import requests
import json
import datetime
import calendar

GOOGLE_MAPS_ENDPOINT = "https://maps.googleapis.com"
GEOCODE_API_KEY = "ENTER_KEY_HERE"

TOMORROW_ENDPOINT = "https://api.tomorrow.io"
TOMORROW_API_KEY = "ENTER_KEY_HERE"

def celciusToFahrenheit(c):
    return (c * (9/5)) + 32

def printDay(day):
    date_string = day["time"].split('T')[0].split('-')
    date = datetime.datetime(int(date_string[0]), int(date_string[1]), int(date_string[2]))

    if (date.date() == datetime.date.today()):
        print(f"Today ({calendar.day_name[date.weekday()]}, {calendar.month_name[date.month]} {date.day}):")
    else:
        print(f"{calendar.day_name[date.weekday()]}, {calendar.month_name[date.month]} {date.day}:")
    
    print(f"    Temperature: {round(celciusToFahrenheit(day["values"]["temperatureMin"]))}{chr(176)}F/{round(celciusToFahrenheit(day["values"]["temperatureMax"]))}{chr(176)}F (Avg {round(celciusToFahrenheit(day["values"]["temperatureAvg"]))}{chr(176)}F)")
    print(f"    Chance of Precipitation: {day["values"]["precipitationProbabilityMax"]}%")

def main():
    # Get zip from user
    zip = input("Enter zipcode: ")
    while (not zip.isnumeric() or not len(zip) == 5):
        print("Zip must be a 5 digit number.")
        zip = input("Enter zipcode: ")

    # Get lat and long from zip
    res = requests.get(f"{GOOGLE_MAPS_ENDPOINT}/maps/api/geocode/json?address={zip}&key={GEOCODE_API_KEY}")

    if (res.status_code != 200):
        print("Failed to get location from zipcode")
        return

    data = json.loads(res.content)
    city = data["results"][0]["address_components"][1]["long_name"]
    lat = data["results"][0]["geometry"]["location"]["lat"]
    long = data["results"][0]["geometry"]["location"]["lng"]

    location = f"{lat},{long}"

    # Get weather info
    res = requests.get(f"{TOMORROW_ENDPOINT}/v4/weather/forecast?location={location}&apikey={TOMORROW_API_KEY}")

    if (res.status_code != 200):
        print("Failed to get location from zipcode")
        return

    data = json.loads(res.content)
    daily = data["timelines"]["daily"]
    print(f"Forecast for {city}:")
    printDay(daily[0])
    printDay(daily[1])
    printDay(daily[2])


if __name__ == "__main__":
    main()