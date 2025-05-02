import re

def validateZip(zip):
    # Check regex
    if (not re.match(r"^[0-9]{5}$", zip)):
        print("Zip must be in in the format #####")
        return False

    return True

def validateAddress(data):
    # Check if address exists
    if (len(data["results"]) == 0):
        print("Cannot find zip code")
        return False

    return True