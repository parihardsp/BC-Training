import re

email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
text = "Contact us at john.doe@example.com or support@company.co"
text1= "New Contact us at john.doe@example.com or support@company.co.uk"

emails = re.findall(email_pattern, text1)
print(emails)


date_pattern = r'\d{2}/\d{2}/\d{4}'
text = "Birthdate: 12/25/1990, Anniversary: 03/08/2005"

dates = re.findall(date_pattern, text)
print(dates)


print('-'*100)
main_text="John Doe is a regular customer at our store. His email is john.doe@example.com, and you can reach him at (123) 456-7890." \
          " John's address is 123 Main Street, Anytown, USA. He often shops for groceries and household items."

main_pattern=r'(j|J)ohn'
print(re.findall(main_pattern, main_text))

contacts = [
    "John Doe",
    "Alice Smith",
    "Allen Donald",
    "Bob  Johnson",
    "Ella  Brown",
    "David  Lee",

]

regex='^\w+\s\w+$'      #Last 3 names has 3 widespaces so they will not be returned, instead write \s+
for name in contacts:
    result=re.search(regex,name)
    if result:
        print(name)

print()
regex='A\w'
for name in contacts:
    match=re.search(regex,name)
    if match:
        print(name)
        print(match.span())
        print(match.group())



