def afisare_numere_impare():
    numere_impare =[]

    #generam primele 20 de nr impare
    for i in range(1,40,2):
        numere_impare.append(i)

    print("primele 20 numere impare: ", numere_impare)

# afisare_numere_impare()

def suma_numerelor():
    suma=0
    for i in range (1,101):
        suma=suma+i

    print("Suma totala:", suma)

# suma_numerelor()

def cel_mai_mare_divizor():
    a = int(input("Introdu primul numar: "))
    b = int(input("Introdu al doilea numar: "))

    while b:
        a,b = b, a % b
    print("Cel mai mare divizor comun:",a)

# cel_mai_mare_divizor()

def este_prim(n):
    if n <= 1:
        return False 
    for i in range(2, int(n ** 0.5) + 1):  
        if n % i == 0:
            return False  # daca este divizibil cu alt numar 
    return True
    if este_prim(numar):
        print(f"{numar} este un numar prim.")
    else:
        print(f"{numar} nu este un numar prim.")

#este_prim()

def suma_media_unei_liste():
    numere = input("Introduceti numerele separate prin spatiu: ").split()
    numere = [int(num) for num in numere]
    suma = sum(numere)
    media = suma / len(numere) if numere else 0
    print(f"Suma numerelor este: {suma}")
    print(f"Media numerelor este: {media:.2f}")

#suma_media_unei_liste()



def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
    elemente = input("Introduceti elementele separate prin spatiu: ").split()
    elemente_sortate = bubble_sort(elemente)
    print("Lista sortata:", elemente_sortate)


#bubble_sort()

def main():
    zile_saptamana = {
        1: "Luni",
        2: "Marti",
        3: "Miercuri",
        4: "Joi",
        5: "Vineri",
        6: "Sambata",
        7: "Duminica"
    }
    numar = int(input("Introduceti un numar de la 1 la 7: "))
    if 1 <= numar <= 7:
            print(f"Ziua saptamanii este: {zile_saptamana[numar]}")
    else:
            print("Numarul trebuie sa fie intre 1 și 7.")


#main()

