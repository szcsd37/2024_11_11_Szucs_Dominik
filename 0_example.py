honapok = ['január', 'február', 'március', 'április,', 'május']

print(honapok)

# lista hossza: len()
print(len(honapok))

# 0. index elem
print(honapok[0])

# 1. index elem
print(honapok[1])

# üres lista létrehpzása
szamok = []
print(szamok)
# elem hozzáadása
for i in range (1, 11):
    szamok.append(i)       #append hozzáad elemeket
print(szamok[2])
print(szamok[9])
# túlindexelés
#print(szamok[10])

# utolsó elem megadása - hátulról első elem

print(szamok[-1])
print(szamok[-2])


