# print the begging of the sentence all the way through "house"

advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as

print(advice.split("house")[0])
# the above code splits on "house" forming two elements in a list, and effectively removing the string "hourse"