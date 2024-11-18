
nyelvek = ['Python',  'C', 'C++', 'Java']
nyelvek2 = sorted(nyelvek)
print(nyelvek2)
print(nyelvek)

# sorbarendezi a listát
nyelvek.sort()
print(nyelvek)

# forditott sorba 
nyelvek.reverse()
print(nyelvek)

# az adott elem első előfordulásának indexe
print(nyelvek.index('C'))

#az adott elem hányszor fordul elő
print(nyelvek.count('Python'))

# nem listametódus,de így lehet eldönteni, hogy egy elemet tartalmaz e a lista 
print('C++' in nyelvek)
print('C+++' in nyelvek)

nev = "Hello"
print(nev.index('1'))