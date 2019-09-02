#simple solution
for i in range(1,101):
    if i%3 == 0 and i%5==0:
        print "FizzBuz"
    elif i%3 == 0:
        print "Buzz"
    elif i%5==0:
        print "Fizz"

    else:
        print str(i)


#solution with own modulo
def mod(x, y):
    remainder=x
    while remainder >= y:
        remainder -= y
    return remainder

#another modulo function
def mod2(x, y):
    return  (x-int(x/y)*y)

for i in range(1,101):  
    if mod2(i,3) == 0 and mod2(i,5)==0:
        print "FizzBuz"
    elif mod2(i,3) == 0:
        print "Buzz"
    elif mod2(i,5) ==0:
        print "Fizz"

    else:
        print str(i)



