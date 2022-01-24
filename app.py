from crypt import methods
from pickle import TRUE
from flask import Flask, render_template, request
import model
import numpy as np

app = Flask(__name__)

@app.route("/", methods= ['GET','POST'])
def profit():
    if request.method == "POST":
        Research = int(request.form["R&D"])
        Admin = int(request.form["Admin"])
        Market = int(request.form["Market"])
        Newyork = int(request.form["NewYork"])
        California = int(request.form["California"])
        int_cols = [[Research,Admin,Market,Newyork,California]]
        profit_pred = model.profit_prediction(Research=Research,Admin=Admin,Market=Market,State_N=Newyork,State_C=California)
        # print(profit_pred)
        mk = profit_pred
           
    return render_template("index.html", data = mk[0])

if __name__=="__main__":
    app.run(debug = True,host='0.0.0.0')