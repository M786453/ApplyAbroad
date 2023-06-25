import requests
import json
from Filters import Filters
from ProgramsDetails import ProgramDetails
from env import headers

def getProgramsData():

    PROGRAMS_DATA_URL = "https://www.applyboard.com/program_search.json"

    programs_data_response = requests.get(PROGRAMS_DATA_URL)

    return json.loads(programs_data_response.text)


def getProgramsByFilters():
    
    filters = Filters().get()

    print(filters)

    PROGRAMS_URL = "https://www.applyboard.com/program_search.json?group_by_school=false"

    programs_response = requests.post(PROGRAMS_URL, headers=headers, json=filters)

    try:

        programs = json.loads(programs_response.text)

        if "programs" in programs.keys():

            programs = json.loads(programs_response.text)["programs"]

            #Updating programs data with their intakes data
            for program in programs:

                program["intakes"],program["program_requirement"] = ProgramDetails().get(program["id"])
        
    except Exception as e:
        
        programs = list()

    return programs

with open("programs.json", "w") as out:
    out.write(json.dumps(getProgramsByFilters()))




