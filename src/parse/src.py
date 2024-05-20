from parse_dal import Parse

from src.config import Config


class ParseAPIDecorator(Parse):
    def get_license_plates(self):
        return self.query_object("AI_Numberplate")["results"]


parse_DAL = ParseAPIDecorator(
    Config.PARSE_URL, 
    Config.PARSE_APP_ID, 
    Config.PARSE_MASTER_KEY
)