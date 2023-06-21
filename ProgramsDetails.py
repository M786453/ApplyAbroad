import requests
import json
from env import AUTH_TOKENS

class ProgramDetails:

    def get(self, program_id):

        PROGRAM_DETAILS_URL = f"https://www.applyboard.com/api/v2/programs/{program_id}?include=program_intakes%2Cprogram_requirement&fields%5Bprogram_intake%5D=general_status%2Cstart_date%2Copen_date%2Csubmission_deadline"

        headers = {
        "Cookie": f"{AUTH_TOKENS}datadome=UCCZZoHWrb2t5vyfZSijf7mmwkdMng0fgS5dQgmPw24nLxJQXhG_SxjuKkR9Rh5T3jvfcdxjT10xFiONRxdu3MOPNBLF3jS14pEdwhSvSDOFAgiw54CF4~xNMR5eMjf;",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43",
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json, text/plain, */*, application/json",
        "Accept-Language": "en-US,en;q=0.9"
        }

        program_details_response = requests.get(PROGRAM_DETAILS_URL, headers=headers)

        program_intakes = json.loads(program_details_response.text)["included"]

        print("Scraping details of program with id '" + str(program_id) + "'")

        # Only those intakes which are not closed
        unclosed_program_intakes = list()

        program_requirement = dict()

        for item in program_intakes:

            if item["type"] == "program_intake":

                if item["attributes"]["general_status"] != "closed":

                    unclosed_program_intakes.append(item)
            
            else:

                program_requirement = item
                


        return unclosed_program_intakes, program_requirement
