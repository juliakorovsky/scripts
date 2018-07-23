# script for posting to the site called Mokum (mokum.place) from the command line
# to run this script you should have reauests library installed

import requests
import uuid
import json
mokum_headers = {'Accept': 'application/json', 'Content-Type': 'application/json',
                 'X-River-Signature': 'Your River Signature', #To get this and the next value, read Mokum API docs
                 'X-API-Token': 'Your Mokum API Token'}
                 
my_text = str(input('Enter your post here:\n'))
my_data = {
  "post": {
    "timelines": ["user"],
    "text": my_text,
    "comments_disabled": 'false',
    "nsfw": 'false'
  },
  "_uuid": str(uuid.uuid4())
}

mokum_request = requests.get('https://mokum.place/api/v1/whoami.json', headers = mokum_headers) # This is only needed to ensure that you CAN login
print(mokum_request.status_code)

mokum_post = requests.post('https://mokum.place/api/v1/posts.json', data=json.dumps(my_data), headers=mokum_headers)
print(mokum_post.status_code) #Ensure server got your request
print(mokum_post.text) #See the result
