import unittest
from user import User
from user import Credentials

class TestUser(unittest.TestCase):
    """
    TestUser class defines test that check the behaviours of users clas.
    """
    def tearDown(self):
        '''
        tearDown clears everything after every test has been run
        '''
        User.users_list = []
        Credentials.cred_list = []

    def setUp(self):
        '''
        setUp runs before the test cases.
        '''
        self.new_account = User ("Victor","ndungi12","twitter")
        self.new_cred = Credentials ("vexus12@gmail.com","0723456789")

    def user_init(self):
        '''
        user_init checks if the object has been initialized properly.
        '''
        self.assertEqual(self.new_account.user_name,"Victor")
        self.assertEqual(self.new_account.password,"ndungi12")
        self.assertEqual(self.new_account.site,"twitter")

        self.assertEqual(self.new_cred.gmail,"vexus12@gmail.com")
        self.assertEqual(self.new_cred.number,"0723456789")

    def test_save_cred(self):
        '''
        This test cases checks whether save_cred functions saves credentials.
        '''
        self.new_cred.save_cred()
        self.assertEqual(len(Credentials.cred_list),1)

    def test_add_user(self):
        '''
        Test case checks whether if an account is added everytime add_account function is called.
        '''
        self.new_account.add_account()
        self.assertEqual(len(User.accounts_list),1)

    def test_delete_account(self):
        '''
        Test case checks whether an account is account is deleted when delete_account is called.
        '''
        new_account = User ("Kivian","kivian12","instagram")
        new_account.add_account()
        User.delete_account(new_account)
        self.assertEqual(len(User.accounts_list),1)

    def test_display_account(self):
        '''
        This test case checks whether the listed items are the items in the accounts_list.
        '''
        self.assertEqual(User.display_account(),User.accounts_list)

    def test_find_account(self):
        '''
        This test case checks whether to check the find_account function.
        '''
        new_account = User ("Kivian","kivian12","instagram")
        new_account.add_account()
        found_acc = User.find_account("kivian12")

        self.assertEqual(found_acc.password,new_account.password)

if __name__ == '__main__':
    unittest.main()
