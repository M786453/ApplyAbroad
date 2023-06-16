import requests
import json

def getSchoolsData():

    SCHOOLS_DATA_URL = "https://www.applyboard.com/quick_search.json"

    schools_data_response = requests.get(SCHOOLS_DATA_URL)

    return json.loads(schools_data_response.text)

def getProgramsData():

    PROGRAMS_DATA_URL = "https://www.applyboard.com/program_search.json"

    programs_data_response = requests.get(PROGRAMS_DATA_URL)

    return json.loads(programs_data_response.text)

def getCountriesList():
    # sort countries relatvie to their names
    COUNTRIES_URL = "https://www.applyboard.com/api/v2/countries?sort=name"

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36"}

    countries_data_resposne = requests.get(COUNTRIES_URL, headers= headers)

    return json.loads(countries_data_resposne.text)

def getProgramsByFilters():

    PROGRAMS_URL = "https://www.applyboard.com/program_search.json?group_by_school=false"

    headers = {
        "Cookie": "datadome=3y_uhsIaBwAAI9oXm5xuJwXU0I2qi97OE8eA-koMaGraECSxrm99dXbJUw1dZ3nTqvDrCguWExeuJxGk-X_KSeV2JkbHSmDEIL18QWJ6RvwzjnT_qLgcvx4C0BS1AtPD",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43",
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json, text/plain, */*, application/json",
        "Accept-Language": "en-US,en;q=0.9"
    }

    data = {"sort_by":"relevance","filter":{"sort_by":"relevance"},"nationality":"PK","education_country":"CA","studied_level":"bachelors","grading_scheme":0,"grade":3.5,"grade_scale":4,"eng_test":{"value":"ielts","r":5,"l":5,"w":5,"s":5},"has_us_study_permit":False,"has_ca_study_permit":False,"has_gb_study_permit":False,"has_au_study_permit":False,"only_direct":False}
    
    programs_response = requests.post(PROGRAMS_URL, headers=headers, json=data)

    return json.loads(programs_response.text)

def getEducationLevels():

    EDUCATION_LEVELS_URL = "https://www.applyboard.com/api/grades/education_levels"

    education_levels_response = requests.get(EDUCATION_LEVELS_URL)

    return json.loads(education_levels_response.text)

