# Loop over the elements of the fish_list list below, logging each one. 
# Terminate the loop immediately after printing the string 'Nemo'

fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

for f in fish_list:
    print(f)
    if f == 'Nemo':
        break