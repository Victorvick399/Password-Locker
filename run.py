#!/usr/bin/env python3.6
from user import Credentials
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

def find_existing_account(password):
    '''
    Function that check if a account exists with that number and return a boolean
    '''
    return User.find_account(password)

def display_account():
    '''
    This function returns all the saved user accounts.
    '''
    return User.display_account()

def main():
    print("Hello Welcome to your Password storage.What would you like to do?")

    while True:
            print("Use these short codes to further enjoy our app : ca - create a new account, da - display accounts, fa -find an already existing accounts, ex -exit the Password")

            short_code = input().lower()

            if short_code == 'ca':
                    print("")
                    print("-"*10)

                    print ("Enter your username ....")
                    user_name = input()

                    print("Enter your password or we can also generate one for you just type gen instead of your password.If not just enter your password......")
                    password = input()
                    if password == "gen":
                        password = f"@{user_name}12$"
                        print(f"Your password is {password}.")
                    else:
                        password = input

                    print("Where is this account from...")
                    site = input()

                    add_account(create_account(user_name,password,site))
                    print ('\n')
                    print(f"The new account of {user_name} has been created. Your password is {password}")
                    print ('\n')

            elif short_code == 'da':

                    if display_account():
                            print("Below is a list of all your saved accounts:")
                            print('\n')

                            for user in display_account():
                                    print(f"{user.user_name} your password is {user.password} .  \n This account belongs to {user.site}")

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
                            print(f"we've found it!!!! \n The username is{search_account.user_name} \n Password is{search_account.password}")
                            print("Do you want delete this account?? \n Type delete now..")
                            respo =input().lower().strip()
                            if respo =="delete" :
                                search_account.delete_account()
                            else:
                                continue
                    else:
                            print("That account does not exist")

            elif short_code == "ex":
                    print("Bye and have a wonderful day.")
                    break
            else:
                    print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':
    main()
