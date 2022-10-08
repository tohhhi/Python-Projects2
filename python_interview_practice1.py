# 1. Care sunt tipurile de date pe care le cunosti in Python? E BINEEE 

# Date mutabile: liste,dictionare, sets, array

# Date imutabile: string, tuple

# "CORECT : INT, FLOAT, STRING, HEX, "

# 2. Daca 'print(id(x))' afiseaza pe ecran 1705363112304, ce afiseaza 'print(id(y))' si de ce?

x = 5

y = 5

print(id(y), id(x)) 

# Arata id-ul locatiei  unde se stocheaza in memorie valoare lui x.

#  Care este timpul de memorie in care se stocheaza datale ?

# Datele se stocheaza in memoria RAM.


# 3. Ce inseamna mutabil si imutabil? Exemple de structuri de data mutabile si imutabile.

# Mutabil inseamna ca datele se pot fi accesate si modificate exemple: lits, dictionare, sets, array

# Imutabile care nu pot fi modificate: string si tuple.

# 4. Ce este afisat pe ecran si de ce?

message = '   python    '

print(message.strip())

print(message)


# Este afisat python cu spatii deoarece daca vrem ca funtia strip sa functioneze trebuie sa printam la momentul in care ii facem strip, sau sa creem o variabila care sa 
# egala cu funtia strip deoarece string ul este imutabil. Modificarea se face practic doar local.


# 5. Care sunt diferentele dintre liste si tuple ?
# Care sunt mai eficiente/ rapide, listele sau tuple?

# listele sunt mutabile si elementele din liste pot fi modificate iar tuple sunt imutabile.

# Tuple este mai rapid deoarece ocupa mai putina memorie.


#6. Cum extragi extensia unui fisier?

# extensia unui fisier este terminatia sa de dupa punct. Ex. fisier.py (fisier python), fisier.csv (fisier csv)

# 7. Ai un fisier test.py care contine urmatorul cod: 

def list_extension(*lists):
    new_list = []
    for list in lists:
        new_list += list
    return new_list

print(list_extension([1, 2, 3], [3, 100, 5.42], [6, 7, 8]))


# 8. Se introduce un numar de la tastatura (n).

# Reprezinta sirul lui Fibonacci care sa aiba n numere.


def fibonacci(n):
    a,b = 0,1

    while a < n:
        print(a)
        a,b = b,a+b
        

fibonacci(1000)