nom = "Dupont"
prenom = "Jean"
age = 30

#print(f"Bonjour, je m'appelle {prenom} {nom} et j'ai {age} ans.")
#print(type(age))
liste=["mangue","papaye","avocat","banane"]
#for a in liste:
 #   print(a)

i=int(input("entrez un nombre entre 0 & 3 "))
if i<0:
    print("rééssayer")
elif i>3:
    print("rééssayer")
else:
    print(liste[i])