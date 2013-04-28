#This program gets a password from the user and validates it.
import login

def main():
    #get a password from the user.
    password = input('Enter your password: ')

    #validate the password.
    while not login.valid_password(password):
        print('That password is not valid.')
        password = input('Enter your password: ')

    print('That is a valid password.')

main()