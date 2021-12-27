def main():
    try:
        number = int(input('Input a positive integer: '))
        print('The number is', str(number))
    except ValueError:
        print('Value is not an integer')

    # if not type(number) is int:
    #     raise TypeError("Only integers are allowed")

    if number < 0:
        raise Exception("Sorry, no numbers below zero")

    name = 'John Doe'

    try:
        print(name)
    except NameError:
        print('The variable \'name\' is not defined.')
    except:
        print('Something unexpected happened.')
    else:
        print('Nothing went wrong.')
    finally:
        print('The \'try except\' is finished.')


if __name__ == '__main__':
    main()