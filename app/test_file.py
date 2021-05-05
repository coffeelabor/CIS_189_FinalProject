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

if __name__ == '__main__':
    unittest.main()
