# whjat will this output?

str1 = "hello there"
str2 = str1
str2 = "goodbye!"
print(str1)

# solution

# this will output "hello there" because the reassigment on line 5 simply unbinds the string
# "hello there" from variable str2 and binds it to the string "goodbye!"; this does not alter the
# object that str1 points to, which is still "hello there"