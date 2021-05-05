import datetime

class Stock():
   
   def __init__(self, stock_symbol, stock_price):
      symbol_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
      price_characters = set("1234567890.")
      if not(symbol_characters.issuperset(stock_symbol)):
         raise ValueError
      if not(price_characters.issuperset(stock_price)):
         raise ValueError
      self._stock_symbol = stock_symbol
      self._stock_price = stock_price
      self._date_added = datetime.datetime.now()

   def __str__(self):
      return f'Stock Symbol: {self._stock_symbol}, Stock Price {self._stock_price}'
