from datetime import datetime

class Book:
    name = str()
    last_update = datetime.now()
    creation_date = datetime.now()
    recipes_list = {
                    "starter": "",
                    "lunch": "",
                    "dessert": ""
                    }
