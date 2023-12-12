import re

with open("7.txt", "r") as f:
    data = f.read()
    names = re.findall(r'Mr.+|Mrs.+|Ms.+', data)
    print(names)
    website = re.findall(r'www.+com|www.+in|plus.+com', data)
    print(website)
    emails = re.findall(r'.+@.+',data)
    print(emails)
    phone = re.findall(r'\d+\*\d+\*\d+|\d{8}|\d+\-\d+\-\d+',data)
    print(phone)