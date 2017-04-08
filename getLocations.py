from googleads import oauth2
from oauth2client import client
from pprint import pprint
from googleads import adwords


import locale
import cPickle as pickle



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


def main(client):
    local_criterion_service = client.GetService('LocationCriterionService', version = 'v201702')

    location_names = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraksa", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

    #Create Selector
    selector = {
        'fields':['Id', 'LocationName', 'DisplayType', 'CanonicalName', 'ParentLocations', 'Reach', 'TargetingStatus'],
        'predicates':[{
            'field':'LocationName',
            'operator':'IN',
            'values':location_names[25:]
        },
        {
            'field':'Locale',
            'operator':'EQUALS',
            'values':['en']
        }]
    }

    # Make the get request.

    location_criteria = local_criterion_service.get(selector)
    #print location_criteria
    states_object = []
    for location_criterion in location_criteria:

        parent_string = ''
        if ('parentLocations' in location_criterion['location'] and location_criterion['location']['parentLocations']):
            parent_string = ", ".join([GetLocationString(parent) for parent in location_criterion['location']['parentLocations']])



            if (location_criterion['location']['displayType'] == 'State'):

                el = {'state':location_criterion['location']['locationName'], 'id':location_criterion['location']['id']}

                states_object.append(el)

            #     print ('The search term \'%s\' returned the location \'%s\' of type \'%s\''
            #    ' with parent locations \'%s\', reach \'%s\' and id \'%s\' (%s)'
            #    % (location_criterion['searchTerm'],
            #       location_criterion['location']['locationName'],
            #       location_criterion['location']['displayType'], parent_string,
            #       location_criterion['reach']
            #       if 'reach' in location_criterion else None,
            #       location_criterion['location']['id'],
            #       location_criterion['location']['targetingStatus']))

    print states_object
    with open('data2.p', 'wb') as fp:
        pickle.dump(states_object, fp)









main(adwords_client)
