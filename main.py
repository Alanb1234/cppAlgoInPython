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

# To time how long it took for the python and c++ algorithms to run
import timeit
from typing import List

app = Flask(__name__)



@app.route("/",methods=["GET","POST"])
def home():

    return render_template("base.html")

@app.route("/output",methods=["GET","POST"])
def output():

    algorithms = request.json['algorithms']
    size = request.json['size']
    size = int(size)

    cpptime = ""
    pythontime = ""

    #put the algorithm here# The random array to be sorted 
    randnums = np.random.randint(1,size+1,size)

    

    # The sorting algortims in c++, * use an if here for selection of the algorithm going to be used
    if algorithms == "bubble":

        #cpp
        start1 = timeit.default_timer()
        SortedNumsCpp = cppSortAlgorithms.bubble_sort(randnums.astype(np.intc))
        end1 = (timeit.default_timer() - start1)*1000 # in milliseconds
        cpptime =  f"{end1:.5f}" 

        #python
        bubblearr = randnums.astype(np.intc).tolist()
        start2 = timeit.default_timer()
        SortedNumsPython = bubbleSort(bubblearr)
        end2 = (timeit.default_timer() - start2)*1000 # in milliseconds
        pythontime =  f"{end2:.5f}" 



    elif algorithms == "merge":
        #cpp
        start = timeit.default_timer()
        SortedNumsCpp = cppSortAlgorithms.merge_sort(randnums.astype(np.intc))
        end = (timeit.default_timer() - start)*1000 # in milliseconds
        cpptime =  f"{end:.5f}"

        #python
        murgearr = randnums.astype(np.intc).tolist()
        start2 = timeit.default_timer()
        SortedNumsPython = mergeSort(murgearr)
        end2 = (timeit.default_timer() - start2)*1000 # in milliseconds
        pythontime =  f"{end2:.5f}" 
        
    elif algorithms == "insertion": 
        #cpp
        start = timeit.default_timer()
        SortedNumsCpp = cppSortAlgorithms.insertion_sort(randnums.astype(np.intc))
        end = (timeit.default_timer() - start)*1000 # in milliseconds
        cpptime =  f"{end:.5f}" 

        #python
        insertarr = randnums.astype(np.intc).tolist()
        start2 = timeit.default_timer()
        SortedNumsPython = insertionSort(insertarr)
        end2 = (timeit.default_timer() - start2)*1000 # in milliseconds
        pythontime =  f"{end2:.5f}" 
        
    cpptime += " ms"
    pythontime += " ms"


    # Generate  random plot
    fig1 = Figure()
    axis1 = fig1.add_subplot(1, 1, 1)
    axis1.set_title("random")
    axis1.set_xlabel("value")
    axis1.set_ylabel("n")
    axis1.bar(range(size),randnums)

    # Generat cpp sorted plot
    fig2 = Figure()
    axis2 = fig2.add_subplot(1, 1, 1)
    axis2.set_title(algorithms+" c++")
    axis2.set_xlabel("value")
    axis2.set_ylabel("n")
    axis2.bar(range(size),SortedNumsCpp)

    # Generat python sorted plot
    fig3 = Figure()
    axis3 = fig3.add_subplot(1, 1, 1)
    axis3.set_title(algorithms+" python")
    axis3.set_xlabel("value")
    axis3.set_ylabel("n")
    axis3.bar(range(size),SortedNumsPython)



    # Convert random plot to PNG image
    pngImage1 = io.BytesIO()
    FigureCanvas(fig1).print_png(pngImage1)

    # Convert cpp sorted plot to PNG image
    pngImage2 = io.BytesIO()
    FigureCanvas(fig2).print_png(pngImage2)

    # Convert python sorted plot to PNG image
    pngImage3 = io.BytesIO()
    FigureCanvas(fig3).print_png(pngImage3)
    

    # Encode PNG image to base64 string
    pngImageB64String1 = "data:image/png;base64,"
    pngImageB64String1 += base64.b64encode(pngImage1.getvalue()).decode('utf8')

    # Encode cpp PNG image to base64 string
    pngImageB64String2 = "data:image/png;base64,"
    pngImageB64String2 += base64.b64encode(pngImage2.getvalue()).decode('utf8')

    # Encode python PNG image to base64 string
    pngImageB64String3 = "data:image/png;base64,"
    pngImageB64String3 += base64.b64encode(pngImage3.getvalue()).decode('utf8')

    return jsonify(rand=pngImageB64String1, cpp=pngImageB64String2, python=pngImageB64String3, cppT=cpptime , pyT=pythontime)

# bubble sort algorithm in pyhton
def bubbleSort(array):
  # loop to access each array element
    for i in range(len(array)):

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:

                # swapping elements if elements
                # are not in the intended order
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

# merge sort alorithm in python
def merge(left, right):
    """Merge sort merging function."""

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def mergeSort(array):
    """Merge sort algorithm implementation."""

    if len(array) <= 1:  # base case
        return array

    # divide array in half and merge sort recursively
    half = len(array) // 2
    left = mergeSort(array[:half])
    right = mergeSort(array[half:])

    return merge(left, right)

# insertion sort algorithm in python
def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

    return arr



if __name__=='__main__':
    app.run(debug=True)
