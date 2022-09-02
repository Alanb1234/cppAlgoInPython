import numpy as np
import cppSortAlgorithms

randnums = np.random.randint(1,101,100)

bubbleSortedNums = cppSortAlgorithms.bubble_sort(randnums.astype(np.intc))
mergeSortedNums = cppSortAlgorithms.merge_sort(randnums.astype(np.intc))

print("The random number array to be sorted is:")
print(randnums)
print()
print("Bubble sort: ")
print(bubbleSortedNums)
print()
print("Merge sort:")
print(mergeSortedNums)
