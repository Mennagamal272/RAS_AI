import numpy as np
array=np.arange(2,33,2)
array=array.reshape(4,4)
print("4x4 even array")
print(array)
print()
stander_deve=array.std()
mean =array.mean()

mask=abs(array - mean) < 0.5 * stander_deve
array1=array[mask]
print(array1)