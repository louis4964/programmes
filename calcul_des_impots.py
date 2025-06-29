from math import *

def impots(adult_parts, E, e, R, Pension, verbose=True):
    
    def fiscalité(quotient):
        if quotient < 11497:
            return 0
        elif 11498 <= quotient < 29315:
            return 0.11 * (quotient - 11498)
        elif 29316 <= quotient < 83823:
            return 0.11 * 17817 + 0.3 * (quotient - 29316)
        elif 83824 <= quotient < 180293:
            return 0.11 * 17817 + 0.3 * 54507 + 0.4 * (quotient - 83824)
        else:
            return 0.11 * 17817 + 0.3 * 54507 + 0.4 * 96469 + 0.45 * (quotient - 180294)
    
    # Calcul des parts fiscales
    if e < 3:
        Parts = adult_parts + 0.5 * e
    else:
        Parts = adult_parts + 0.5 * (e - 1) + 1
    
    # Vérification des pensions
    if E > 0:
        if Pension > 6674 * E:
            raise ValueError("Pension trop élevée : maximum autorisé = 6 674 € par étudiant.")
        R_fiscal = R - Pension
    else:
        R_fiscal = R

    # Calculs
    quotient_f = R_fiscal / Parts
    impots_avec_qf = fiscalité(quotient_f) * Parts
    quotient_sans_qf = R / Parts
    impots_sans_qf = fiscalité(quotient_sans_qf) * Parts

    reduction_max = e * 1759
    gain_qf = impots_sans_qf - impots_avec_qf

    if gain_qf > reduction_max:
        impots_final = impots_sans_qf - reduction_max
        msg = f"Réduction QF plafonnée à {reduction_max} €."
    else:
        impots_final = impots_avec_qf
        if e == 0:
            msg = "Pas de réduction liée au quotient familial : aucun enfant à charge."
        else:
            msg = f"Réduction QF appliquée : {gain_qf:.2f} €."

    revenu_net = R - impots_final
    revenu_mensuel = revenu_net / 12

    if verbose:
        print("="*30)
        print(f"Vos impôts s'élèveront à {round(impots_final,2)} € cette année.")
        print(f"Soit un revenu après impôts de {round(revenu_net,2)} € soit {round(revenu_mensuel,2)} € par mois.")
        print(msg)
        print("="*30)

    return [impots_final, revenu_net, revenu_mensuel]

    
"""
La fonction impots calcule le montant de l'impôt sur le revenu en France à partir de plusieurs paramètres : 
le nombre d'adultes (A), d'enfants à charge (e), un indicateur (E) qui détermine si une pension est versée, 
le revenu annuel brut (R), et éventuellement une pension annuelle versée à un enfant étudiant (Pension). 

La première étape consiste à calculer le nombre de parts fiscales en fonction du foyer. 
Si une pension est versée, la fonction vérifie qu’elle ne dépasse pas le plafond légal (6674 € par enfant). 
Ensuite, le revenu imposable est transformé en "quotient familial", en divisant le revenu
(éventuellement réduit de la pension) par le nombre de parts.

L’impôt est ensuite calculé selon les tranches officielles du barème progressif de l'impôt français.
Enfin, la fonction affiche le montant total de l’impôt, le revenu net après impôts, ainsi que le revenu mensuel net. 
Elle retourne ces trois valeurs sous forme de liste.

"""   
print(impots(2,2,0,40000,8000))
