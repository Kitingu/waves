import uuid
from datetime import date

waves_db = []


class Wave:

    def __init__(self, title, details, user, category):
        self.title = title
        self.details = details
        self.user = user
        self.date_created = date.today().strftime("%d/%m/%Y")
        self.category = category

    def create_wave(self, ):
        waves_db.append({
            'wave_id':str(uuid.uuid4()),
            'title': self.title,
            'details': self.details,
            'user': self.user,
            'date_created': self.date_created,
            'category': self.category
        })
    @staticmethod
    def get_wave(id):
        return [wave for wave in waves_db if wave['wave_id'] == id ]

    @classmethod
    def get_waves(cls):
        return waves_db


# kali = Wave(1010,'khali makes peace with wizzo', 'sdfghjkdbgfe', 'kasee', 'buzz')
# id = 1010
# kali.create_wave()
# print(kali.get_wave(id))
# print(waves_db)
