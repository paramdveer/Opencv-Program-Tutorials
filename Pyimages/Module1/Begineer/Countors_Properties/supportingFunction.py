test = zip()

# referring a zip class
print('The type of an empty zip : ', type(test))

list1 = ['Alpha', 'Beta', 'Gamma', 'Sigma']
list2 = ['one', 'two', 'three', 'six']

test = zip(list1, list2)  # zip the values

print('\nPrinting the values of zip')
for values in test:
    print(values)  # print each tuples