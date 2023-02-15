#===================================================
# The Entire Front End made by Mehmood Amjad i190472 
#===================================================
from flask import Flask, render_template, request

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import code

# TODO: reading from the database
def file_read():
    lines = []
    # TODO: reading from database file
    with open('database.txt') as f:
        lines = f.readlines()

    # TODO: seperating the results in a list
    s = ""
    count = 0
    for i in lines:
        s += lines[count]
        count += 1
    s = s.replace("\n",",")
    return list(s.split(","))


app = Flask(__name__)
# TODO: setting the root path 
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        pass
    else:
        return render_template('index.html')
#TODO: setting the path after student clicks the check result button
@app.route('/MCQ', methods=['POST', 'GET'])
def MCQ():
    if request.method == 'POST':
        pass
    else:
        # TODO: Implementing the code
        code.omr_scan()
        # TODO: reading from the database
        li = file_read()
        # TODO: displaying the webpage containing result from the database
        return render_template('display_mcq.html',length = len(li),data=li)
