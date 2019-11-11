import unittest
from user import User

class TestUser(unittest.TestCase):
    """
    TestUser class defines test that check the behaviours of users clas.
    """
    def tearDown(self):
        '''
        tearDown clears everything after every test has been run
        '''
        User.users_list = []

    def setUp(self):
        '''
        setUp runs before the test cases.
        '''
        self.new_account = User ("Victor","ndungi12","twitter")

    def user_init(self):
        '''
        user_init checks if the object has been initialized properly.
        '''
        self.assertEqual(self.new_account.user_name,"Victor")
        self.assertEqual(self.new_account.password,"ndungi12")
        self.assertEqual(self.new_account.site,"twitter")


    def test_add_user(self):
        '''
        Test case checks whether if an account is added everytime add_account function is called.
        '''
        self.new_account.add_account()
        self.assertEqual(len(User.accounts_list),1)

    def test_delete_user(self):
        '''
        Test case checks whether an account is account is deleted when
        '''
        self.new_account.delete_account()


if __name__ == '__main__':
    unittest.main()
