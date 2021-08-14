import os
import pickle
from sklearn.naive_bayes import GaussianNB

# define the class encodings and reverse encodings
classes = {1: "class_0", 2: "class_1", 3: "class_2"}
r_classes = {y: x for x, y in classes.items()}

# function to process data and return it in correct format
def process_data(data):
    processed = [
        {
            "alcohol": d.alcohol,
            "malic_acid": d.malic_acid,
            "ash": d.ash,
            "alcalinity_of_ash": d.alcalinity_of_ash,
            "magnesium": d.magnesium,
            "total_phenols": d.total_phenols,
            "flavanoids": d.flavanoids,
            "nonflavanoid_phenols": d.nonflavanoid_phenols,
            "proanthocyanins": d.proanthocyanins,
            "colour_intensity": d.colour_intensity,
            "hue": d.hue,
            "diluted_wines": d.diluted_wines,
            "proline": d.proline,
            "alochol_class": d.alcohol_class
        }
        for d in data
    ]

    return processed
