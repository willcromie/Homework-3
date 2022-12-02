Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def chooseEven(nums):
...     even=[]
...     for n in nums:
...         if n % 2==0:
...             even.append(n)
...         return even
... 
...     
>>> print(chooseEven([4,1,3,2,7]))
[4]
