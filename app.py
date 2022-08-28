# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 21:25:00 2022

@author: valer
"""

# -*- coding: utf-8 -*-
import flask
import math
import numpy as np
import pickle
import pandas as pd
from flask import Flask, request, jsonify, render_template

# Use pickle to load in the pre-trained model

app = flask.Flask(__name__)
with open('Forest_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Initialise the Flask app
app = flask.Flask(__name__)



# (int)(request.form['personId'])



# Set up the main route
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('index.html'))
    
    if flask.request.method == 'POST':
        # Extract the input
        area = int(flask.request.form['area'])       
        
        # get the product
        rooms = int(flask.request.form['rooms'])
        
        area = np.log(area)

        # Make DataFrame for model
        input_variables = [[rooms, area]]

        # Get the model's prediction
        prediction = model.predict(input_variables)
    
        # Render the form again, but add in the prediction and remind user
        # of the values they input before
        return flask.render_template('index.html',
                                     original_input={'rooms':rooms,
                                                     'area':area},
                                     result=round(math.exp(prediction),2)
                                     )

if __name__ == '__main__':
    app.run(debug=True)

    
    


