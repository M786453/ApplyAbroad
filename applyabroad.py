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

def whereAutocomplete(query, nmbr_of_results):

    AUTOCOMPLETE_URL = f"https://www.applyboard.com/api/autocomplete/where/ac/?q={query}&n={nmbr_of_results}"

    autocomplete_response = requests.get(AUTOCOMPLETE_URL)

    return json.loads(autocomplete_response.text)

def getCountriesList():
    # sort countries relatvie to their names
    COUNTRIES_URL = "https://www.applyboard.com/api/v2/countries?sort=name"

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36"}

    countries_data_resposne = requests.get(COUNTRIES_URL, headers= headers)

    return json.loads(countries_data_resposne.text)

def getEducationLevels():

    EDUCATION_LEVELS_URL = "https://www.applyboard.com/api/grades/education_levels"

    education_levels_response = requests.get(EDUCATION_LEVELS_URL)

    return json.loads(education_levels_response.text)

def getGradingScheme(country_code: str, education_level: int):

    GRADING_SCHEME_URL = f"https://www.applyboard.com/api/grades/grading_schemes?country_code={country_code}&level={education_level}"

    grading_scheme_response = requests.get(GRADING_SCHEME_URL)

    return json.loads(grading_scheme_response.text)


def getFilters() -> dict:

        COUNTRIES_LIST = getCountriesList()["data"]

        EDUCATION_LEVELS = getEducationLevels()

        STUDY_PERMITS = [
            "I don't have this",
            "USA F1 Visa",
            "Canadian Study Permit / Visitor Visa",
            "UK Student Visa (Tier 4) / Short Term Study Visa",
            "Australian Study Visa",
            "Irish Stamp 2"
        ]

        ENGLISH_TESTS = {
                            'dont_have':{"value":"dont_have"},
                            'provide_later':{"value":"provide_later"},
                            'toefl':{"value":"toefl","r":0,"l":0,"s":0,"w":0}, # r: reading, l: listening, s: speaking, w: writing
                            'ielts':{"value":"ielts","r":0,"l":0,"s":0,"w":0}, # r: reading, l: listening, s: speaking, w: writing
                            'duolingo_english':{"value":"duolingo_english","total":0},
                            'pte':{"value":"pte","r":0,"l":0,"s":0,"w":0,"total":0}
                            
                        }

        SORT_BY = [
                            "relevance",
                            "school_rank",
                            "tuition_low",
                            "tuition_high",
                            "fee_low",
                            "fee_high"
                ]



        filters = {
                "sort_by":str(),"filter":{"sort_by":str()},
                "nationality":str(),"education_country":str(),
                "studied_level":str(),"grading_scheme":str(),
                "grade":int(),"grade_scale":int(),
                "eng_test":dict(),"has_us_study_permit":bool(),
                "has_ca_study_permit":bool(),"has_gb_study_permit":bool(),
                "has_au_study_permit":bool(),"has_ie_study_permit":bool(),
                "only_direct":bool()
            }
        

        # Get Inputs from user and update the filters dict

        # Search Query

        where = input("Enter School or Location: ")

        if where == "":

            print("No Location or School provided.")

        # "where_text":"manchester","where_value":"manchester","where_type":"unknown",

        ## Updating Filter

        filters["where_text"] = where
        filters["where_value"] = where
        filters["where_type"] = "unknown"

        filters["filter"]["where_text"] = where
        filters["filter"]["where_value"] = where
        filters["filter"]["where_type"] = "unknown"


        # Eligibility Details
        print("")
        print("####### Eligibility Details #######")

        
        ## SORT BY Filter

        print("")

        print("Choose one of the following 'Sort By' Option:")

        for index, sort_value in enumerate(SORT_BY):
             
            print(str(index) + ":" + sort_value)

        sort_by_choice = input("'Sort By' Option Number: ")

        if sort_by_choice == "":
            sort_by = SORT_BY[0]
            print("Default Sort By Option:", sort_by)
        else:
            sort_by = int(sort_by_choice)

            sort_by = SORT_BY[sort_by]

            print("Sort By Option Choosed:", sort_by)

        """
        Updating 'Sort By' Filter Value
        """

        filters["sort_by"] = sort_by

        filters["filter"]["sort_by"] = sort_by

        ## STUDY PERMIT Filter

        print("")
        
        print("Choose one of the following option for 'Study Permit':")

        for index, permit in enumerate(STUDY_PERMITS):

            print(str(index) + ":" + permit)

        permit_choice = input("Enter Option Number: ")

        if permit_choice != "":

            permit_value = STUDY_PERMITS[int(permit_choice)]

            if permit_value == STUDY_PERMITS[1]:

                filters["has_us_study_permit"] = True
            
            if permit_value == STUDY_PERMITS[2]:

                filters["has_ca_study_permit"] = True
            
            if permit_value == STUDY_PERMITS[3]:

                filters["has_gb_study_permit"] = True
            
            if permit_value == STUDY_PERMITS[4]:

                filters["has_au_study_permit"] = True
            
            if permit_value == STUDY_PERMITS[5]:

                filters["has_ie_study_permit"] = True
            
            print("Permit Option Choosed: " + permit_value)
        
        else:

            print("No permit option choosed.")


        ## Nationality Filter

        print("")

        nationality = input("Nationality: ")

        for country in COUNTRIES_LIST:
             
             if nationality.lower() == country["attributes"]["name"].lower():
                nationality = country["attributes"]["code"]
        
        print("Choosed Nationality:", nationality)

        filters["nationality"] = nationality
        
        ## Education Country Filter

        print("")

        education_country = input("Education Country: ")

        for country in COUNTRIES_LIST:

            if education_country.lower() == country["attributes"]["name"].lower():
                education_country = country["attributes"]["code"]
        
        print("Choosed Education Country:", education_country)

        filters["education_country"] = education_country
        
        ## Education Level Filter

        print("")

        print("Choose Your Grade: ")


        for index, education_level_data in enumerate(EDUCATION_LEVELS):

            print(str(index+1) + ": " + education_level_data["name"])
        
        grade_id = input("Enter Only Grade Number: ")

        if grade_id != "":

            education_level = EDUCATION_LEVELS[int(grade_id)-1]["type"]
            
            print("Choosed Education Level:", education_level)

            filters["studied_level"] = education_level

            ## Grading Scheme Filter

            grading_scheme = 0

            filters["grading_scheme"] = grading_scheme

            ## Grading Scale Filter

            print("")

            grading_scale = int(input("Enter Grading Scale From 0-100:"))

            print("Choosed Grading Scale:", grading_scale)

            filters["grade_scale"] = grading_scale

            ## Grading Average Filter

            print("")

            grading_average = int(input("Enter Grading Average: "))

            print("Choosed Grading Average:", grading_average)

            filters["grade"] = grading_average
        
        else:

            print("No Grade Choosed.")

        ## English Exam Filter

        print("")

        print("Choose English Exam Type:")

        ENGLISH_TESTS_LIST = [test for test in ENGLISH_TESTS.keys()]

        for index, value in enumerate(ENGLISH_TESTS_LIST):

            print(str(index) + ":" + value)
        
        eng_test_choice = input("Enter Exam Number: ")

        if eng_test_choice != "":

            eng_test = ENGLISH_TESTS_LIST[int(eng_test_choice)]


            ### Enter Further Details of English Exam

            eng_test_dict = {eng_test: ENGLISH_TESTS[eng_test]}

            ### If selected english test dictionary contains more than 1 values
            if len(ENGLISH_TESTS[eng_test]) > 1:

                print("Enter Further Details of '" + eng_test + "':")

                for key in ENGLISH_TESTS[eng_test].keys():

                    if key == "r":

                        eng_test_dict[eng_test]['r'] = int(input("Enter Reading Score: "))

                    if key == "l":

                        eng_test_dict[eng_test]['l'] = int(input("Enter Listening Score: "))

                    if key == "s":

                        eng_test_dict[eng_test]['s'] = int(input("Enter Speaking Score: "))

                    if key == "w":

                        eng_test_dict[eng_test]['w'] = int(input("Enter Writing Score: "))

                    if key == "total":

                        eng_test_dict[eng_test]["total"] = int(input("Overall Score: "))

            print("Choosed English Exam: ",eng_test_dict)

        else:

            eng_test_dict = {ENGLISH_TESTS_LIST[0]: ENGLISH_TESTS["dont_have"]}

            print("Default English Exam Value: ", eng_test_dict)


        filters["eng_test"] = eng_test_dict

        ## Only Direct Admissions Filter

        print("")

        print("Show Only Direct Admissions:")

        print("Yes")

        print("No")

        only_direct_admission = True if input("Enter 'Yes' Or 'No': ").lower() == "yes" else False

        print("Direct Admission Choosed:", only_direct_admission)

        filters["only_direct"] = only_direct_admission

        ## GRE and GMAT Filter
        ## If grade is higher than grade of higher school
        if grade_id != "":

            if int(grade_id) > 12:

                ### GRE Filter

                print("")

                gre_dict = {"value": False}

                gre_choice = input("Have you passed GRE?\nEnter 'Yes' or 'No':")

                gre_dict["value"] = True if gre_choice.lower() == "yes" else False

                if gre_dict["value"]:
                
                    gre_dict["v"] = int(input("Enter Verbal Score: "))
                    gre_dict["vp"] = int(input("Enter Verbal Rank%: "))

                    gre_dict["q"] = int(input("Enter Quantitative Score: "))
                    gre_dict["qp"] = int(input("Enter Qunatitative Rank%: "))

                    gre_dict["w"] = int(input("Enter Writing Score: "))
                    gre_dict["wp"] = int(input("Enter Writing Rank%: "))

                #### Update Filters

                filters["gre"] = gre_dict

                ### GMAT Filter

                print("")

                gmat_dict = {"value": False}

                gmat_choice = input("Have you passed GMAT?\nEnter 'Yes' or 'No':")

                gmat_dict["value"] = True if gmat_choice.lower() == "yes" else False
                
                if gmat_dict["value"]:

                    gmat_dict["v"] = int(input("Enter Verbal Score: "))
                    gmat_dict["vp"] = int(input("Enter Verbal Rank%: "))

                    gmat_dict["q"] = int(input("Enter Quantitative Score: "))
                    gmat_dict["qp"] = int(input("Enter Qunatitative Rank%: "))

                    gmat_dict["w"] = int(input("Enter Writing Score: "))
                    gmat_dict["wp"] = int(input("Enter Writing Rank%: "))

                    gmat_dict["t"] = int(input("Enter Total Score: "))
                    gmat_dict["tp"] = int(input("Enter Total%: "))

                #### Update Filters

                filters["gmat"] = gmat_dict



        print(filters)
        
        return filters


def getProgramsByFilters():


    filters = getFilters()


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




