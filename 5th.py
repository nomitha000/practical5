a=int(input('Enter year: '))
fh=open('output5.txt','w')
if(a%4==0):
    print('It is a leap year')
    fh.write('leap year')
else:
    print('Not a leap year')
    fh.write('not a leap year')

fh.close()
