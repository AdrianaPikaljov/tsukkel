import random
import math

# Ülesanne 15
count = 0
while True:
    elev = input("osta elevant ära! ")
    count += 1
    if "elevant" in elev.lower():  # Kui kasutaja vastuses on sõna "elevant"
        break  # Lõpeta, kui on õige vastus
print(f"sa vastasid {count} korda, enne kui mainisid elevanti.")

# Ülesanne 16
vaiksem, suurem = random.randint(1, 50), random.randint(51, 100)  # Genereeri juhuslik vahemik
secret = random.randint(vaiksem, suurem)  # Genereeri juhuslik arv valitud vahemikust
print(f"arva ara arv, mis on vahemikus {vaiksem}-{suurem} või kirjuta 'lõpp'!")
while True:
    arvamine = input("sinu pakkumine: ")
    if arvamine.lower() == "lõpp":  # Kui kasutaja kirjutab 'lõpp', siis mäng lõppeb
        break
    elif arvamine.isdigit() and int(arvamine) == secret:  # Kui kasutaja arv on õige
        print("oige vastus!")
        break
    else:
        print("Vale, proovi uuesti!")  # Kui pakkumine on vale, siis palub uuesti proovida

# Ülesanne 17
vert = int(input("mitu ruutu vertikaalselt? "))  # Küsi kasutajalt, mitu rida ruute
hor = int(input("mitu ruutu horisontaalselt? "))  # Küsi kasutajalt, mitu veergu ruute


# Lihtsustatud ruudustiku joonistamine: iga rida koosneb tekstilises vormis ruutudest
for y in range(vert): # Iga vertikaalse ruudu jaoks
    for i in range(hor):
        print("- " * vert)
        print("| " * hor)  # Kuvab ruudud horisontaalselt, iga rida sisaldab "hor" arvu ruute
        

# Ülesanne 18
N, M = random.randint(1, 10), random.randint(11, 20)  # Genereeri kaks juhuslikku arvu
print(f"{N}^2={N**2}, {N}^3={N**3}, {M}^2={M**2}, {M}^3={M**3}")  # Kuvab nende ruudud ja kuubid

# Ülesanne 19
n = int(input("mitu arvu sisestad? "))  # Küsi, kui palju arve sisestatakse
numbers = [float(input(f"Sisesta arv {i+1}: ")) for i in range(n)]  # Kogub kõik arvud kasutajalt
summa = sum(numbers)  # Arvutab kõikide sisestatud arvude summa
keskmine = summa / n  # Arvutab aritmeetilise keskmise
geom_keskmine = math.prod(numbers) ** (1/n)  # Arvutab geomeetrilise keskmise (korrutis kõikidest arvudest ja siis n-te juur)
korrutis = math.prod(numbers)  # Arvutab arvude korrutise
print(f"summa: {summa}, aritmeetiline keskmine: {keskmine}, geomeetriline keskmine: {geom_keskmine}, korrutis: {korrutis}")



# Ülesanne 20
numbers = [int(input(f"sisesta {i+1}. neljakohaline arv: ")) for i in range(4)]  # Kogub 4 neljakohalist arvu
print(f"suurim arv: {max(numbers)}, väikseim arv: {min(numbers)}")  # Kuvab suurima ja väikseima arvu
