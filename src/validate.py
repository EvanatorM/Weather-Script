import re
import json

def validate_zip(zip):
    # Check regex
    try:
        if (not re.match(r"^[0-9]{5}$", zip)):
            print("Zip must be in in the format #####")
            return False
    except:
        print("Zip must be in in the format #####")
        return False

    return True

def validate_address(data):
    # Check if address exists
    try:
        if (len(data["results"]) == 0):
            print("Cannot find zip code")
            return False
    except:
        print("Cannot find zip code")
        return False

    return True

def validate_lat_long(lat, long):
    try:
        latF = float(lat)
        longF = float(long)

        if (latF < -90 or latF > 90):
            print("Invalid location")
            return False
        if (longF < -180 or longF > 180):
            print("Invalid location")
            return False
    except:
        print("Invalid location")
        return False
    
    return True

def validate_weather(data):
    try:
        data = json.loads(data)
        if (len(data["timelines"]["daily"]) < 3):
            return False
        
        return True
    except:
        print("Invalid weather response")
        return False