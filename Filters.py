from EligibilityFilters import EligibilityFilters

class Filters(EligibilityFilters):


    def get(self):

        self.mainFilters()

        self.eligibilityFilters()

        return self.filters

    