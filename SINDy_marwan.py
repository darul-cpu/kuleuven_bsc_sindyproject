import numpy as np


def sindy(X, dt, threshold=0.1):
    #Main SINDy
    X_dot=afgeleide(X,dt)
    Theta, names=veelterm_library(X)
    Xi = stlsq(Theta, X_dot, threshold)
    return Xi, names

def afgeleide(X, dt):
    """
    Berekend afgeleide naar de tijd met numerieke differntiatie.
    """
    X_dot = np.gradient(X, dt, axis=0)

    return X_dot

def veelterm_library(X):
    #Veelterm kandidaat library tot graad 2, returns theta de kandidaat functie matrix en names is de lijst met symbolen van kandidaat library

    from itertools import combinations_with_replacement #genereerd combinaties waarbij dezelfde elementen kunnen voorkomen, dan moeten we alle mogelijkheden zelf niet moeten schrijven

    n_samples, n_variables = X.shape #geeft de dimensie van de X Numpy-array, n_samples is het aantal tijdstippen en n_variables het aantal toestandsvariabelen

    Theta = [np.ones(n_samples)] #maakt arrays van 1
    names = ["1"]
    #we hebben dus theta met enkel 1

    for i in range(n_variables):
        Theta.append(X[:, i]) #we selecteren de waarden en voegen die toe aan theta
        names.append(f"x{i + 1}")#we gebruiken fstring om symbolen toe te voegen 

    #Na deze loop hebben we dus theta die eruit ziet als [1,x1,x2,x3]
    
    for i, j in combinations_with_replacement(range(n_variables), 2):#we gaan nu elke combinatie uitvoeren en we gebruiken combinanties van 2 indices
        Theta.append(X[:, i] * X[:, j])#selecteert twee kolommen en vermeenigvuldigd , bv x1(t)*x2(t)
        names.append(f"x{i + 1}*x{j + 1}")#we gaan de naam opslaan van de vorige iteratie

    Theta = np.column_stack(Theta)#we plaatsen de arrays naast elkaar 

    return Theta, names



def stlsq(Theta, X_dot, threshold=0.1, max_iter=10):
    #We implementeren stlsq, wat doet het ? Het geeft terug de coefficienten matrix die we nodig hebben voor onze differntiaalvergelijking

    
    Xi = np.linalg.lstsq(Theta, X_dot, rcond=None)[0]#We berekenen eerst de gewone least squares oplossing, we proberen voor alle kandidaatfuncties de coefficienten te berekenen die de afgeleide zo goed mogelijk benaderen .

    for _ in range(max_iter):#We herhalen de iteratie

        for i in range(X_dot.shape[1]):#we behandelen ieder differntiaalvergelijking afzonderlijk

            small = np.abs(Xi[:, i]) < threshold #we zeggen dat de small zijn de coefficienten kleiner dan onze threshold, np.abs om absolute waarden te krijgen , small is een lijst van bolean waarden bv [True, False, False, True]
            Xi[small, i] = 0.0 #we stellen die smalls gelijk aan 0, dus voor elke coefficient geassocieerd met True /
            active = ~small #We selecteren enkel de overblijvende termen als small=True dan verwijderen we ze en als active = True, behouden we de term, ~draait de Bolean waarde om, zoals erboven vinden we dus bv dat active [False, True , True, False]

            if np.any(active):#Als er nog termen overblijven np.any geeft True terug als er minstens een in de lijst True is .
                Xi[active, i] = np.linalg.lstsq( Theta[:, active],X_dot[:, i],rcond=None)[0]#dus opnieuw de least squares maar zonder de smalls

    return Xi





