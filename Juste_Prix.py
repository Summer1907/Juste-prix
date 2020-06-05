#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
import time
import requests , json
from flask import Flask, session ,request, render_template

app = Flask(__name__)
app.secret_key = 'LOL'

@app.route('/',)
def index():
 session['number'] = random.randrange(1,100)
 Rep = session['number']
 return render_template("index.html",Rep=Rep)

@app.route('/invite', methods=['POST'])
def result():
 Rep = session['number']

 if  int(request.form['invite']) == session['number']:
    answer = "Parfait"
    return render_template("index.html", answer=answer, Rep=Rep)
 elif int(request.form['invite']) < session['number']:
      answer = "Plus"
      return render_template("index.html", answer=answer, Rep=Rep)
 else:
    answer = "Moins"
    return render_template("index.html", answer=answer, Rep=Rep)

def article():
 url = "https://api.cdiscount.com/OpenApi/json/Search"
 params = {
  "ApiKey": "ad97c8a1-51c3-4126-af03-4e7e27572933",
  "SearchRequest": {
    "Keyword": "TV",
    "SortBy": "",
    "Pagination": {
      "ItemsPerPage": 1
    },
    "Filters": {
      "Price": {},
      "IncludeMarketPlace": "false"
    }
  }
}
 response = requests.post(url, data=json.dumps(params))

 price = response.json()['Products'][0]['BestOffer']['SalePrice']
 description = response.json()['Products'][0]['Name']
 image = response.json()['Products'][0]['MainImageUrl']

 return render_template("index.html", price=price, description=description, image=image)









app.run(debug=True)