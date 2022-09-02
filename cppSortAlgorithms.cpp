// cppSortAlgorithms.cpp : 
#include <boost/python.hpp>
#include <boost/python/numpy.hpp>
#include <boost/scoped_array.hpp>
#include <iostream>
#include <bits/stdc++.h> 

using namespace std;
namespace p = boost::python;
namespace np = boost::python::numpy;



using namespace std;

// ***** Bubble sort algorithm *****
void bubble_sort(int* bubbleNumbers, int size) {

    for (int i = 0; i < size-1; i++) {

        for (int j = i + 1; j < size; j++) {

            int temp;
            if (bubbleNumbers[i] > bubbleNumbers[j]) {
                //Swaping the values
                temp = bubbleNumbers[i];
                bubbleNumbers[i] = bubbleNumbers[j];
                bubbleNumbers[j] = temp;
            }
        }
    }


}  




// ***** Merge sort algorithm *****
void merge(int* mergeNumbers, int p, int q, int r){

    int n1, n2, i, j, k;
    // size of left array = n1
    // size of right array = n2

    n1 = q - p + 1;
    n2 = r -q;

    // Dynamic arrays, but need to deallocate after use
    int* L = new int[n1];
    int* R = new int[n2];

    // Initilizing the value of the left part to L
    for (i = 0; i < n1; i++){
        L[i] = mergeNumbers[p+i];
    }

    // Initilizing the value of the right part to R
    for (j = 0; j < n2; j++){
        R[j] = mergeNumbers[q+j+1];
    }

    i=0, j=0;
    // Compareing and merging them
    // Into new array in sorted order
    for (k=p; i<n1 && j<n2; k++){
        
        if (L[i]<R[j]){
            mergeNumbers[k] = L[i++];
        }
        else{
            mergeNumbers[k] = R[j++];
        }
    }

    // If left array L[] has more elements then Right array R[]
    // hten it ill put all the remaining elements of L[] into A[]
    while (i < n1){
        mergeNumbers[k++] = L[i++];
    }

    // If right array R[] has more elements then Left array L[]
    // hten it ill put all the remaining elements of R[] into A[]
    while(j<n2){
        mergeNumbers[k++] = R[j++];
    }


    // Deallocate the dynamic arrays after use
    delete[]L;
    L = NULL;
    delete[]R;
    R = NULL;

}
// This is the divide and conqure part
void merge_sort(int* mergeNumbers, int p, int r){

    int q;
    if (p<r){
        // middle number
        q= (p+r)/2;
        merge_sort(mergeNumbers, p, q);
        merge_sort(mergeNumbers, q+1, r);
        merge(mergeNumbers, p, q, r);
    }
}

np::ndarray wrap_bubble_sort(np::ndarray const & bubbleNumbers) {
    
    // Make sure we get integers
    if (bubbleNumbers.get_dtype() != np::dtype::get_builtin<int>()) {
        PyErr_SetString(PyExc_TypeError, "Incorrect array data type");
        p::throw_error_already_set();
    }



    // Could also pass back a vector, but unsure if you use C++ or C
    bubble_sort(reinterpret_cast<int*>(bubbleNumbers.get_data()), bubbleNumbers.shape(0));


    return bubbleNumbers;

}


np::ndarray wrap_merge_sort(np::ndarray const & mergeNumbers) {
    
    // Make sure we get integers
    if (mergeNumbers.get_dtype() != np::dtype::get_builtin<int>()) {
        PyErr_SetString(PyExc_TypeError, "Incorrect array data type");
        p::throw_error_already_set();
    }

    // Could also pass back a vector, but unsure if you use C++ or C
    merge_sort(reinterpret_cast<int*>(mergeNumbers.get_data()),0, mergeNumbers.shape(0)-1);


    return mergeNumbers;

}



// Deciding what to expose in the library python can import
BOOST_PYTHON_MODULE(cppSortAlgorithms) {  // Thing in brackets should match output library name
    Py_Initialize();
    np::initialize();
    p::def("bubble_sort", wrap_bubble_sort);
    
    p::def("merge_sort", wrap_merge_sort);
}




