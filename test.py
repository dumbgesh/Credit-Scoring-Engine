import json

user_input = input('Enter dictionary as JSON: ')
borrower = json.loads(user_input)

print(borrower)