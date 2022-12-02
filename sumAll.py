Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def main():
...     sum1 = 0
...     while True:
...         n = input("Enter a number: ")
...         sum1 = sum1 + int(n)
...         if int(n) == 0:
...             break
...     print("the sum of all numbers is: %d" %sum1)
... 
...     
>>> main()
Enter a number: 1
Enter a number: 2
Enter a number: 3
Enter a number: 4
Enter a number: 56
Enter a number: 78
Enter a number: 90
Enter a number: 0
the sum of all numbers is: 234
