import os
import robin_stocks as r

class TestStocks:
    def test_quotes():
        profile_info = r.get_quotes('spy')
        print(profile_info)
        assert profile_info

        
# class TestLogin:
#     @classmethod
#     def setup_class(cls):
#         print('setting up')
#         r.login(os.environ['robin_username'], os.environ['robin_password'])
     
#     @classmethod
#     def teardown_class(cls):
#         print('logging out')
#         r.logout()
        
#     def test_one():
#         profile_info = r.load_account_profile()
#         print(profile_info)
#         assert profile_info