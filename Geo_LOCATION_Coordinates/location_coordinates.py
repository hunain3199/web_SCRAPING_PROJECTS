from geopy.geocoders import Nominatim
import time
geolocator = Nominatim(user_agent="scraper")
location = geolocator.geocode('Westbury')
time.sleep(.45)
latitudes = location.latitude
longitudes = location.longitude
print(location.latitude, location.longitude)