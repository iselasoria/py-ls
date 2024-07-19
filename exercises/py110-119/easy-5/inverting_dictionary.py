"""
Given a dictionary where both keys and values are unique, invert this dictionary
so that its keys become values and its values become keys.

I: dict
O: dict

Rules:
- keys are to become values
- values are to become keys

DS:
dictionary

Algo:
- iterate over the dictionary
- with each run
    - append to a rolling variable the key and value into a tiny list --> ['apple','fruit']
    - reverse the list --> ['fruit','apple']
    - turn the list of lists into a dictionary and return

"""
def invert_dict(diccionario):
    list_of_lists = []

    for k, v in diccionario.items():
        par = [v, k]
        list_of_lists.append(par)

    new_dict = dict(list_of_lists)

    return new_dict

## with a dict comprehension
def invert_dict(di):
    return {value : key for key, value in di.items()}

print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      })== {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True