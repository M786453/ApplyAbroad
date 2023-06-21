import requests
import json

class ProgramDetails:

    def get_program_intakes(self, program_id):

        PROGRAM_DETAILS_URL = f"https://www.applyboard.com/api/v2/programs/{program_id}?include=program_intakes&fields%5Bprogram_intake%5D=general_status%2Cstart_date%2Copen_date%2Csubmission_deadline"

        headers = {
        "Cookie": "datadome=UCCZZoHWrb2t5vyfZSijf7mmwkdMng0fgS5dQgmPw24nLxJQXhG_SxjuKkR9Rh5T3jvfcdxjT10xFiONRxdu3MOPNBLF3jS14pEdwhSvSDOFAgiw54CF4~xNMR5eMjf",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43",
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json, text/plain, */*, application/json",
        "Accept-Language": "en-US,en;q=0.9"
        }

        program_details_response = requests.get(PROGRAM_DETAILS_URL, headers=headers)

        program_intakes = json.loads(program_details_response.text)["included"]

        print("Scraping intakes of program#" + str(program_id) + ".")

        # Only those intakes which are not closed
        unclosed_program_intakes = [up_intake for up_intake in program_intakes if up_intake["attributes"]["general_status"] != "closed"]

        return unclosed_program_intakes
