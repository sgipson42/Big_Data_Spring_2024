import numpy as np

# python is actually slow -- loops are slow-- it makes a copy of i each time
# lists are not arrays--dont have some of the advantages of arrays
# numpy is barely written in python, the real numpy is mostly in c++ because it's way faster

regular_python_list = [1, 2, 6]
# now make it a numpy array
switch_to_array = np.array(regular_python_list) # more efficient this way when lots of operations have to happen or when list is really big
print(switch_to_array)

# make a 2D array
twoD_list = [[1, 2, 6],[3, 5, 7]] # dimensions have to match for this -- each dimension must have same number of elements
twoD_array = np.array(twoD_list)
print(twoD_array)

# nan only works for float -- there isn't an int that represents nothing -- but there is a float representing nothing -- nan
# so if you have to work with data where some might be missing, you want ot make sure you can convert whatever you are doing to floats

data3 = [4, 'a', False]
arr3 = np.array(data3)
# what is the type of this? probably object?
print(arr3)
print(type(arr3)) # numpy array
print(type(arr3[0])) # numpy str
# why did it convert to all one type? because arrays have to be homogeneuos --the only reason arrays are fast is because you know exactly how far to jump,
    # you have to make everything the same size (each element, pointers to strings, to get to the right thing)
    # because random access memory you jump to it
    # why arrays are fast -- also why you need to make all elements the same datatypes

print()
print(switch_to_array.ndim) # 1 dimension
print(twoD_array.ndim) # 2 dimensions -- has axis 0 and axis 1, might havw to tell it which axis to do an operation over
print(arr3.ndim) # 1 dimension

# these all have a shape (dimensions), come back as tuples
print()
print(switch_to_array.shape)
print(twoD_array.shape)
print(arr3.shape)

# length of the shape = number of dimensions
print()
print(len(switch_to_array.shape))
print(len(twoD_array.shape))
print(len(arr3.shape))

# functions to help you make arrays
arr4 = np.zeros((2, 4, 5))
print(arr4) # a 3D object printing like its 2 separate objects
print(arr4.ndim)
print(len(arr4))
print(arr4.shape)

# functions to help you make arrays
arr4 = np.ones((2, 4, 5))
print(arr4) # a 3D object printing like its 2 separate objects
print(arr4.ndim)
print(len(arr4))
print(arr4.shape)

# functions to help you make arrays
arr4 = np.arange(-5, 5, 0.5) # 0.5 is the step interval #5 is max but this doesn't go into the array, stops right before
print(arr4) # a 3D object printing like its 2 separate objects
print(arr4.ndim)
print(len(arr4))
print(arr4.shape)

arr4 = np.linspace(-5, 5, 50)
print(arr4)
print(arr4.shape)

# reshaping
print(arr4.shape) # (50,)
arr5 = arr4.reshape((2,5,5)) #has to multiply out to be the same number of things coming in--won't create new values
print(arr5)
print(arr5.shape)

arr6 = arr5.ravel() # folding back in (opposite of unravel) rah-vel
print(arr6)
print(arr6.shape) # makes it 1D -- slaps it into one array again

arr9 = np.array([[1,2,3],[4,5,6]])
print(arr9)
print(arr9.shape)

# reshape gives you more options than ravel -- you get to specify the dimensions
# but if you don't want to decide every single dimension just do -1 and let the rest of them sort itself out
arr9a = arr9.reshape(-1) # same as ravel in this case
print(arr9a)
print(arr9a.shape)

arr9b = arr9.reshape((3,-1)) # start by doing a 3 by something, and then tack on whatever is left in the rows
print(arr9b)
print(arr9b.shape)

# memory is 1D, when you reshape, all youve done is tell it to remember a new shape, the data has not moved
# reshape takes like no time because data isn't being moved

