class account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def register():
    username = input('Create a username: ')
    password = input('Create a password: ')

    try:
        acc = account(username, password)
    except:
        print('Something went wrong.')

    print('Username \'', acc.username, '\' created successfully.')

    return acc

def login():
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    users_file = open('users.txt', 'r')
    passwords_file = open('passwords.txt', 'r')

    usernames = users_file.readlines()
    passwords = passwords_file.readlines()

    try:
        user_index = usernames.index(username+'\n')

        if password+'\n' == passwords[user_index]:
            print('Login successful!')
        else:
            print('Wrong password.')

    except:
        print('Username not found.')


def main():
    try:
        option = input('Register or Login [r/l]: ')
    except:
        print('Invalid option')
    
    if option == 'r':
        acc = register()

        users_file = open('users.txt', 'a')
        users_file.write(acc.username+'\n')

        passwords_file = open('passwords.txt', 'a')
        passwords_file.write(acc.password+'\n')

    elif option == 'l':
        login()

if __name__ == '__main__':
    main()

