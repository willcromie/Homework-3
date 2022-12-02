Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def letterGrade(score):
...     if score < 60:
...         letter = 'F'
...     elif score < 70:
...         letter = 'D'
...     elif score < 80:
...         letter = 'C'
...     elif score < 90:
...         letter = 'B'
...     else:
...         letter = 'A'
...     return letter
... 
>>> def main():
...     x = float(input('Enter a numerical grade: '))
...     letter = letterGrade(x)
...     print('Your grade is ' + letter + '.')
... 
...     
>>> main()
Enter a numerical grade: 90
Your grade is A.
