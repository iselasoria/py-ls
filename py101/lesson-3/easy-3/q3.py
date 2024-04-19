# what will this code output?
str1 = "hello there"
str2 = str1
str2 = "goodbye!"
print(str1)

# hello there
# str1 is initialized and pointed to the string 'hello there'
# the second line intializes a variable str2 and points it to str1, which
# still references string 'hello there'
# then, str2 is _unplugged_ from the string 'hello there' and now points to
# the string 'goodbye!' but this does not change the fact that str1 is still pointing there
