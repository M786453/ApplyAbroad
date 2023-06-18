import requests
import json

class MainFilter:

    def __init__(self):
        
        self.filters = {
                "sort_by":str(),"filter":{"sort_by":str()},
                "nationality":str(),"education_country":str(),
                "studied_level":str(),"grading_scheme":str(),
                "grade":int(),"grade_scale":int(),
                "eng_test":dict(),"has_us_study_permit":bool(),
                "has_ca_study_permit":bool(),"has_gb_study_permit":bool(),
                "has_au_study_permit":bool(),"has_ie_study_permit":bool(),
                "only_direct":bool()
            }
        
        self.COUNTRIES_LIST = self._get_countries_list()["data"]

        self.EDUCATION_LEVELS = self._get_education_levels_data()

        self.SCHOOLS_DATA = self._get_schools_data()
    
    def _what_study_filter(self):

        # What Study Details

        print("")

        what = input("What would you like to study: ")

        if what == "":

            print("No Target Study.")
        
        ## Updating Filter

        self.filters["what_text"] = what
        self.filters["what_value"] = what
        self.filters["what_type"] = "unknown"

        self.filters["filter"]["what_text"] = what
        self.filters["filter"]["what_value"] = what
        self.filters["filter"]["what_type"] = "unknown"

    def _where_study_filter(self):

        # Where study Details

        print("")

        where = input("Enter School or Location: ")

        if where == "":

            print("No Location or School provided.")

        ## Updating Filter

        self.filters["where_text"] = where
        self.filters["where_value"] = where
        self.filters["where_type"] = "unknown"

        self.filters["filter"]["where_text"] = where
        self.filters["filter"]["where_value"] = where
        self.filters["filter"]["where_type"] = "unknown"
    
    def _sort_by_filter(self):

        SORT_BY = [
                            "relevance",
                            "school_rank",
                            "tuition_low",
                            "tuition_high",
                            "fee_low",
                            "fee_high"
                ]
        
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

        self.filters["sort_by"] = sort_by

        self.filters["filter"]["sort_by"] = sort_by

    def _get_countries_list(self):
        # sort countries relatvie to their names
        COUNTRIES_URL = "https://www.applyboard.com/api/v2/countries?sort=name"

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36"}

        countries_data_resposne = requests.get(COUNTRIES_URL, headers= headers)

        return json.loads(countries_data_resposne.text)

    def _get_education_levels_data(self):

        EDUCATION_LEVELS_URL = "https://www.applyboard.com/api/grades/education_levels"

        education_levels_response = requests.get(EDUCATION_LEVELS_URL)

        return json.loads(education_levels_response.text)

    def _where_auto_complete(query, nmbr_of_results):

        AUTOCOMPLETE_URL = f"https://www.applyboard.com/api/autocomplete/where/ac/?q={query}&n={nmbr_of_results}"

        autocomplete_response = requests.get(AUTOCOMPLETE_URL)

        return json.loads(autocomplete_response.text)

    def _get_grading_scheme(country_code: str, education_level: int):

        GRADING_SCHEME_URL = f"https://www.applyboard.com/api/grades/grading_schemes?country_code={country_code}&level={education_level}"

        grading_scheme_response = requests.get(GRADING_SCHEME_URL)

        return json.loads(grading_scheme_response.text)

    def _get_schools_data(self):

            SCHOOLS_DATA_URL = "https://www.applyboard.com/quick_search.json"

            schools_data_response = requests.get(SCHOOLS_DATA_URL)

            return json.loads(schools_data_response.text)

    def mainFilters(self):

        self._what_study_filter()

        self._where_study_filter()

        self._sort_by_filter()
