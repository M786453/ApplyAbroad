from EligibilityFilters import EligibilityFilters
from SchoolFilters import SchoolFilters
from ProgramFilters import ProgramFilters

class Filters(EligibilityFilters, SchoolFilters, ProgramFilters):


    def get(self):

        self.mainFilters()

        self.eligibilityFilters()

        self.schoolFilters()

        self.programFilters()

        return self.filters

    