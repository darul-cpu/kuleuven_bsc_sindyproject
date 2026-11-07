def gaussische_ruis(X):
  gemiddelde=0
  standaardafwijking=0.1
  ruis= np.random.normal(gemiddelde,standaardafwijking,size=X.shape)
  return X+ruis
