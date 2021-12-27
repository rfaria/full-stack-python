def main():
    value = int(input('Input an integer: '))

    if value % 2 == 0:
        print(value, 'is even.')
    else:
        print(value, 'is odd.')


if __name__ == '__main__':
    main()