
class Free_Account():

    def __init__(self, account_ID, first_name, last_name, account_balance):
        name_characters = set(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        number_characters = set("1234567890")
        if not(name_characters.issuperset(first_name) and name_characters.issuperset(last_name)):
            raise ValueError
        if not(number_characters.issuperset(account_ID) and number_characters.issuperset(account_balance)):
            raise ValueError

        self._account_ID = account_ID    
        self._first_name = first_name
        self._last_name = last_name
        self._account_balance = account_balance
        self.stocks = []

    def __str__(self):
        return f'Account ID: {self._account_ID} First Name: {self._first_name}, Last Name: {self._last_name}, Account Balance: {self._account_balance}'

    def __repr__(self):
        return f'repr: {self._account_ID} {self._first_name} {self._last_name} {self._account_balance}'

    def add_stock(self, account_object):
        self.stocks.append(str(account_object))

    def display(self):
        return f'Account Holder: {self._last_name}, {self._first_name}\nAccount Balance: {self._account_balance}\n'+ '\n'.join(self.stocks)
        