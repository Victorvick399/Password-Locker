#!/usr/bin/env python3.6

from user import User

def create_account(user_name,password,site):
     '''
     Function to create a new Password account.
     '''
     new_account = User(user_name,password,site)
     return new_account

def add_account(user):
    '''
    Function to add another acount.
    '''
    user.add_account()

def delete_account(user):
    '''
    Function is to delete a account.
    '''
    user.delete_contact()

def find_account(password):
    '''
    This function an account using a password and returns its details.
    '''
    return User.find_account(password)

def find_existing_account(user):
    '''
    Function that check if a contact exists with that number and return a boolean
    '''
    return User.find_account(password)

def display_accounts():
    '''
    This function returns all the saved user accounts.
    '''
    return User.display_account()

def main():
    print("Hello Welcome to your Password storage.What would you like to do?")

    while True:
            print("Use these short codes to further enjoy our app : ca - create a new account, da - display contacts, fa -find an already existing contact, ex -exit the Password")

            short_code = input().lower()

            if short_code == 'ca':
                    print("")
                    print("-"*10)

                    print ("Enter your username ....")
                    user_name = input()

                    print("Enter your password ...")
                    password = input()

                    print("Where is this account from...")
                    site = input()

                    add_account(create_account(user_name,password,site))
                    print ('\n')
                    print(f"The new account of {user_name} has been created. Your password is {password}")
                    print ('\n')

            elif short_code == 'da':

                    if display_accounts():
                            print("Below is a list of all your saved accounts:")
                            print('\n')

                            for contact in display_accounts():
                                    print(f"{user.user_name} your password is {user.password} .  '\n' This account belongs to {user.site}")

                            print('\n')
                    else:
                            print('\n')
                            print("You haven't saved any accounts.Type ca and create a new one now.")
                            print('\n')

            elif short_code == 'fa':

                    print("Please enter the password of the account you are searching for..")

                    searched_password = input()
                    if find_existing_account(searched_password):
                            search_account = find_account(searched_password)
                            print(f"{search_account.user_name} '\n' {search_account.password}")
                    else:
                            print("That account does not exist")

            elif short_code == "ex":
                    print("Bye and have a wonderful day.")
                    break
            else:
                    print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':
    main()
