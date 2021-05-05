import datetime

class Stock():
   
   def __init__(self, stock_symbol, stock_price):
      self._stock_symbol = stock_symbol
      self._stock_price = stock_price
      self._date_added = datetime.datetime.now()

   
