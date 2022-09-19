# -*- coding: UTF-8 -*-
from xml.sax.handler import feature_external_ges
import numpy as np
import app.model as model

import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/test_post', methods=['POST'])
def test():
    # 取得前端傳過來的數值
    insertValues = request.get_json()
    x= 1
    aa = insertValues[str(x)]
    return jsonify({'return': str(aa)})

@app.route('/test_predict', methods=['POST'])
def postInput():
    # 取得前端傳過來的數值
    insertValues = request.get_json()
    feature = ['gender ', 'bmi status', 'age', 'height', 'weight', 'BMI', 'sbp', 'dbp',
       'pulse', 'T-CHOL', 'LDL-C', 'HDL-C', 'AC', 'inbody score', 'weight.1',
       'bone weight', 'fat weight', 'bmi', 'fat rate', 'hydro l',
       'protein weight', 'mineral weight', 'hc-head', 'hc-neck', 'hc-breath',
       'hc-heart', 'hc-digest', 'hc-neural', 'hc-bone', 'hc-skin', 'hc-sleep',
       'hc-tScore', 'workout 30 min', 'rest time ', 'goal']
    print(insertValues)
    insertValues['age'] = (insertValues['age']-31 ) / ( 51-31 ) 
    insertValues['height'] = (insertValues['height']-155 ) / ( 182-155 )
    insertValues['weight'] = (insertValues['weight']-47.6 ) / ( 100-47.6 )
    insertValues['BMI'] = (insertValues['BMI']-19.07 ) / ( 34.38-19.07 ) 
    insertValues['sbp'] = (insertValues['sbp']-83 ) / ( 163-83 ) 
    insertValues['dbp'] = (insertValues['dbp']-56 ) / ( 98-56 ) 
    insertValues['pulse'] = (insertValues['pulse']-56 ) / ( 100-56 )
    insertValues['T-CHOL'] = (insertValues['T-CHOL']-133 ) / ( 250-133 ) 
    insertValues['LDL-C'] = (insertValues['LDL-C']-32 ) / ( 180-32 ) 
    insertValues['HDL-C'] = (insertValues['HDL-C']-26 ) / ( 150-26 )
    insertValues['AC'] = (insertValues['AC']-50 ) / ( 113-50 )
    insertValues['inbody score'] = (insertValues['inbody score']-59 ) / ( 83-59 ) 
    insertValues['weight.1'] = (insertValues['weight.1']-47.6 ) / ( 100-47.6 ) 
    insertValues['bone weight'] = (insertValues['bone weight']-18.8 ) / ( 56.2-18.8 ) 
    insertValues['fat weight'] = (insertValues['fat weight']-7.7 ) / ( 30.9-7.7 ) 
    insertValues['bmi'] = (insertValues['bmi']-18.4 ) / ( 34.38-18.4 ) 
    insertValues['fat rate'] = (insertValues['fat rate']-12.9 ) / ( 44.1-12.9 ) 
    insertValues['hydro l'] = (insertValues['hydro l']-25.8 ) / ( 54.0-25.8 ) 
    insertValues['protein weight'] = (insertValues['protein weight']-6.9 ) / ( 14.5-6.9 ) 
    insertValues['mineral weight'] = (insertValues['mineral weight']-2.42 ) / ( 5.09-2.42 ) 
    insertValues['workout 30 min'] = (insertValues['workout 30 min'] ) / ( 3-0 )

    x = []
    for i in feature:
        x.append(insertValues[i])
    print(x)
    input = np.array([[x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12],x[13],x[14],x[15],x[16],x[17],x[18],x[19],x[20],x[21],x[22],x[23],x[24],x[25],x[26],x[27],x[28],x[29],x[30],x[31],x[32],x[33],x[34]]])
    result = model.predict(input)
    return jsonify({'return': str(result)})