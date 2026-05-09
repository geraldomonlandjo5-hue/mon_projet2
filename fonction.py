def salaire_mensuel(salaire_annuel):
    salaire_mensuel = salaire_annuel / 12
    return salaire_mensuel
def salaire_hebdomadaire(salaire_mensuel):
    salaire_hebdomadaire = salaire_mensuel / 4
    return salaire_hebdomadaire
def salaire_horaire(salaire_hebdomadaire,heures_travaillées):
    salaire_horaire = salaire_hebdomadaire / heures_travaillées
    return salaire_horaire
a=int(input("entrez votre salaire annuel "))
b=int(input("entrez le nombre d'heures travaillées par semaine "))
print(f"Votre salaire mensuel est de {salaire_mensuel(a)} euros.")
print(f"Votre salaire hebdomadaire est de {salaire_hebdomadaire(salaire_mensuel(a))} euros.")
print(f"Votre salaire horaire est de {salaire_horaire(salaire_hebdomadaire(salaire_mensuel(a)),b)} euros.")
