# Naprogramuj funkciu samohlaskovy(retazec), ktora bude mat jeden parameter a to retazec. Funkcia bude zistovať či je reťazec samohlaskovy

s=['i','o','a','u','e','y']

def sam(t):
    x= False
    for i in range (0,len(t)):
        if t[i] in s:
            x = True
        else:
            x = False
            break
    print(x)

sam("uoiey")



