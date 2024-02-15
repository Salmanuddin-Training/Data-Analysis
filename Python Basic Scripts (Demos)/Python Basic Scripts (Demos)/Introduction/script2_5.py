x = 5; y = 10;
print('The value of x is {} and y is {}'.format(x,y))
#The value of x is 5 and y is 10'


#We can even use keyword arguments to format the string.
print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'John'))

#We can even format strings use the % operator to accomplish this, as we were doing in C Programming
x = 1240.3456789
print('The value of x is %3.2f' %x)
print('The value of x is %0.4f' %x)
