# without running, what will this print?

animal = 'horse'

match animal:
    case 'duck':
        print('quack')
    case 'squirrel':
        print('nook nook')
    case 'horse':
        print('neigh') ###### this code will print neigh because this is the statement that matches the case
    case 'bird':
        print('tweet tweet')
    case _:
        print('*cricket*') 