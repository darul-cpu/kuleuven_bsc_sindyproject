def print_diffverg(Xi,names):
  for i in range(Xi.shape[1]):
    termen=[]
    for j in range(Xi.shape[0]):
      if Xi[j,i] != 0:
        coefficient=Xi[j,i]
        termen.append(f"{coefficient:+.4f}*{names[j]}")
    vergelijking=" ".join(termen)
    print(f"x{i+1}' = {vergelijking}")
        
