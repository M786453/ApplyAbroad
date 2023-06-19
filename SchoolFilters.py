from MainFilter import MainFilter
import requests
import json

class SchoolFilters(MainFilter):

    def __init__(self):
        super().__init__()
        self.market_data = self._get_markets_data()["data"]
        self.schools = self.SCHOOLS_DATA["schools"]["schoolHashMap"]

    def _country_filter(self):

        COUNTRIES = [country["attributes"]["common_name"] for country in self.market_data]

        SELECTED_COUNTRIES = self._get_user_choices(COUNTRIES, "Countries")

        if len(SELECTED_COUNTRIES) == 0:
            print("No Country Selected.")
        else:
            # Updating Filters
            self.filters["countries"] = SELECTED_COUNTRIES

            self.filters["filter"]["countries"] = SELECTED_COUNTRIES

        return SELECTED_COUNTRIES

    def _post_grad_permit_filter(self):

        # Post-Graduation Work Permit Filter

        print("")

        print("Have Post-Graduation Work Permit?")

        pgwp = True  if input("Enter 'Yes' or 'No': ").lower() == "yes" else False

        # Updating Filters

        self.filters["pgwp"] = pgwp

        self.filters["filter"]["pgwp"] = pgwp

    def _get_markets_data(self):

        MARKETS_URL = "https://www.applyboard.com/api/v2/markets"

        market_response = requests.get(MARKETS_URL)

        return json.loads(market_response.text)

    def _get_provinces(self, selected_countries: list):

        provinces = list()

        for market_country in self.market_data:

            if market_country["attributes"]["common_name"] in selected_countries:

                provinces.extend(market_country["attributes"]["administrative_divisions"])

        return provinces

    def _province_filter(self, selected_countries: list):

        PROVINCES = self._get_provinces(selected_countries)

        SELECTED_PROVINCES = self._get_user_choices(PROVINCES, "Provinces")
        
        if len(SELECTED_PROVINCES) == 0:
            print("No Province Selected.")
        else:
            # Updating Filters
            self.filters["provinces"] = SELECTED_PROVINCES

            self.filters["filter"]["provinces"] = SELECTED_PROVINCES
        
        return SELECTED_PROVINCES

    def _get_cities(self, country_codes : list, provinces : list):

        country_codes = ",".join(country_codes)

        provinces = ",".join(provinces)

        CITIES_URL = f"https://www.applyboard.com/api/v2/schools/cities?country_code={country_codes}&province={provinces}"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9"
        }

        cities_response = requests.get(CITIES_URL, headers=headers)

        cities = list()

        for country in json.loads(cities_response.text)["countries"]:

            for province in country["provinces"]:
                cities.extend(province["cities"])

        return cities

    def _campus_city_filter(self, selected_countries: list, selected_provinces: list):

        country_codes = [country["id"] for country in self.market_data if country["attributes"]["common_name"] in selected_countries]

        CITIES = self._get_cities(country_codes, selected_provinces)
        
        SELECTED_CITIES = self._get_user_choices(CITIES, "Cities")

        if len(SELECTED_CITIES) == 0:
            print("No City Selected.")
        else:
            # Updating Filters
            self.filters["cities"] = SELECTED_CITIES
            self.filters["filter"]["cities"] = SELECTED_CITIES 
        
        return SELECTED_CITIES

    def _school_type_filter(self):

        SCHOOL_TYPES = [
            "University",
            "College",
            "English Institute",
            "High School"
        ]

        SELECTED_SCHOOL_TYPES = self._get_user_choices(SCHOOL_TYPES, "School Types")

        SELECTED_TYPES_NUMBERS = list()

        for t in SELECTED_SCHOOL_TYPES:

            SELECTED_TYPES_NUMBERS.append(int(SCHOOL_TYPES.index(t)) + 1)


        if len(SELECTED_SCHOOL_TYPES) == 0:
            print("No School Type Selected")
        else:
            #Updating Filters
            self.filters["school_types"] = SELECTED_TYPES_NUMBERS
            self.filters["filter"]["school_types"] = SELECTED_TYPES_NUMBERS

        return SELECTED_TYPES_NUMBERS

    def _school_filter(self, selected_countries, selected_provinces, 
                       selected_cities, selected_school_types):

        FILTERED_SCHOOLS = dict()
        FILTERED_SCHOOLS_NAMES = list()

        for school_id in self.schools:

            school = self.schools[school_id]

            if school["country"] in selected_countries and school["province"] in selected_provinces and school["city"] in selected_cities and school["type"] in selected_school_types:

                FILTERED_SCHOOLS[school["name"]] = school_id

                FILTERED_SCHOOLS_NAMES.append(school["name"])

                
        SELECTED_SCHOOLS = self._get_user_choices(FILTERED_SCHOOLS_NAMES, "Schools")

        SELECTED_SCHOOLS_IDS = [FILTERED_SCHOOLS[school_name] for school_name in SELECTED_SCHOOLS]

        

        if len(SELECTED_SCHOOLS_IDS) == 0:
            print("No School Selected.")
        else:
            #Updating Filters
            self.filters["school_ids"] = SELECTED_SCHOOLS_IDS
            self.filters["filter"]["school_ids"] = SELECTED_SCHOOLS_IDS

    def schoolFilters(self):

        selected_countries = self._country_filter()

        self._post_grad_permit_filter()

        selected_provinces = self._province_filter(selected_countries)

        selected_cities = self._campus_city_filter(selected_countries, selected_provinces)

        selected_types = self._school_type_filter()

        self._school_filter(selected_countries, selected_provinces, selected_cities, selected_types)
