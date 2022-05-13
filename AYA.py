import random
import requests


class AyA():
    max_ayah = 6236
    
    audio_edition_list = ['abdullahbasfar', 'abdurrahmaansudais', 'abdulsamad',
                                'shaatree', 'alafasy', 'ahmedajamy', 'husary', 'hudhaify', 'minshawi']
    
    @classmethod
    def get_aya(cls):
        aya_number = random.randrange(1, cls.max_ayah)
        url = f'http://api.alquran.cloud/v1/ayah/{aya_number}/ar.{random.choice(cls.audio_edition_list)}'
        data = requests.get(url).json()
        return data
