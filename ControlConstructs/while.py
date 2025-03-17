#WAC to print numbers from 1-10
i = 1
while(i<11):
    print(i)
    i=i+1
#WAC to print numbers from 1-5 but if number is equal to 3 dont print it.
for i in range(1,6):
    if(i == 3):
        continue
    else:
        print(i)
#WAC to print numbers from 1-10 but if number is equal to 5 then break the loop.
for i in range(1,11):
    if(i == 5):
        break
    else:
        print(i)
#WAC to print the table of given number in one line seperated by space.
num = int(input('Enter the number to print table'))
for i in range(1,11):
    print(i * num, end = " ")

