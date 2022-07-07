import random

n=int(input('začínam so sumou: '))
print('štart', end=' ')
sucet = 0
for i in range(1000):
    a=random.randint(1,20)
    b=random.randint(1,20)
    c=random.randint(1,20)
    if a == b == c:
        print('100',end=' ')
        n+=100
    elif a==b or b==c or a==c:
        print('5', end=' ')
        n+=5
    else:
        print('-1',end=' ')
        n-=1
    if n==0:
        break

print(f'zostalo mi {n} euro')
