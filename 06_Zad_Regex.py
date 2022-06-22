'''Napisati regex za provjeru validnosti unosa e-maila. E-Mail mora biti formata ime.prezime@fpmoz.sum.ba Nakon toga napisati regex za provjeru eduId koji mora biti formata iprezimeX@sum.ba gdje je i prvo slovo imena + prezime. X predstavlja bilo koji broj (moze ici u beskonacnost), a taj broj ne mora postojati (može biti samo iprezime@sum.ba). Od korisnika zatražiti unos maila i eduid te ispisati uspješnost. Istražiti greedy i non-greedy quantifiers.'''

import re

ime = input('Unesite ime: ')
prezime = input('Unesite prezime: ')

regex_fpmoz = "(^[a-z]{2,15})[.]([a-z]{2,15})([@]fpmoz[.]sum[.]ba$)"
regex_sum = "^" + ime.lower()[0] + prezime.lower() + "(\d*[@]sum[.]ba$)"

while 1:
    unos = input('Unesite @fpmoz.sum.ba mail: ')
    unos2 = input('Unesite @sum.ba mail: ')
    test = re.match(regex_fpmoz, unos)
    test2 = re.match(regex_sum, unos2)
    if test and test2:
        print('Uspjesno ste unijeli email adrese!')
        break
    elif not test:
        print('Neispravan format @fpmoz.sum.ba adrese!')
    elif not test2:
        print('Neispravan format @sum.ba adrese')
