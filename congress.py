Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def main():
...     age = int(input("Enter age: "))
...     length = int(input("Enter length of citizenship: "))
...     senator = False
...     citizen = False
...     if age >= 25 and length >= 7:
...         citizen = True
...     if age >= 30 and length >= 9:
...         senator = True
...     if senator and citizen:
...         print("you are eligible for the house and senate")
...     elif citizen:
...         print("you are eligible for the house")
...     else:
...         print("you are ineligible for congress")
... 
...         
>>> main()
Enter age: 30
Enter length of citizenship: 7
you are eligible for the house
>>> main()
Enter age: 30
Enter length of citizenship: 9
you are eligible for the house and senate
>>> main()
Enter age: 20
Enter length of citizenship: 5
you are ineligible for congress
