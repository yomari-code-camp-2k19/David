########### Python 3.6 #############
import requests
import config
from config import intent_getter_key

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': intent_getter_key,
}
while True:
    params ={
        # Query parameter
        'q': str(input("Ask me about any news: ")),
        # Optional request parameters, set to default values
        'timezoneOffset': '0',
        'verbose': 'false',
        'spellCheck': 'false',
        'staging': 'false',
    }

    try:
        r = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/e0724d01-86be-4758-89b6-8baa568032d5',headers=headers, params=params)
        print(r.json())

    except Exception as e:
        print("[Errno {0}]".format(e))

    ####################################