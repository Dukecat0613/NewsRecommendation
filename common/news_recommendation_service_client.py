# @Author: Dukecat
# @Date:   2017-05-02T23:27:09-04:00
# @Last modified by:   Dukecat
# @Last modified time: 2017-05-11T19:42:13-04:00





import pyjsonrpc

URL = "http://localhost:5050/"

client = pyjsonrpc.HttpClient(url=URL)

def getPreferenceForUser(userId):
    preference = client.call('getPreferenceForUser', userId)
    print "Preference list: %s" % str(preference)
    return preference
