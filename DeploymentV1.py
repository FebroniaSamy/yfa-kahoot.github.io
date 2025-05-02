import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import datetime

with open('LRmodelV1.pickle', 'rb') as F:
    model = pickle.load(F)

def monopred(dist):
  x= datetime.now()
  tempData = {
  "Hours": [x.hour],
  "Years": [x.year],
  "Months": [x.month],
  "distance": [dist]
  }

  #load data into a DataFrame object:
  sPred = pd.DataFrame(tempData)

  Single_pred =model.predict(sPred)

  return round(list(Single_pred)[0],2)
