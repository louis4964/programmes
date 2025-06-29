import numpy as np 

def calcul_valeur_maison(S,t,n):
    M = 0.3 * S
    t = t / 12 
    n = n * 12 
    capital_emprunt = M*(1-(1 + t)**(-n))/ t 
    interets = M*n - capital_emprunt
    maison_valeur = capital_emprunt / 1.08 
    frais_notaire = maison_valeur * 0.08
    print(f"Le montant de vos intérêts est de {round(interets,2)} €.")
    print(f"La valeur du bien pouvant être acheté est de {round(maison_valeur,2)} et les frais de notaire seront de {round(frais_notaire,2)} €.")
    print(f"Ainsi pour que tous tienne dans votre budget de {round(M*n,2)}, il faudra faire un prêt de {round(maison_valeur,2)} €.")

"""
But :
Cette fonction permet d’estimer la valeur maximale d’un bien immobilier que l’on peut acheter sans apport personnel, 
en fonction d’une mensualité (M), d’un taux d’intérêt annuel (t) et d’une durée d’emprunt (n en années).

Paramètres :
S : Salaire de la personne (€),
t : taux d’intérêt annuel de l’emprunt (en pourcentage),
n : durée du prêt (en années).

Explication du code :
Le taux annuel est converti en taux mensuel (t/12), et la durée en mois (n*12). 
Les intérêts totaux sont calculés par la différence entre le total remboursé (M * n) et le capital réellement emprunté.
La valeur du bien est ensuite estimée comme étant égale au capital emprunté divisé par 1,08 (hypothèse d’augmentation du prix de 8%). 
Enfin, les frais de notaire sont estimés à 8% de la valeur du bien, et toutes ces informations sont affichées.

"""
# Favoriser la 2 -> plus facile a implementer dans logiciel

def calcul_apport_a_cote_pret(S,t,n,A):
    M = 0.3 * S
    t = t / 12 
    n = n*12
    F_N = 0.05
    capital_emprunt = M*(1-(1 + t)**(-n))/ t 
    interets = M*n - capital_emprunt
    maison_valeur = (capital_emprunt + A) / (1+F_N) 
    frais_notaire = maison_valeur * F_N
    print(f"Le montant de vos intérêts est de {round(interets,2)} €.")
    print(f"La valeur du bien pouvant être acheté est de {round(maison_valeur,2)} et les frais de notaire seront de {round(frais_notaire,2)} €.")
    print(f"Pour que tous tienne dans votre budget de {round(M*n,2)}, il faudra faire un prêt de {round(maison_valeur,2)} €.")

"""

But :
Cette fonction calcule la valeur d’un bien immobilier que l’on peut acheter avec un apport personnel A,
en plus d’un prêt dont les mensualités sont M, sur n années, avec un taux d’intérêt t, et des frais de notaire de
F_N (en proportion, ex : 0.08).

Paramètres :
S : Salaire de la personne (€),
t : taux d’intérêt annuel,
n : durée du prêt (en années),
A : montant de l’apport personnel (€),
F_N : taux des frais de notaire (en proportion, par exemple 0.08 pour 8%).

Explication du code :
Le calcul du capital emprunté est identique à celui de la première fonction. Les intérêts sont également obtenus de la même manière. 
Toutefois, ici, le budget total disponible est augmenté de l’apport personnel A, permettant d’acheter un bien plus cher. 
La formule de la valeur du bien devient :
Cela inclut les frais de notaire dans le prix total. Ces frais sont recalculés à partir de la valeur estimée. 
L’objectif est de déterminer le bien le plus cher possible tout en respectant les contraintes du budget et de l’apport.

"""



def calcul_apport_immobilier(
    salaire_mensuel,
    taux_annuel,
    duree_annees,
    apport,
    type_bien,
    taux_assurance,
    marge_securite,
    frais_dossier
):

    # Paramètres
    duree_mois = duree_annees * 12
    taux_mensuel = taux_annuel / 12
    assurance_mensuelle = taux_assurance * salaire_mensuel  # estimation par défaut

    # Capacité de remboursement mensuelle max avec marge de sécurité
    mensualite_max = 0.3 * salaire_mensuel * marge_securite - assurance_mensuelle

    # Calcul du capital empruntable
    if taux_mensuel > 0:
        capital_emprunt = mensualite_max * (1 - (1 + taux_mensuel) ** -duree_mois) / taux_mensuel
    else:
        capital_emprunt = mensualite_max * duree_mois  # cas taux 0

    # Frais de notaire estimés selon le type de bien
    taux_notaire = 0.075 if type_bien == "ancien" else 0.03
    
    # Prix total du bien pouvant être acheté
    budget_total = capital_emprunt + apport - frais_dossier
    prix_bien_ht_frais = budget_total / (1 + taux_notaire)
    frais_notaire = prix_bien_ht_frais * taux_notaire

    # Affichage
    print("=" * 40)
    print(f"Mensualité maximale (avec marge) : {round(mensualite_max, 2)} €")
    print(f"Montant emprunté possible : {round(capital_emprunt, 2)} €")
    print(f"Budget total disponible (apport inclus) : {round(budget_total, 2)} €")
    print(f"Prix estimé du bien (hors frais notaire) : {round(prix_bien_ht_frais, 2)} €")
    print(f"Frais de notaire estimés : {round(frais_notaire, 2)} €")
    print("=" * 40)
    
    """
    return {
        "mensualite_max": mensualite_max,
        "capital_emprunt": capital_emprunt,
        "prix_bien_ht_frais": prix_bien_ht_frais,
        "frais_notaire": frais_notaire,
        "budget_total": budget_total
    }
    """


"""
    Calcule la capacité d'achat immobilière maximale d'un foyer en fonction de son salaire, de l'apport, et des conditions d'emprunt.
    
    - salaire_mensuel : salaire brut mensuel (€)
    - taux_annuel : taux d'intérêt annuel du prêt (ex : 0.04 pour 4 %)
    - duree_annees : durée de l'emprunt en années
    - apport : apport personnel en euros
    - type_bien : "ancien" ou "neuf" (influence les frais de notaire)
    - taux_assurance : taux annuel de l’assurance emprunteur (par défaut 0.3 %)
    - marge_securite : pourcentage de prudence (par défaut 90 % de la capacité max)
    - frais_dossier : frais bancaires forfaitaires (par défaut 1000 €)
"""
