class Credentials():
    """
    This contains more details about the user class.
    """

    cred_list = []

    def __init__(self,gmail,number):
        self.gmail = gmail
        self.number = number

    def save_cred(self):
        '''
        This adds
        '''
        Credentials.cred_list.append(self)

    # @classmethod
    # def gen_password(cls)

class User:
    """
    Class for containing all the methods that run the application
    """

    accounts_list = []

    def __init__(self,user_name,password,site):
        self.user_name = user_name
        self.password= password
        self.site = site

    def add_account(self):
        '''
        add_user adds more accounts onto the user_list.
        '''
        User.accounts_list.append(self)

    def delete_account(self):
        '''
        delete_user deletes a saved account from user_list.
        '''
        User.accounts_list.remove(self)

    @classmethod
    def display_account(cls):
        '''
        display_users displays the list of accounts.
        '''
        return cls.accounts_list

    @classmethod
    def find_account(cls,password):
        '''
        find_user displays a specific account and its details.
        '''
        for user in cls.accounts_list:
            if user.password == password:
                return user
