# the following raises a type_error

tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_checker = len # this method is not getting called on any object, so this wont work
length_of_tweet = length_checker(tweet + 5)


# What does a TypeError indicate? Try running the above code, then use the resulting 
# error message to determine exactly what is wrong. (You don't have to fix this code.)