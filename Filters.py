from EligibilityFilters import EligibilityFilters
from SchoolFilters import SchoolFilters

class Filters(EligibilityFilters, SchoolFilters):


    def get(self):

        self.mainFilters()

        self.eligibilityFilters()

        self.schoolFilters()

        return self.filters

    