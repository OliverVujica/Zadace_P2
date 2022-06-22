import random

imena = ['Richard', 'Kevin', 'Edward', 'Debbie', 'Adam', 'Norma', 'Christopher', 'Karen', 'Tami', 'Michael', 'John',
'Roseanna', 'Gerald', 'George', 'Vesta', 'Julie', 'Raymond', 'Janice', 'Susan', 'Kerry', 'Lorenzo', 'Holly', 'Dan',
'Sherri', 'William', 'Karey', 'Marion', 'Melissa', 'Vincent', 'Ruby']

prezimena = ['Arnold', 'Simmons', 'Velasco', 'Canada', 'Gibbs', 'Thompson', 'Rendall', 'Harris', 'Hendon', 'Lyles', 'Perez',
'Cleary', 'Hoyman', 'Hall', 'Baker', 'Fichter', 'Colantuono', 'Moose', 'Howard', 'Davis', 'Nutt', 'Cornett', 'Smith',
'Lemus', 'Beltran', 'Ho', 'Cook', 'Samuels', 'Rodriguez', 'Cano']

radnici = []

for i in range(15):
    rjecnik = {
        'ime' : random.choice(imena),
        'prezime' : random.choice(prezimena),
        'satnica' : round(random.uniform(4, 6), 2)
        }
    radnici.append(rjecnik)
    
for i in radnici:
    i['tjedni_sati'] = random.randint(20, 30)
    
ntorke = []    
for i in radnici:
    mnozenje = i['satnica'] * i['tjedni_sati']
    ntorka = (i['ime'], i['prezime'], mnozenje)
    ntorke.append(ntorka)
  
zbroj = 0
for ime, prezime, isplata in ntorke:
    zbroj += isplata
    
prosjek = zbroj / 15  
print('Ukupna isplata za tjedan', zbroj, 'Prosjecna isplata za tjedan', prosjek)

for ime, prezime, isplata in ntorke:
    if isplata > prosjek:
        print(ime, prezime)


