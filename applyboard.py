import requests
import json

from Filters import Filters
from ProgramsDetails import ProgramDetails

def getProgramsData():

    PROGRAMS_DATA_URL = "https://www.applyboard.com/program_search.json"

    programs_data_response = requests.get(PROGRAMS_DATA_URL)

    return json.loads(programs_data_response.text)


def getProgramsByFilters():

    filters = Filters().get()

    print(filters)

    PROGRAMS_URL = "https://www.applyboard.com/program_search.json?group_by_school=false"

    headers = {
        "Cookie": "datadome=UCCZZoHWrb2t5vyfZSijf7mmwkdMng0fgS5dQgmPw24nLxJQXhG_SxjuKkR9Rh5T3jvfcdxjT10xFiONRxdu3MOPNBLF3jS14pEdwhSvSDOFAgiw54CF4~xNMR5eMjf",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43",
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json, text/plain, */*, application/json",
        "Accept-Language": "en-US,en;q=0.9"
    }
    
    programs_response = requests.post(PROGRAMS_URL, headers=headers, json=filters)

    try:

        programs = json.loads(programs_response.text)

        if "programs" in programs.keys():

            programs = json.loads(programs_response.text)["programs"]

            #Updating programs data with their intakes data
            for program in programs:

                program["intakes"],program["program_requirement"] = ProgramDetails().get(program["id"])


        
        
    except Exception as e:

        print(e)
        
        programs = list()

    

    return programs

with open("programs.json", "w") as out:
    out.write(json.dumps(getProgramsByFilters()))




