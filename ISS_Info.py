import requests
from twilio.rest import Client

# All of this is to get give the credentials to twilio when you call the api
account_sid = '' # Account sid that can be found in your twilio account
auth_token = '' # auth token that can also be found in your twilio account
# Account sid and auth token 
client = Client(account_sid, auth_token)

# Calls the api for open-notify and gathers the information
r = requests.get('http://api.open-notify.org/astros.json')
people = r.json()
number_iss = people['number']


# function to run a for loop to grab the names of the astronauts in the ISS and add it to a list
def names():
    astro = []
    for p in people['people']:
        astro.append(p['name'])
    return astro


astronauts = (names())

# Writes the message that will be sent out
Message = 'Did you know there are currently ' + str(number_iss) + ' astronauts in the NASA ISS right ' \
                                                                  'now? Their names are ' + str(astronauts) + ' .'

# formulate the message that will be sent
message = client.messages.create(
    to="", # The phone number you are sending it to
    from_="", # Your twilio phone number that can be found in your twilio account
    body=Message)
