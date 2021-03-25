import numpy as np

def multmatrices(unitaria_1, unitaria_2):
    unitaria_3 = np.dot(unitaria_1, unitaria_2)
    unitaria_4 = np.dot(unitaria_3, np.transpose(np.conj(unitaria_3)))
    if (unitaria_4 == np.identity(len(unitaria_4))).any:
        print('Es unitaria')
        return unitaria_3
    return 'La resultante no es unitaria'

print(multmatrices([[0,1],[1,0]],[[2**(1/2)/2,2**(1/2)/2],[2**(1/2)/2,-2**(1/2)/2]]))