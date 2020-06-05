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
 return render_template("index.html",)

@app.route('/invite', methods=['POST'])
def result():
 
 if  int(request.form['invite']) == session['number']:
    answer = "Gagner ! "
    return render_template("index.html", answer=answer, )
 elif int(request.form['invite']) < session['number']:
      answer = "Plus"
      return render_template("index.html", answer=answer,)
 else:
    answer = "Moins"
    return render_template("index.html", answer=answer,)

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
 data = requests.post(url, data=json.dumps(params))

 image = data.json()['Products'][0]['MainImageUrl']
 price = data.json()['Products'][0]['BestOffer']['SalePrice']
 description = data.json()['Products'][0]['Name']

 return render_template("index.html", price=price, description=description, image=image)