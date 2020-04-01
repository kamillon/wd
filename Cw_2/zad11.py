import math as m
n=0
while n < 3 or n >9:
    n=int(input("wprowadź wielkość diamentu między 3 a 9: "))
gora = m.ceil(n/2+1)
dol = m.floor(n/2) 

for i in range (1,gora):
    for j in range (gora-i):
        print(' ', end = '')
    for j in range (i*2 -1):
        print('o', end = '')
    print('')

for i in range (dol, -1, -1):
    for j in range (gora - i):  
        print(' ', end = '')    
    for j in range (i*2-1):
        print('o', end = '')
    print('')