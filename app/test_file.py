import unittest
from package import stock as s
from package import free_account as fa 
from package import paid_account as pa 

class StockTest(unittest.TestCase):
    def setUp(self):
        self.stock = s.Stock('TSLA', '670.60')

    def tearDown(self):
        del self.stock
    
    def test_stock_contructor_values(self):
        self.assertEqual(self.stock._stock_symbol, 'TSLA')
        self.assertEqual(self.stock._stock_price, '670.60')

    def test_incorrect_stock_symbol(self):
        with self.assertRaises(ValueError):
            stock = s.Stock('1234', '670.60')

    def test_incorrect_stock_price(self):
        with self.assertRaises(ValueError):
            stock = s.Stock('TSLA', 'Hello')
    
    def test_stock_display(self):
        stock = s.Stock('TSLA', '670.60')
        test_string = 'Stock Symbol: TSLA, Stock Price 670.60'
        self.assertEqual(str(stock), test_string)

class FreeAccountTest(unittest.TestCase):
    def setUp(self):
        self.free_account = fa.Free_Account('1', 'John', 'Doe', '20000')
    
    def tearDown(self):
        del self.free_account

    def test_free_account_constructor_values(self):
        self.assertEqual(self.free_account._account_ID, '1')
        self.assertEqual(self.free_account._first_name, 'John')
        self.assertEqual(self.free_account._last_name, 'Doe')
        self.assertEqual(self.free_account._account_balance, '20000')
    
    def test_incorrect_first_name(self):
        with self.assertRaises(ValueError):
            person = fa.Free_Account('1', '123', 'Doe', '20000')

    def test_incorrect_last_name(self):
        with self.assertRaises(ValueError):
            person = fa.Free_Account('1', 'John', '123', '20000')
    
    def test_incorrect_account_balance(self):
        with self.assertRaises(ValueError):
            person = fa.Free_Account('1', 'John', 'Doe', 'hello')
    
    def test_incorrect_account_ID(self):
        with self.assertRaises(ValueError):
            person = fa.Free_Account('hello', 'John', 'Doe', '20000')
    
    def test_string(self):
        person = fa.Free_Account('1', 'John', 'Doe', '20000')
        self.assertEqual(str(person), 'Account ID: 1 First Name: John, Last Name: Doe, Account Balance: 20000')

    def test_add_stock(self):
        person = fa.Free_Account('1', 'John', 'Doe', '20000')
        stock_1 = s.Stock('TSLA', '670.60')
        stock_2 = s.Stock('AAPL', '125.43')
        person.add_stock(stock_1)
        person.add_stock(stock_2)
        self.assertEqual(len(person.stocks), 2)

    def test_display(self):
        person = fa.Free_Account('1', 'John', 'Doe', '20000')
        test_string = 'Account Holder: Doe, John\nAccount Balance: 20000\n'
        self.assertEqual(person.display(), test_string)
    
    def test_display_with_stocks(self):
        person = fa.Free_Account('1', 'John', 'Doe', '20000')
        stock_1 = s.Stock('TSLA', '670.60')
        stock_2 = s.Stock('AAPL', '125.43')
        person.add_stock(stock_1)
        person.add_stock(stock_2)
        test_string = 'Account Holder: Doe, John\nAccount Balance: 20000\nStock Symbol: TSLA, Stock Price 670.60\nStock Symbol: AAPL, Stock Price 125.43'
        self.assertEqual(person.display(), test_string)

if __name__ == '__main__':
    unittest.main()
