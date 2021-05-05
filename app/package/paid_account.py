from .free_account import *

class Paid_Account(Free_Account):

    def __init__(self, account_ID, first_name, last_name, account_balance):
        super().__init__(self, account_ID, first_name, last_name, account_balance)
