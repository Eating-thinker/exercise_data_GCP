# -*- coding: UTF-8 -*-
import pickle
import gzip

# 載入Model
with gzip.open('app/model/randomForestModel.pgz','r') as f:
    randomForestModel = pickle.load(f)

def predict(input):
    pred=randomForestModel.predict(input)[0]
    print(pred)
    return pred