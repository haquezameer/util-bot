import os
import requests

BASE_URL = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/en/'
HEADERS = {'app_id': os.environ['OD_APP_ID'],
           'app_key': os.environ['OD_APP_KEY']}


def getMeaning(word_id):
    URL = BASE_URL + word_id
    reqres = requests.get(URL, headers=HEADERS)
    if reqres.status_code == 200:
        res = reqres.json()
        word_meaning = res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
        return word_id + ' means ' + ': ' + word_meaning
    else:
        return 'something went wrong'
