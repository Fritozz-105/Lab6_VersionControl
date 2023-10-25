def print_menu():
    # Prints the menu with options to encode a password, decode the password, and quit.
    print('Menu')
    print('-' * 13)
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()


def encode_pw(password):
    # Takes the user's input and uses a for loop to turn the input to an integer to add 3 to and then turns it back into
    # a string where it is added to the user_password return.
    user_password = ''
    for i in range(len(password)):
        if (int(password[i]) + 3) > 9:
            user_password = user_password + str((int(password[i]) + 3) - 10)
        else:
            user_password = user_password + str(int(password[i]) + 3)
    return user_password


def main():
    try:
        user_choice = 1
        while user_choice != 3:
            # While loop that runs until the user selects option 3.
            print_menu()
            user_choice = int(input('Please enter an option: '))
            if user_choice == 1:
                user_password = input('Please enter your password to encode: ')
                print('Your password has been encoded and stored!')
                print()
                encoded_password = encode_pw(user_password)
            elif user_choice == 2:
                print(f'The encoded password is {encoded_password}, and the original password is '
                      f'{user_password}.')
                print()
    except UnboundLocalError as excpt:
        print(f'Please set a password first, {excpt}')
    except:
        print('Unknown error occurred')


if __name__ == '__main__':
    main()
