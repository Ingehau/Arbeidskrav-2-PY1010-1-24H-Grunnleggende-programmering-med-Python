# Arbeidskrav 2, PY1010-1-24H Grunnleggende programmering med Python

# Oppgave 1
# Spør først om hvilket år du er født.
# Regn ut hvor gammel du blir i løpet av år 2024.
alder = int(input("Hvilket år er du født? "))
alder_i_2024 = 2024 - alder
print("I 2024 blir du", alder_i_2024, "år gammel.")


# Oppgave 2
# Regn ut antall pizzaer
# Hver elev spiser 0.25 pizza. 
# Rund opp antall pizza til heltall.
import math

antall_elever = int(input("Skriv inn antall elever: "))
pizza_per_elev = 0.25
pizza_totalt = antall_elever * pizza_per_elev

# Rund opp til nærmeste hele pizza ved å bruke math.ceil.
pizza_rundet_opp = math.ceil(pizza_totalt)
print("Det må handles inn", pizza_rundet_opp, "pizzaer.")


# Oppgave 3
# Lag et program som regner om grader til radianer.
# Importer numpy for å bruke np.pi
import numpy as np

v_grad = float(input("Skriv inn gradtallet: "))
v_rad = v_grad * np.pi / 180
print("Gradtallet i radianer er:", v_rad)


# Oppgave 4
# a) Opprett en dictionary med land (keys), og info om hovedstad og antall innbyggere i millioner.
# b) Be brukeren om å skrive inn et land og skriv ut hovedstad og antall innbyggere.
# c) Programmet skal utvide dictionaryen med et nytt land som brukeren skriver inn.

data = {
    "England": {"hovedstad": "London", "innbyggere": 8.982},
    "Frankrike": {"hovedstad": "Paris", "innbyggere": 2.161},
    "Norge": {"hovedstad": "Oslo", "innbyggere": 0.697}
}

# b) Be brukeren om et land og skriv ut info
land = input("Skriv inn et land"): ")

# Antar at brukeren skriver inn et land som finnes i data
if land in data:
    hovedstad = data[land]["hovedstad"]
    innbyggere = data[land]["innbyggere"]
    print(hovedstad, "er hovedstaden i", land, 
          "og det er", innbyggere, "mill. innbyggere i", hovedstad)
else:
    print("Landet finnes ikke i dictionaryen data.")

# c) Be brukeren om info om et nytt land
nytt_land = input("Skriv inn navnet på et nytt land (som ikke finnes i data): ")
ny_hovedstad = input("Skriv inn hovedstaden i " + nytt_land + ": ")
ny_innbyggere = float(input("Skriv inn antall innbyggere (i millioner) i " + ny_hovedstad + ": "))

# Oppdater dictionaryen med ny informasjon
data[nytt_land] = {"hovedstad": ny_hovedstad, "innbyggere": ny_innbyggere}

# Skriv ut hele dictionaryen for å se at det ble oppdatert
print("Oppdatert dictionary:", data)


# Oppgave 5
# Funksjon som tar imot a og b og regner ut:
#  - arealet til en figur som består av en rettvinklet trekant + en halvsirkel
#  - "ytre" omkrets (samlet lengde av kantene + buen)
# I eksempelet antar vi at halvsirkelen har hypotenusen til trekanten som diameter.

def beregn_areal_og_omkrets(a, b):
    import math
    # Hypotenusen til trekanten
    c = math.sqrt(a**2 + b**2)
    
    # Areal av trekant
    areal_trekant = 0.5 * a * b
    
    # Areal av halvsirkel (diameter = c, radius = c/2)
    areal_halvsirkel = 0.5 * math.pi * (c/2)**2
    
    # Total areal
    areal = areal_trekant + areal_halvsirkel
    
    # Omkrets = side a + side b + halvsirkelens bue
    # Halvsirkelens bue = 1/2 av omkretsen til hel sirkel med diameter c
    # Omkrets hel sirkel = math.pi * c, så halv sirkel = 0.5 * math.pi * c
    omkrets = a + b + (0.5 * math.pi * c)
    
    return areal, omkrets

# Test funksjonen med input fra brukeren
a = float(input("Skriv inn verdi for a: "))
b = float(input("Skriv inn verdi for b: "))

areal, omkrets = beregn_areal_og_omkrets(a, b)
print("Figurens areal er:", areal)
print("Figurens omkrets er:", omkrets)


# Oppgave 6
# Kode som plotter funksjonen f(x) = -x^2 - 5 for x i intervallet [-10, 10].
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)
y = -x**2 - 5

plt.plot(x, y)
plt.title("f(x) = -x^2 - 5")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()
