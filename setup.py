from googleads import oauth2
from oauth2client import client
from pprint import pprint
from googleads import adwords
from flask import Flask

import locale
import cPickle as pickle

import json
# get this object
from flask import Response, send_from_directory



locale.setlocale(locale.LC_ALL, 'en_US')
client_id = "563744622690-ae6klrpf57gmugf4b8kdh4thsudd0hco.apps.googleusercontent.com"
client_secret = "oKMnHv0aGzec42-OL6MIASmB"

flow = client.OAuth2WebServerFlow(
    client_id = client_id,
    client_secret=client_secret,
    scope=oauth2.GetAPIScope('adwords'),
    user_agent='Test',
    redirect_uri = "http://localhost:8082"
)

auth_uri = flow.step1_get_authorize_url()

# print auth_uri

auth_code = "4/OnrImjz9Yd3oq8kE-qgzcOKQ-5YABAtOsx_2e10WH8Y#"


# credentials = flow.step2_exchange(auth_code)
#
# pprint(vars(credentials))

access_token = "ya29.GlsmBCJdOWhwEULh0O_IeTMPAhCkCgL1cbkrol-acHVqiyeOSbDYWSIeQM0hxtMWPOduBhO5XbW7RtSm0aKfnHtMHinkuFJpeZE0_mhcPZjNdrvdxsM9RtDdgItN"
refresh_token = "1/I1aqrBRCI9u8lKLUm0Aj3dNjY8gTsamf2Qtf0ezkpKI"
user_agent = "Test"

oauth2_client = oauth2.GoogleRefreshTokenClient(
    client_id, client_secret, refresh_token
)

print "Here"

developer_token = "bJwEPmlBGNvB7eCHtBL5BQ"

adwords_client = adwords.AdWordsClient(
    developer_token, oauth2_client, user_agent
)

print "Here"

adwords_client.SetClientCustomerId('280-678-2972')

states = [
    {'name':'Alabama', 'id':21133},
    {'name':'Arizona', 'id':21136},
    {'name':'California', 'id':21137},
    {'name':'California', 'id':21138},
    {'name':'California', 'id':21139},
    {'name':'California', 'id':21140}

]

def GetLocationString(location):
  return '%s (%s)' % (location['locationName'], location['displayType']
                      if 'displayType' in location else None)


def loadLocationStats(client):
    data = 0

    microAmounts = []

    with open('data.p', 'rb') as fp:
        data = pickle.load(fp)

    data2 = 0
    with open('data2.p', 'rb') as fp:
        data2 = pickle.load(fp)

    data.extend(data2)
    states = data

    for i in range(0, 10):
        traffic_estimator_service = client.GetService('TrafficEstimatorService', version = 'v201702')

        keywords = [
            #{'text':'alabama'}
            {'text':'miami dolphins'}
        ]

        keyword_estimates_requests = []
        for keyword in keywords:
            keyword_estimates_requests.append({
                'keyword':{
                    'xsi_type':'Keyword',
                    'matchType':'PHRASE',
                    'text': keyword['text']
                }
            })

        adgroup_estimate_requests = [{
            'keywordEstimateRequests': keyword_estimates_requests,
            'maxCpc':{
                'xsi_type': 'Money',
                'microAmount': '10000'
            }
        }]

        # Create campaign estimate requests.
        campaign_estimate_requests = []
        for state in states[i*5:i*5+5]:
            campaign_estimate_requests .append({
                'adGroupEstimateRequests': adgroup_estimate_requests,
                'criteria':[
                    {
                        'xsi_type':'Location',
                        'id': state['id'] # United States
                    },
                    {
                        'xsi_type': 'Language',
                        'id':'1000' # English
                    }
                ]
            })

        # Selector
        selector = {
            'campaignEstimateRequests':campaign_estimate_requests
        }

        estimates = traffic_estimator_service.get(selector)
        #print estimates
        campaigns = estimates['campaignEstimates']
        for index, camp in enumerate(campaigns):
             print states[index + 5*i], "$" + str(camp['adGroupEstimates'][0]['keywordEstimates'][0]['min']['averageCpc']['microAmount']/1000000.0)
             microAmounts.append({"name":states[index + 5*i]['state'], "microAmount":str(camp['adGroupEstimates'][0]['keywordEstimates'][0]['min']['averageCpc']['microAmount']/1000000.0)})
        # for est in estimates['campaignEstimates'][0]['adGroupEstimates'][0]['keywordEstimates']:
        #     print state['name'] , est['min']['impressionsPerDay']
    return microAmounts


app = Flask(__name__, static_url_path='')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/resources/<path:path>')
def send_resources(path):
    return send_from_directory('resources', path)

@app.route('/')
def root():
    return app.send_static_file('index_2.html')

@app.route("/api/data")
def getCpc():
    return Response(json.dumps(loadLocationStats(adwords_client)), mimetype='application/json')

app.run()
