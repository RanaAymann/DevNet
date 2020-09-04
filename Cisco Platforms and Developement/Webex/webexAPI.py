import requests

apiUrl = 'https://webexapis.com/v1/rooms'
access_token = 'your_access_token'

# your access token copy the brearer from the webex website

httpHeaders = {'Content-Type': 'application/json',
               'Authorization': 'Bearer ' + access_token}

queryParams = {'sortBy': 'lastactivity', 'max': '2'}

response = requests.get(url=apiUrl, headers=httpHeaders, params=queryParams)

print(response.status_code)
print(response.text)
