x = input('Please enter a number: ')
print (x)

symbol = input('Please enter a calculation symbol: ')
print (symbol)

y = input('Please enter one more number: ')
print (y)

if symbol == '+':
    print (int(x)+int(y))
    
elif symbol == '-':
    print (int(x)-int(y))

elif symbol == '*':
    print (int(x)*int(y))

elif symbol == '/':
    print (int(x)/int(y))

else: print ('error')