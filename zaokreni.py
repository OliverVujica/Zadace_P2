'''Napisati rekurzivnu funkciju koja kao parametar prima string, a kao rezultat taj string ispisuje sa zada.'''

def obrni(string):
    if len(string) == 0:
        return string
    else:
        return obrni(string[1:]) + string[0]