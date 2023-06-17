from MainFilter import MainFilter

class EligibilityFilters(MainFilter):


    def _study_permit_filter(self):


        STUDY_PERMITS = [
            "I don't have this",
            "USA F1 Visa",
            "Canadian Study Permit / Visitor Visa",
            "UK Student Visa (Tier 4) / Short Term Study Visa",
            "Australian Study Visa",
            "Irish Stamp 2"
        ]

        # STUDY PERMIT Filter

        print("")
        
        print("Choose one of the following option for 'Study Permit':")

        for index, permit in enumerate(STUDY_PERMITS):

            print(str(index) + ":" + permit)

        permit_choice = input("Enter Option Number: ")

        if permit_choice != "":

            permit_value = STUDY_PERMITS[int(permit_choice)]

            if permit_value == STUDY_PERMITS[1]:

                self.filters["has_us_study_permit"] = True
            
            if permit_value == STUDY_PERMITS[2]:

                self.filters["has_ca_study_permit"] = True
            
            if permit_value == STUDY_PERMITS[3]:

                self.filters["has_gb_study_permit"] = True
            
            if permit_value == STUDY_PERMITS[4]:

                self.filters["has_au_study_permit"] = True
            
            if permit_value == STUDY_PERMITS[5]:

                self.filters["has_ie_study_permit"] = True
            
            print("Permit Option Choosed: " + permit_value)
        
        else:

            print("No permit option choosed.")

    def _nationality_filter(self):

        # Nationality Filter

        print("")

        nationality = input("Nationality: ")

        for country in self.COUNTRIES_LIST:
             
             if nationality.lower() == country["attributes"]["name"].lower():
                nationality = country["attributes"]["code"]
        
        print("Choosed Nationality:", nationality)

        self.filters["nationality"] = nationality

    def _education_country_filter(self):

        # Education Country Filter

        print("")

        education_country = input("Education Country: ")

        for country in self.COUNTRIES_LIST:

            if education_country.lower() == country["attributes"]["name"].lower():
                education_country = country["attributes"]["code"]
        
        print("Choosed Education Country:", education_country)

        self.filters["education_country"] = education_country

    def _education_details_filter(self):

        ## Education Level Filter

        print("")

        print("Choose Your Grade: ")


        for index, education_level_data in enumerate(self.EDUCATION_LEVELS):

            print(str(index+1) + ": " + education_level_data["name"])
        
        grade_id = input("Enter Only Grade Number: ")

        if grade_id != "":

            education_level = self.EDUCATION_LEVELS[int(grade_id)-1]["type"]
            
            print("Choosed Education Level:", education_level)

            self.filters["studied_level"] = education_level

            ## Grading Scheme Filter

            grading_scheme = 0

            self.filters["grading_scheme"] = grading_scheme

            ## Grading Scale Filter

            print("")

            grading_scale = int(input("Enter Grading Scale From 0-100:"))

            print("Choosed Grading Scale:", grading_scale)

            self.filters["grade_scale"] = grading_scale

            ## Grading Average Filter

            print("")

            grading_average = int(input("Enter Grading Average: "))

            print("Choosed Grading Average:", grading_average)

            self.filters["grade"] = grading_average
        
        else:

            print("No Grade Choosed.")
        
        return grade_id

    def _english_exam_filter(self):

        ENGLISH_TESTS = {
                            'dont_have':{"value":"dont_have"},
                            'provide_later':{"value":"provide_later"},
                            'toefl':{"value":"toefl","r":0,"l":0,"s":0,"w":0}, # r: reading, l: listening, s: speaking, w: writing
                            'ielts':{"value":"ielts","r":0,"l":0,"s":0,"w":0}, # r: reading, l: listening, s: speaking, w: writing
                            'duolingo_english':{"value":"duolingo_english","total":0},
                            'pte':{"value":"pte","r":0,"l":0,"s":0,"w":0,"total":0}
                            
                        }
        
        ENGLISH_TESTS_LIST = [test for test in ENGLISH_TESTS.keys()]

        ## English Exam Filter

        print("")

        print("Choose English Exam Type:")

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


        self.filters["eng_test"] = eng_test_dict

    def _direct_admission_filter(self):

        ## Only Direct Admissions Filter

        print("")

        print("Show Only Direct Admissions:")

        only_direct_admission = True if input("Enter 'Yes' Or 'No': ").lower() == "yes" else False

        print("Direct Admission Choosed:", only_direct_admission)

        self.filters["only_direct"] = only_direct_admission
    
    def _gre_filter(self, grade_id):

        if grade_id != "":

            # If grade is higher than grade of higher school
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

                    self.filters["gre"] = gre_dict

    def _gmat_filter(self, grade_id):

        if grade_id != "":

            # If grade is higher than grade of higher school
            if int(grade_id) > 12:

                # GMAT Filter

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

                self.filters["gmat"] = gmat_dict

    def eligibilityFilters(self):

        self._study_permit_filter()

        self._nationality_filter()

        self._education_country_filter()

        grade_id = self._education_details_filter()

        self._english_exam_filter()

        self._direct_admission_filter()

        self._gre_filter(grade_id)

        self._gmat_filter(grade_id)