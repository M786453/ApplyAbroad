import requests
import json

class ProgramDetails:

    def get_program_intakes(self, program_id):

        PROGRAM_DETAILS_URL = f"https://www.applyboard.com/api/v2/programs/{program_id}?include=program_intakes&fields%5Bprogram_intake%5D=general_status%2Cstart_date%2Copen_date%2Csubmission_deadline"

        headers = {
        "Cookie": "datadome=3y_uhsIaBwAAI9oXm5xuJwXU0I2qi97OE8eA-koMaGraECSxrm99dXbJUw1dZ3nTqvDrCguWExeuJxGk-X_KSeV2JkbHSmDEIL18QWJ6RvwzjnT_qLgcvx4C0BS1AtPD",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43",
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json, text/plain, */*, application/json",
        "Accept-Language": "en-US,en;q=0.9"
        }

        program_details_response = requests.get(PROGRAM_DETAILS_URL, headers=headers)

        program_intakes = json.loads(program_details_response.text)["included"]

        # Only those intakes which are not closed
        unclosed_program_intakes = [up_intake for up_intake in program_intakes if up_intake["attributes"]["general_status"] != "closed"]

        return unclosed_program_intakes
