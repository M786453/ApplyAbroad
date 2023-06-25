import requests
import json
from env import headers

class ProgramDetails:

    def get(self, program_id):

        PROGRAM_DETAILS_URL = f"https://www.applyboard.com/api/v2/programs/{program_id}?include=program_intakes%2Cprogram_requirement&fields%5Bprogram_intake%5D=general_status%2Cstart_date%2Copen_date%2Csubmission_deadline"

        program_details_response = requests.get(PROGRAM_DETAILS_URL, headers=headers)

        program_details = json.loads(program_details_response.text)

        print(program_details)

        if "included" in program_details.keys():

            program_details = json.loads(program_details_response.text)["included"]

            print("Scraping details of program with id '" + str(program_id) + "'")

            # Only those intakes which are not closed
            unclosed_program_intakes = list()

            program_requirement = dict()

            for item in program_details:

                if item["type"] == "program_intake":

                    if item["attributes"]["general_status"] != "closed":

                        unclosed_program_intakes.append(item)
                
                else:

                    program_requirement = item
                


            return unclosed_program_intakes, program_requirement
    
        else:

            return list(), dict()