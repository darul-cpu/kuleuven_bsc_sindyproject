def printdiff(Xi,names):
    variabelen=["x","y","z"]
    for i,variabel in enumerate(variabelen):
        verg=f"d{variabel}/dt="
        termen=[]
        for coefficient,name in zip(Xi[:,i],names):
            if abs(coefficient)>1e-10:
                terms.append(f"{coefficient:+.4f} {name}")
        verg+=" ".join(terms)
        print(verg)
