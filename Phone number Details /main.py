import phonenumbers
from phonenumbers import timezone,geocoder,carrier

number=input("Enter your phone number(with country code): ")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
region=geocoder.description_for_number(phone,"en")
print(phone)
print("Time Zone: " + str(time))
print("Service Provider: "+ car)
print("Region: " + region)
