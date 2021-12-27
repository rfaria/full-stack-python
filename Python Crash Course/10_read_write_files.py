def main():
    try: 
        countries_file = open('countries.txt', 'r')

        print('Is readable:', countries_file.readable())
        # print('First line:', countries_file.readline())
        # print('File content:', countries_file.readlines())

        for row in countries_file.readlines():
            print(row)

        countries_file.close()
    except:
        print('Something went wrong.')

    
    try:
        countries_file = open('countries_new.txt', 'w')

        countries_file.write('USA')
        countries_file.write('\nEngland')

        countries_file.close()

    except:
        print('Something went wrong.')


    try:
        countries_file = open('countries.txt', 'a')

        countries_file.write('\nUSA')
        countries_file.write('\nEngland')

        countries_file.close()

    except:
        print('Something went wrong.')

    
    try:
        python_file = open('python_file.py', 'w')
        python_file.write('print(\'This is a meta Python file\')')
    except:
        print('Something went wrong.')

if __name__ == '__main__':
    main()