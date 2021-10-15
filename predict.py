import numpy as np
import pickle

def predict(pregnancies, glucose, bloodpressure, skinthickness, insulin, bpi, dbfunc, age, model_name):
    filename = model_name+".sav"
    model = pickle.load(open(filename, "rb"))
    y_pred = model.predict(
        np.array([
            [
                pregnancies,
                glucose,
                bloodpressure,
                skinthickness,
                insulin,
                bpi,
                dbfunc,
                age]]))

    return y_pred[0]