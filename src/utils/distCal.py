import requests
import math    
api_key = 'AIzaSyDiB8cANSb9SnlY94TEA-y7NvLWOW3_Jdw'
# Change address format
# addr_from = address_from.replace(' ', '+')
# formatted_addr_to = address_to.replace(' ', '+')
# Geocoding API request with start address
geocode_from = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address=margao&sensor=false&key=AIzaSyDiB8cANSb9SnlY94TEA-y7NvLWOW3_Jdw').json()
if 'error_message' in geocode_from:
    print(geocode_from['error_message'])
if 'results' not in geocode_from or len(geocode_from['results']) == 0:
    print('No geocoding results found for the starting address')

# Geocoding API request with end address
geocode_to = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address=panjim&sensor=false&key=AIzaSyDiB8cANSb9SnlY94TEA-y7NvLWOW3_Jdw').json()
if 'error_message' in geocode_to:
    print(geocode_to['error_message'])

if 'results' not in geocode_to or len(geocode_to['results']) == 0:
    print('No geocoding results found for the destination address')

# Get latitude and longitude from the geodata
latitude_from = geocode_from['results'][0]['geometry']['location']['lat']
longitude_from = geocode_from['results'][0]['geometry']['location']['lng']
latitude_to = geocode_to['results'][0]['geometry']['location']['lat']
longitude_to = geocode_to['results'][0]['geometry']['location']['lng']

# Calculate distance between latitude and longitude
theta = longitude_from - longitude_to
dist = math.sin(math.radians(latitude_from)) * math.sin(math.radians(latitude_to)) + math.cos(math.radians(latitude_from)) * math.cos(math.radians(latitude_to)) * math.cos(math.radians(theta))
dist = math.acos(dist)
dist = math.degrees(dist)
miles = dist * 60 * 1.1515

# Convert unit and print(distance
unit = 'K'
if unit == 'K':
    print(round(miles * 1.609344, 2))
elif unit == 'M':
    print(round(miles * 1609.344, 2))
else:
    print(round(miles, 2))