import requests
import json

from Filters import Filters

def getSchoolsData():

    SCHOOLS_DATA_URL = "https://www.applyboard.com/quick_search.json"

    schools_data_response = requests.get(SCHOOLS_DATA_URL)

    return json.loads(schools_data_response.text)

def getProgramsData():

    PROGRAMS_DATA_URL = "https://www.applyboard.com/program_search.json"

    programs_data_response = requests.get(PROGRAMS_DATA_URL)

    return json.loads(programs_data_response.text)


def getProgramsByFilters():

    filters = Filters().get()

    PROGRAMS_URL = "https://www.applyboard.com/program_search.json?group_by_school=false"

    headers = {
        "Cookie": "datadome=3y_uhsIaBwAAI9oXm5xuJwXU0I2qi97OE8eA-koMaGraECSxrm99dXbJUw1dZ3nTqvDrCguWExeuJxGk-X_KSeV2JkbHSmDEIL18QWJ6RvwzjnT_qLgcvx4C0BS1AtPD",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43",
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json, text/plain, */*, application/json",
        "Accept-Language": "en-US,en;q=0.9"
    }
    
    programs_response = requests.post(PROGRAMS_URL, headers=headers, json=filters)

    return json.loads(programs_response.text)

with open("programs.json", "w") as out:
    out.write(json.dumps(getProgramsByFilters()))




