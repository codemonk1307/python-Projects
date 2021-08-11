

import phonenumbers
from phonenumbers import carrier

phone_number = phonenumbers.parse("Number with country code")

# this will print the country name 
print(geocoder.description_for_number(phone_number, 'en'))

# this will print the service provider's name
print(carrier.name_for_number(phone_number, 'en'))

# this will print the time zone of the call 
print(timezone.time_zones_for_number(phone_number))

