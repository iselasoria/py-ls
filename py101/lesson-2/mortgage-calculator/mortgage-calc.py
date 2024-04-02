import json

with open('messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(msg):
    print(f'==> {msg}')


prompt(MESSAGES['initial_amount_request'])
requested_amount = float(input())

print(f"You're borrowing ${requested_amount}")
print(MESSAGES['apr_request'])
interest_rate = float(input())


print(MESSAGES['duration_request'])
loan_duration_years= int(input())

annual_interest_rate =float(interest_rate) / 100
monthly_interest_rate = annual_interest_rate / 12
months = float(loan_duration_years) * 12


monthly_payment = requested_amount * \
                            (monthly_interest_rate / \
                            (1 - (1 + monthly_interest_rate) ** (-months)))
print(f'You can expect to pay: ${monthly_payment:.2f}')