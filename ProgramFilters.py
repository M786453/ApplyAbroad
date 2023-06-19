from MainFilter import MainFilter

class ProgramFilters(MainFilter):
    
    def __init__(self):
        """
        Added for only testing purposes, remove this after testing
        """
        super().__init__()

    def _program_level_filter(self):

        PROGRAM_LEVELS_DATA = self.SCHOOLS_DATA["filterOptions"]["program_level"]

        PROGRAM_LEVELS = [level["label"] for level in PROGRAM_LEVELS_DATA]

        SELECTED_PROGRAM_LEVELS = self._get_user_choices(PROGRAM_LEVELS, "Program Levels")

        SELECTED_PROGRAM_LEVELS_VALUES = [level["value"] for level in PROGRAM_LEVELS_DATA if level["label"] in SELECTED_PROGRAM_LEVELS]

        if len(SELECTED_PROGRAM_LEVELS_VALUES) == 0:

            print("No Program Level Selected")

        else:

            #Updating Filter

            self.filters["program_level"] = SELECTED_PROGRAM_LEVELS_VALUES

            self.filters["filter"]["program_level"] = SELECTED_PROGRAM_LEVELS_VALUES

    def _intakes_filter(self):

        INTAKES_DATA = self.SCHOOLS_DATA["filterOptions"]["intakes"]

        INTAKES_LABELS = [intake["label"] for intake in INTAKES_DATA]

        SELECTED_INTAKES = self._get_user_choices(INTAKES_LABELS, "Intakes")

        SELECTED_INTAKES_VALUES = [intake["value"] for intake in INTAKES_DATA if intake["label"] in SELECTED_INTAKES]

        if len(SELECTED_INTAKES_VALUES) == 0:

            print("No Intake Selected.")
        
        else:

            # Updating filters

            self.filters["intakes"] = {"subValue":False,"value": SELECTED_INTAKES_VALUES}

            self.filters["filter"]["intakes"] = { "value": SELECTED_INTAKES_VALUES}

    def _intakes_status(self):

        INTAKE_STATUS_DICT = {
            "Open": "open",
            "Likely Open": "likely_open",
            "Will Open": "will_open",
            "Waitlist": "waitlist"
        }

        INTAKE_STATUS_KEYS = [key for key in INTAKE_STATUS_DICT.keys()]

        SELECTED_STATUSES = self._get_user_choices(INTAKE_STATUS_KEYS, "Intake Statuses")

        SELECTED_STATUSES_VALUES = [INTAKE_STATUS_DICT[key] for key in SELECTED_STATUSES]

        if len(SELECTED_STATUSES_VALUES) == 0:

            print("No Intake Status Selected")

        else:

            # Updating Filter
            self.filters["intake_status"] = SELECTED_STATUSES_VALUES

            self.filters["filter"]["intake_status"] = SELECTED_STATUSES_VALUES

    def _discipline_filter(self):

        CATEGORIES = self.SCHOOLS_DATA["filterOptions"]["categories"]

        CATEGORIES_LABELS = [category[0] for category in CATEGORIES]

        SELECTED_CATEGORIES = self._get_user_choices(CATEGORIES_LABELS, "Categories")

        SELECTED_CATEGORIES_VALUES = [category[1] for category in CATEGORIES if category[0] in SELECTED_CATEGORIES]

        if len(SELECTED_CATEGORIES_VALUES) == 0:

            print("No Category Selected")

        else:

            #Updating Filter

            self.filters["categories"] = SELECTED_CATEGORIES_VALUES

            self.filters["filter"]["categories"] = SELECTED_CATEGORIES_VALUES

    def _sub_category_filter(self, selected_categories_values):

        SUB_CATEGORIES_OPTIONS = list()

        SUB_CATEGORIES_OPTIONS.extend(option for sub_category in self.SCHOOLS_DATA["filterOptions"]["sub_categories"] if sub_category["value"] in selected_categories_values for option in sub_category["options"])

        SUB_CATEGORIES_OPTIONS_LABELS = list()

        SUB_CATEGORIES_OPTIONS_LABELS.extend(option["label"] for option in SUB_CATEGORIES_OPTIONS)

        SELECTED_SUB_CAT_LABELS = self._get_user_choices(SUB_CATEGORIES_OPTIONS_LABELS, "Sub Cateories")

        SELECTED_SUB_CAT_VALUES = [sub_cat["value"] for sub_cat in SUB_CATEGORIES_OPTIONS if sub_cat["label"] in SELECTED_SUB_CAT_LABELS]

        if len(SELECTED_SUB_CAT_VALUES) == 0:

            print("No Sub Category Selected")

        else:

            #Updating Filters
            self.filters["sub_categories"] = SELECTED_SUB_CAT_VALUES

            self.filters["filter"]["sub_categories"] = SELECTED_SUB_CAT_VALUES

    def _living_costs_filter():

        pass

    def programFilters():

        pass

programFilters = ProgramFilters()
# programFilters._program_level_filter()
# programFilters._intakes_filter()
# programFilters._intakes_status()
# programFilters._discipline_filter()
programFilters._sub_category_filter([2])

print(programFilters.filters)


