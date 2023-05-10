import numpy as np

zeros_array=np.zeros(16,dtype=int)  #create zeros array with 16 element 
zeros_array=zeros_array.reshape(4,4)  #reshape array to be two diman
zeros_array=zeros_array+np.array([1,2,3,4])   #Use broadcasting to create a 4 x 4 array (1 2 3 4)
print(zeros_array)