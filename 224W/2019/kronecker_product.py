import numpy as np

def nth_kron_product(arr : np.ndarray, n : int) -> np.ndarray:
    if n < 0 :
        return arr 
    intermediate_result = arr
    for i in range( n ):
        intermediate_result = np.kron(intermediate_result, arr)
    return intermediate_result


a = np.array([[1,1],[1,0]])
print(nth_kron_product(a,13).shape)