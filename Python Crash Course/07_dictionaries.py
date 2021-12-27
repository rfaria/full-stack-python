def main():
    my_dict = {'name': ['Rodrigo', 'Jessica'], 
    'age': [32, 29]}

    print(my_dict['name'])
    print(my_dict['age'])

    my_dict['name'].append('John Doe')
    my_dict['age'].append(47)

    print(my_dict['name'])
    print(my_dict['age'])


if __name__ == '__main__':
    main()