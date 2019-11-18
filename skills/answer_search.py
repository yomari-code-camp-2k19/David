# import http.client, urllib.parse
# import json

# # Replace the subscriptionKey string value with your valid subscription key.
# subscriptionKey = 'fdcfb1d80954452ea0129d029083fa6b'

# host = 'https://api.labs.cognitive.microsoft.com'
# path = '/answerSearch/v7.0/search '


# while True:
#     query = str(input("Ask me anything: "))

#     params = '?q=' + urllib.parse.quote (query) + '&mkt=en-us'

#     def get_local():
#         headers = {'Ocp-Apim-Subscription-Key': subscriptionKey}
#         conn = http.client.HTTPSConnection (host)
#         conn.request ("GET", path + params, None, headers)
#         response = conn.getresponse ()
#         return response.read ()

#     result = get_local()
#     print (json.dumps(json.loads(result), indent=4))


import requests
import json
from config import answer_search_key

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': answer_search_key,
}
while True:
    params ={
        # Query parameter
        'q': str(input("Ask me about any news: ")),
        # Optional request parameters, set to default values
        'mkt': 'en-us'
    }

    try:
        r = requests.get('https://api.labs.cognitive.microsoft.com//answerSearch/v7.0/search',headers=headers, params=params)
        result =r.json()
        for value in list(dict(result.get('entities')).get('value')):
            print(dict(value).get('description') + '\n')
    except Exception as e:
        print("[Errno {0}]".format(e))

    ####################################