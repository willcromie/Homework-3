Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def main():
...     balance = float(input("enter initial balance: $ "))
...     rate = float(input("enter annual interest rate: "))
...     final = float(input("enter desired final balance: $ "))
...     y = 1
...     print("\nStarting Balance: %.2f \n" %(balance))
...     while (balance <= final):
...         balance = balance + (balance * rate)
...         print("\n Year: %d \t Balance: $%.2f " %(y, balance))
...         y = y + 1
... 
...         
>>> main()
enter initial balance: $ 500
enter annual interest rate: .04
enter desired final balance: $ 550

Starting Balance: 500.00 


 Year: 1 	 Balance: $520.00 

 Year: 2 	 Balance: $540.80 

 Year: 3 	 Balance: $562.43 
