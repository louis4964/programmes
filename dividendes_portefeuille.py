from math import*
import numpy as np 
import matplotlib.pyplot as plt

def Portefeuilles(
    investissement_P1, R1, D1, reinvest_P1,
    investissement_P2, R2,
    duree,
    mensualite_P1, m1,
    mensualite_P2, m2,
    dividendes_verses_dans_P2
):
    capital_P1 = investissement_P1
    capital_P2 = investissement_P2
    cash_flow_total = 0

    for _ in range(duree):
        if mensualite_P1.lower() == 'oui':
            capital_P1 += 12 * m1
        if mensualite_P2.lower() == 'oui':
            capital_P2 += 12 * m2

        dividendes_P1 = capital_P1 * D1

        if reinvest_P1.lower() == 'non' and dividendes_verses_dans_P2 =='non':
            cash_flow_total += dividendes_P1*0.7
            capital_P1 *= (R1 - D1)
        else:
            capital_P1 = capital_P1*(1 - D1*0.3)*R1

        if dividendes_verses_dans_P2.lower() == 'oui':
            capital_P2 += dividendes_P1

        capital_P2 *= R2

    print(f"--- Résultats après {duree} ans ---")
    print(f"Capital P1 : {round(capital_P1, 2)} €")
    print(f"Capital P2 : {round(capital_P2, 2)} €")
    print(f"Cash Flow encaissé (non réinvesti) : {round(cash_flow_total, 2)} €")
    print(f"Total patrimoine : {round(capital_P1 + capital_P2, 2)} €")
    print()
    return capital_P1 + capital_P2 

def patrimoine2(P_o,R,n,m):
    I = 0 
    for i in range (0,n+1):
        I += (1+R)**i
    
    P = P_o + m*12*I
    print(f'Votre patrimoine final sera de {round(P,2)} €')
    return P

def simulation(n):
    P_div = []
    P = []
    P_s_2 =[]
    dif = []
    t = np.linspace(0,n,n)
    for i in range(n):
        P.append(patrimoine2(2000,0.07,i,400))
        
        P_div.append(Portefeuilles(
          investissement_P1=2000, R1=1.07, D1=0.02, reinvest_P1='non',
          investissement_P2=0, R2=1.03,
          duree=i,
          mensualite_P1='oui', m1=400,
          mensualite_P2='non', m2=0,
          dividendes_verses_dans_P2='oui'))
        
        P_s_2.append(Portefeuilles(
          investissement_P1=2000, R1=1.07, D1=0.02, reinvest_P1='oui',
          investissement_P2=0, R2=1.03,
          duree=i,
          mensualite_P1='oui', m1=400,
          mensualite_P2='non', m2=0,
          dividendes_verses_dans_P2='non'))
        
        dif.append(P_div[i]-P[i])
        
    plt.plot(t,P_div,'r',label='Simulation avec dividendes et P2')
    plt.plot(t,P_s_2,'g',label='Simulation avec dividendes sans P2')
    plt.plot(t,P,'b',label='Simulation sans dividendes')
    #plt.plot(t,dif,'g--',label='evolution ecart patrimoine')
    plt.title(f"patrimoine S1 = {round(P_div[n-1],2)} \n et patrimoine S2 = {round(P[n-1],2)}\n et patrimoine S1 sans P2 = {round(P_s_2[n-1],2)}.")
    plt.grid(True)
    plt.legend()
    plt.show()

print(simulation(30))

"""print("Situation 1 : uniquement P1 sans mensualité (sans réinvest. D)")
Portefeuilles(
    investissement_P1=2000, R1=1.06, D1=0.02, reinvest_P1='non',
    investissement_P2=0, R2=1.03,
    duree=20,
    mensualite_P1='non', m1=0,
    mensualite_P2='non', m2=0,
    dividendes_verses_dans_P2='non'
)

print("Situation 2 : uniquement P1 sans mensualité (avec réinvest. D)")
Portefeuilles(
    investissement_P1=2000, R1=1.06, D1=0.02, reinvest_P1='oui',
    investissement_P2=0, R2=1.03,
    duree=20,
    mensualite_P1='non', m1=0,
    mensualite_P2='non', m2=0,
    dividendes_verses_dans_P2='non'
)

print("Situation 3 : P1 avec mensualité - 400e (sans réinvest. D)")
Portefeuilles(
    investissement_P1=2000, R1=1.06, D1=0.02, reinvest_P1='non',
    investissement_P2=0, R2=1.03,
    duree=20,
    mensualite_P1='oui', m1=400,
    mensualite_P2='non', m2=0,
    dividendes_verses_dans_P2='non'
)

print("Situation 4 : P1 avec mensualité - 400e (avec réinvest. D)")
Portefeuilles(
    investissement_P1=2000, R1=1.06, D1=0.02, reinvest_P1='oui',
    investissement_P2=0, R2=1.03,
    duree=20,
    mensualite_P1='oui', m1=400,
    mensualite_P2='non', m2=0,
    dividendes_verses_dans_P2='non'
)

print("Situation 5 : P1 avec mensualité - 400e (dividendes versés dans P2 sans mensualité)")
Portefeuilles(
    investissement_P1=2000, R1=1.06, D1=0.02, reinvest_P1='non',
    investissement_P2=0, R2=1.03,
    duree=20,
    mensualite_P1='oui', m1=400,
    mensualite_P2='non', m2=0,
    dividendes_verses_dans_P2='oui'
)

print("Situation 6 : P1 avec mensualité - 350e (dividendes versés dans P2 avec mensualité - 50e)")
Portefeuilles(
    investissement_P1=2000, R1=1.06, D1=0.02, reinvest_P1='non',
    investissement_P2=0, R2=1.03,
    duree=20,
    mensualite_P1='oui', m1=350,
    mensualite_P2='oui', m2=50,
    dividendes_verses_dans_P2='oui'
)

"""



"""
| Situation | Mensualité P1 | Réinvest. Dividendes P1 | P2 utilisé | Mensualité P2 | Source P2                     |
| --------- | ------------- | ----------------------- | ---------- | ------------- | ----------------------------- |
| 1         | Non           | Non                     | Non        | —             | —                             |
| 2         | Non           | Oui                     | Non        | —             | —                             |
| 3         | 400€/mois     | Non                     | Non        | —             | —                             |
| 4         | 400€/mois     | oui                     | Non        | —             | —                             |
| 5         | 400€/mois     | Non (versés dans P2)    | Oui        | Non           | Dividendes de P1              |
| 6         | 350€/mois     | Non (versés dans P2)    | Oui        | 50€/mois      | Dividendes de P1 + Mensualité |
"""