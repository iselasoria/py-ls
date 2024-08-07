"""
Building on the previous exercise, write a function that returns True or False based on whether
or not an inventory item (an ID number) is available. As before, the function takes
two arguments: an item ID and a list of transactions. The function should return True only if
the sum of the quantity values of the item's transactions is greater than zero. Notice that
there is a movement property in each transaction object. A movement value of 'out' will
decrease the item's quantity.

You may (and should) use the transactions_for function from the previous exercise.

I: int, list
O: list

Rules:
- sum of all quantity values for a specific item should be more than 1.
- an _out_ movement indicates that many items have been sold, so this reduces the stock
    - assuming the in/out is like +/-


DS:
I: list
Interim: dictionary
O: list

Algo:
- initialize inventory to 0
- use the inventory_items_transaction(dictionario) to get all the transactions for the specific number in question and store in list
- iterate over the list and with each run #  {"id": 101, "movement": 'in',  "quantity":  5}
    -  iterate over the dictionary
        - if the movement is out,
            - take away from inventory
        otherwise increase the movement by the quantity
- return inventory comparison of greater than 0
"""

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]
def transactions_for(inventory_item, inventory_list):
    return [tiny_dict for tiny_dict in transactions if tiny_dict["id"] == inventory_item]


def is_item_available(product_id, transactions):
    product_inventory_transactions = transactions_for(product_id, transactions)

    inventory = 0

    for product in product_inventory_transactions:
        if product['movement'] == 'in':
            inventory += product['quantity']
            # print(f"Inventory is now: {inventory}")
        else:
            inventory -= product['quantity']
            # print(inventory)
    return inventory > 0

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True