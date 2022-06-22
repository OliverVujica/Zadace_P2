'''Napraviti generator funkcije za ispis svih parnih i svih neparnih brojeva manjih od prosljeđenog parametra.'''

n = int(input('Unesite n: '))

def parni(n):
    a = 2
    while a < n:
        yield a
        a += 2
        
for i in parni(n):
    print(i)

print('------')

def neparni(n):
    a = 1
    while a < n:
        yield a
        a += 2

for i in neparni(n):
    print(i)