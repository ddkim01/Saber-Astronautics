#
# Author: David Kim (z5255322@ad.unsw.edu.au)
#
# Date: September 2022
#
# Task: Saber Astronautics Technical Test 3
#
# Function: Creates a REST API endpoint based on an external JSON file format which 
#           delivers SPEX data.
#
# Description: 
#
# Parameters: 
#
# Return: 
#
# Bugs: Accessing the localhost:5000/incomes yielded an error 
#     
#
# Sources: Learning flask => https://auth0.com/blog/developing-restful-apis-with-python-and-flask/
#
# Status: Tutorial
#
# =======================================================================================
#

# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "Hello, World!"

from flask import Flask, jsonify, request

app = Flask(__name__)

incomes = [
  { 'description': 'salary', 'amount': 5000 }
]

@app.route('/incomes')
def get_incomes():
  return jsonify(incomes)

@app.route('/incomes', methods=['POST'])
def add_income():
  incomes.append(request.get_json())
  return '', 204
