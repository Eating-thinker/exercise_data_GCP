# -*- coding: UTF-8 -*-
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
    x = []
    for i in range(35):
        x.append(insertValues[str(i)])
    input = np.array([[x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12],x[13],x[14],x[15],x[16],x[17],x[18],x[19],x[20],x[21],x[22],x[23],x[24],x[25],x[26],x[27],x[28],x[29],x[30],x[31],x[32],x[33],x[34]]])
    print(input)
    result = model.predict(input)
    return jsonify({'return': str(result)})

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=3000, debug=True)
    app.run(debug=True)