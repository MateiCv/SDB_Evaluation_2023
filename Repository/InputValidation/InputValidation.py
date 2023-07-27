from datetime import datetime
import validators

class InputValidation:

    def check_id_validity(id:str):
        if not id.isnumeric():
            raise Exception("Invalid ID")

    def check_month_validity(month:str):
        if not month.isnumeric():
            raise Exception("Invalid Month, Provide Numeric Value")

    def check_word_validation(word: str):
        if not word.isalpha():
            raise Exception("Invalid Input")

    def check_city_validation(city:str):
        if city.isnumeric():
            raise Exception("Invalid Input")

    def check_numeric_value_validation(number:str):
        if not number.isnumeric():
            raise Exception("Invalid Input")

    def check_website_validity(url:str):
        if not validators.url(url):
            raise Exception("Invalid Url")


    def check_date_validity(date:str):
        try:
            res = bool(datetime.strptime(date, "%d.%m.%Y"))
            if not res:
                raise Exception("Invalid Input Data!")
        except ValueError:
            raise Exception("Invalid Input Data!")
