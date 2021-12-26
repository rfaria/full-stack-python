def greet_one(name):
    print('Hello to you,', name, end='!\n')

def greet_all(*names):
    print('\nHello to you all', end=', ')
    print(', '.join(*names), end='!')

def main():
    number = int(input('How many people should be greeted? '))
    
    name = []
    for i in range(number):
        print('Input the name of person number', i+1, end=': ')
        name.append(input())
        greet_one(name[i])

    greet_all(name)


if __name__ == '__main__':
    main()