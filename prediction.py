import joblib
#import matplotlib as plt
import pandas as pd
import numpy as np
from PIL import Image
import os

curr_path = os.path.dirname(os.path.realpath(__file__))

feat_cols = ['clonesize', 'bumbles', 'andrena', 'osmia', 'MaxOfUpperTRange', 'RainingDays', 'fruitset', 'fruitmass',
             'seeds']

rf_final = joblib.load(curr_path + "/blueberry_model.sav")


def predict_yield(attributes: np.ndarray):
    """ Returns Blueberry Yield value"""

    pred = rf_final.predict(attributes)
    print("Yield predicted:")

    return pred[0]