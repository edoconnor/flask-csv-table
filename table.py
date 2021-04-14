import os
import pandas as pd
from flask import Flask, render_template, request

table = Flask(__name__)

@table.route('/')
def index():
    df = pd.read_csv("data.csv")
    temp = df.to_dict('records')
    columnNames = df.columns.values
    return render_template('index.html', records=temp, colnames=columnNames)

if __name__ == '__main__':
    table.run(debug=True)