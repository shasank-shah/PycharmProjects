import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

ch_number = phonenumbers.parse("+919886489220", "CH")
country = geocoder.description_for_number(ch_number, "en")
print(country)

ro_number = phonenumbers.parse("+919886489220", "RO")
carr = carrier.name_for_number(ro_number, "en")
print(carr)