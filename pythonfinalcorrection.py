import random
print('Program to check the status of a random number in a given range ')
def even_or_odd(c):
    if c%2==0:
        print(c,'is an even number')
    else:
        print(c,'is an odd number')
def pos_or_neg(c):
    if c==0:
        print(c,'is neither a positive nor a negative number')
    elif c>0:
        print(c,'is a positive number')
    elif c<0:
        print(c,'is a negative number')
def prime_or_composite(c):
    if c==0 or c==1:
        print(c,'is neither a prime nor a composite number')
    else:
        ct=0
        if c>0:
            for i in range(1,c):
                if c%i==0:
                    ct+=1
            if ct>1:
                print(c,'is a composite number')
            else:
                print(c,'is a prime number')
        else:
            print(c,'is neither a prime nor a composite number')
A=input('Do you want to check status of a number(yes/no): ')
if type(int(A))==int:
    print('Please enter string value not integer.')
    A=input('Do you want to check status of a number(yes/no): ')
while (A=='Y' or A=='YES'or A=='Yes' or A=='yes' or A=='y'):
    a=int(input('Enter the starting range: '))
    b=int(input('Enter the ending range: '))
    if a>b:
        print('Enter correct range')
        a=int(input('Enter the starting range: '))
        b=int(input('Enter the ending range: '))
    c=random.randint(a,b)
    pos_or_neg(c)
    even_or_odd(c)
    prime_or_composite(c)
    A=input('Do you want to continue: ')
if (A=='N' or A=='No' or A=='no' or A=='n' or A=='NO'):
    print('Program ended')
