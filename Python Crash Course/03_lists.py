def main():
    countries = ['Brazil', 'Portugal', 'USA', 'Germany']
    print('The list consists of:', countries)
    print('The first element is', countries[0])
    print('The last element is', countries[-1])

    cities = list(('Sao Paulo', 'Lisbon', 'New York', 'Berlin'))
    print('\nThe list consists of:', cities)
    print('The first element is', cities[0])
    print('The last element is', cities[-1])

    countries.insert(1, 'France')
    cities.insert(1, 'Paris')

    print('\nThe list of countries is now', countries)
    print('The list of cities is now', cities)

    countries.remove('Portugal')
    cities.remove('Lisbon')

    print('\nThe list of countries is now', countries)
    print('The list of cities is now', cities)

    continents = ['America', 'Europe']
    continents.clear()
    print('Continents: ', continents)

    print('\nPosition of USA in the list:', countries.index('USA'))

    new_list = [1,1,1,1,1,2,3,2,3,2,1,1]
    print('\nNew list:', new_list)
    print('Times that 1 appears:', new_list.count(1))

    print('new_list.pop(6)', new_list.pop(6))
    print('\nNew list:', new_list)
    print('Times that 1 appears:', new_list.count(1))

    list1 = [1,2,3]
    list2 = ['a','b','c']

    list1.clear()
    del list2

    print(list1)
    # print(list2)

    nested_list = [[1,2,3],[4,5,6],[7,8,9]]
    
    print('\nNested list: ', nested_list)

    for i in range(3):
        for j in range(3):
            print(nested_list[i][j])


if __name__ == '__main__':
    main()