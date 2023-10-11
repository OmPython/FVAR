a = int(input('Enter the amount of annuity : '))
r = int(input('Enter the rate of interest p.a. : '))
y = int(input('Enter the number of years : '))
c = int(input('Enter the conversion period per year : '))

i = (r/c)/100
n = (y*c)

fvar = ((((1+i)**n)-1)/i)*a
print('Future value of annuity regular = ' + str(fvar))
