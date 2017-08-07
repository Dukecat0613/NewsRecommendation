import pyjsonrpc
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import parameters

# Recommendation_SERVER_PORT = 5050
URL = "http://" + parameters.SERVER_HOST + ":5050/"

client = pyjsonrpc.HttpClient(url=URL)

def getPreferenceForUser(userId):
    preference = client.call('getPreferenceForUser', userId)
    print "Preference list: %s" % str(preference)
    return preference
