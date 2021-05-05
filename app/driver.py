'''
/***************************************************************
* Name: Final Project
* Author: Reed James
* Created: 4 May 2021
* Course: CIS 189 - Python
* Version: Python 3.7.5
* OS: Windows 10
* Copyright: This is my own original work based on
*               specifications issued by our instructor
* Description: Python program for picking stocks
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access to my program.
***************************************************************/
'''
from package import *
import tkinter


if __name__ == "__main__":

    main_window = tkinter.Tk()
    main_window.geometry("500x500")

    main_window.title("Stock Picker")

    person = Free_Account('1', 'John', 'Doe', '20000')
    stock_1 = Stock('TSLA', '670.60')
    stock_2 = Stock('AAPL', '125.43')
    person.add_stock(stock_1)
    person.add_stock(stock_2)
    print(person.display())
    print('Hello World')
    

    main_window.mainloop()