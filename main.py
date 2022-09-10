from hashlib import algorithms_available
import io
from urllib import request
from flask import Flask, render_template,request, Response, jsonify, make_response, url_for,request, redirect
import numpy as np
# Imporint the bindings
import cppSortAlgorithms
import base64

# The matplot stuff
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():

    return render_template("base.html")

@app.route("/output",methods=["GET","POST"])
def output():

    algorithms = request.json['algorithms']
    size = request.json['size']
    size = int(size)

    #put the algorithm here# The random array to be sorted 
    randnums = np.random.randint(1,size+1,size)

    # The sorting algortims in c++, * use an if here for selection of the algorithm going to be used
    bubbleSortedNums = cppSortAlgorithms.bubble_sort(randnums.astype(np.intc))
    mergeSortedNums = cppSortAlgorithms.merge_sort(randnums.astype(np.intc))


    # Generate  random plot
    fig1 = Figure()
    axis1 = fig1.add_subplot(1, 1, 1)
    axis1.set_title("random")
    axis1.set_xlabel("value")
    axis1.set_ylabel("n")
    axis1.bar(range(size),randnums)

    # Generat bubble plot
    fig2 = Figure()
    axis2 = fig2.add_subplot(1, 1, 1)
    axis2.set_title("Bubble")
    axis2.set_xlabel("value")
    axis2.set_ylabel("n")
    axis2.bar(range(size),bubbleSortedNums)



    # Convert random plot to PNG image
    pngImage1 = io.BytesIO()
    FigureCanvas(fig1).print_png(pngImage1)

    # Convert bubble plot to PNG image
    pngImage2 = io.BytesIO()
    FigureCanvas(fig2).print_png(pngImage2)



    # Encode PNG image to base64 string
    pngImageB64String1 = "data:image/png;base64,"
    pngImageB64String1 += base64.b64encode(pngImage1.getvalue()).decode('utf8')

    # Encode PNG image to base64 string
    pngImageB64String2 = "data:image/png;base64,"
    pngImageB64String2 += base64.b64encode(pngImage2.getvalue()).decode('utf8')

    return jsonify(rand=pngImageB64String1,bubl=pngImageB64String2)



if __name__=='__main__':
    app.run(debug=True)