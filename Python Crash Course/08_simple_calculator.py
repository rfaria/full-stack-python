def main():

    keep_running = 'y'

    while(keep_running == 'y'):

        num1 = int(input('Input first number: '))
        num2 = int(input('Input second number: '))
        operator = input('Input operator: ')

        if operator == '+':
            print(num1+num2)
        elif operator == '-':
            print(num1+num2)
        elif operator == '*':
            print(num1*num2)
        elif operator == '/':
            print(num1/num2)
        else:
            print('Invalid operator.')
        
        keep_running = input('Keep running? [y/n]')


if __name__ == '__main__':
    main()