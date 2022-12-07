# Naprogramuj funkciu, ktorá bude vypisovať (resp.vracať) n-ty znak v poradi v danom reťazci, ak samozrejme existuje

def funk(a,b):
    if len(a)>=b:
        print(a[b-1])
    else:
        print('neexistujuci znak ')

funk('prazdniny',4)




