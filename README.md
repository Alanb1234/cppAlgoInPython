# The power of interoperation between C++ and Pyhton

The aim of this poject is to show how powerful interoperation between C++ and Pyhton can be.

Pyhton is a powerfujl language but comes at the cost of being slow. This project shows how libraries that allow for interpoeration between Python and C++ (boost.pyhton in this case) can be used to create very fast executing python programmes.

In order to show this, C++ algorithms have been wrapped using boost.python libraries then compiled to create a .so file that can be imported by python. The runtimes of the wrapped algorithms are compared with algoritims writen in python alone. The results usually show that the algorithms that utilize interoperability between C++ and python  are usually faster by an order of magnitude.

To illisturate the result a website has been created using flask, javascript, html and css. The random generated numpy array and the final sorted array's will be visualised using a matplot bar chart that is coverted to an image that is renderd on the webpage when ever the submit button is pressed.

