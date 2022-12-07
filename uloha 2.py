#Naprogramuj funkciu, ktora bude mat jeden parameter a to retazec. Funkcia bude vracať počet číslic v reťazci.

def cisl(a):
    b=a
    x=0
    for i in range(0,len(a)):
        if b[i].isnumeric():
            x+=1
        else:
            x=x
    print(x)
cisl('asfa92 fasf124 31 ')





