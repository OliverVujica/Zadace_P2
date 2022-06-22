'''Iz podataka učitanih iz datoteke rezultati.csv sortirati listu po prezimenima.
Napraviti novi rječnik gdje će se po bodovnom rangu upisivati broj ostvarenih ocjena.'''

from csv import reader

rjecnik = {
    'nedovoljan' : 0,
    'dovoljan' : 0,
    'dobar' : 0,
    'vrlo dobar' : 0,
    'izvrstan' : 0
}

with open('rezultati.csv', 'r', encoding='utf8') as read_obj:
    csv_reader = reader(read_obj)
    studenti = list(map(tuple, csv_reader))

for ime, prezime, bodovi in studenti:
    if int(bodovi) < 50:
        rjecnik['nedovoljan'] += 1
    elif int(bodovi) <= 65:
        rjecnik['dovoljan'] += 1
    elif int(bodovi) <= 80:
        rjecnik['dobar'] += 1 
    elif int(bodovi) <= 90:
        rjecnik['vrlo dobar'] += 1   
    else:
        rjecnik['izvrstan'] += 1

for broj in rjecnik:
    print('Ocjena:', broj, ',', ' ', 'Ukupni broj ocjene:', rjecnik[broj])