# predict the output of the code shown below. When you run it, do you see what you expected?

list1 = [2, 6, 4]
list2 = [2, 6, 4]

print(list1 == list2) # True
print(list1 is list2) # False

# in python, the == opperator checks for the contents of the list, since these lists contain the same elements, this comparison returns true
# however, if we use the `is` check, we get False. is checks for identity, and so since list1 and list2 are at different places in memory, they
# are not the same object
