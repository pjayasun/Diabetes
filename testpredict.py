import numpy as np
import pickle

filename = "KNN.sav"
model = pickle.load(open(filename, "rb"))
y_pred_1 = model.predict(np.array([[10,125,70,26,115,31.1,0.205,41]]))

print("KNN", "\tOutcome :",y_pred[0])
