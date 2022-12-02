Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def calcWeeklyWages(totalHours, hourlyWage):
...     overtime = 0
...     doubletime = 0
...     if totalHours <= 40:
...         regularHours = totalHours
...     else:
...         overtime = totalHours - 40
...         regularHours = 40
...     if overtime > 20:
...         doubletime = overtime - 20
...         overtime = 20
...     return hourlyWage*regularHours + (1.5*hourlyWage)*overtime + (2*hourlyWage)*doubletime
... 
>>> def main():
...     hours = float(input('Enter hours worked: '))
...     wage = float(input('Enter dollars paid per hour: '))
...     total = calcWeeklyWages(hours, wage)
...     print('Wages for {hours} hours at ${wage:.2f} per hour are ${total:.2f}.'
...           .format(**locals()))
... 
...     
>>> main()
Enter hours worked: 50
Enter dollars paid per hour: 6
Wages for 50.0 hours at $6.00 per hour are $330.00.
