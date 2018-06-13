#################################################
# Extremely basic api call to google maps to get
# and understanding of how things work
#################################################


# Import libraries needed to run parsing and requests
import urllib.parse
import requests

# Main URL where we will be calling on the request
main_api = 'http://maps.googleapis.com/maps/api/geocode/json?'

# While true keeps the program alive even after 1st run through
while True:
    # We ask for user input for where they would like information on
    address = input('Enter a zip code: ')

    # Provide a quit option for user
    if address == 'quit' or address == 'q':
        break

    # This is where we will append our user input into the request
    # and print out the request URL sent to the API
    url = main_api + urllib.parse.urlencode({'address': address})
    print(url)

    # These lines provide the constructed URL where we will be finding all the Json data
    # This is where all our data pulled from the API is stored
    json_data = requests.get(url).json()
    #print(json_data)

    # This line lets us know if our query worked or not
    json_status = json_data['status']
    # print('API Status: ' + json_status)

    # Main loop which lets us 1. Verify status 2. parse through data with a loop 3. Display them to the user
    if json_status == 'OK':
        for each in json_data['results'][0]['address_components']:
            print(each['long_name'])

    # This line just shows our address formatted, the zip code we looked up
        formatted_address = json_data['results'][0]['formatted_address']
        print()
        print('Zip code is: ' + formatted_address)

