#mobile phone tracker mini project

import phonenumbers
from phonenumbers import geocoder

number = input("enter no. to check location")
ch_number = phonenumbers.parse(number,'CH')+

print(geocoder.description_for_number(ch_number, 'en'))

from phonenumbers import carrier

s_num=phonenumbers.parse(number, 'RQ')
print(carrier.name_for_number(s_num, 'en'))