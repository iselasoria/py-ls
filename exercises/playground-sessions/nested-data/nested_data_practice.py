"""
1. Write a Python function to retrieve the names of all managers in the company.
2. Explain how you would update the position of Bob in the engineering department from ‘developer’ to ‘senior developer’.
3. Write a Python code snippet to calculate the average age of employees in the sales department.
"""


company = {
    "engineering": [
        {"name": "Alice", "age": 29, "position": "developer"},
        {"name": "Bob", "age": 32, "position": "developer"},
        {"name": "Charlie", "age": 37, "position": "manager"}
    ],
    "hr": [
        {"name": "Dave", "age": 41, "position": "recruiter"},
        {"name": "Eve", "age": 36, "position": "manager"}
    ],
    "sales": [
        {"name": "Frank", "age": 28, "position": "salesperson"},
        {"name": "Grace", "age": 34, "position": "manager"}
    ]
}
###### Q1
def get_manager(company):
    managers = []

    for dpt in company:
        for person in company[dpt]:
            if person['position'] == 'manager':
                managers.append(person['name'])

    return managers


print(get_manager(company))


####### Q2 Change Bob's title to Senior Developer
company['engineering'][1]['position'] = 'Senior Developer'
print(company['engineering'][1]['position'])
print()

####### Q3
ages = [person['age'] for person in company['sales']]

avg = sum(ages) / len(ages)

print(avg)
