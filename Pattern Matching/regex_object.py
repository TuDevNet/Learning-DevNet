import re

phoneNum = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
result = phoneNum.search("My phone number is: 415-555-4242.")
print("Phone number was found: " + result.group())

