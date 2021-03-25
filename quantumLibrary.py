import numpy as np
from numpy import linalg as LNG


def quantumStates(vector, pos):
    prob = (vector[pos].real**2+vector[pos].imag**2)/(LNG.norm(vector, axis=0))**2
    return round(prob, 2)


def quantumTransition(ket, bra):
    for i in range(len(bra)):
        bra[i] = bra[i].real + bra[i].imag*(-1j)
    inner = np.inner(bra, ket)
    norm_1, norm_2 = LNG.norm(ket, axis=0), LNG.norm(bra, axis=0)
    inner = np.round(inner/(norm_1*norm_2), 2)
    return inner

def quantumObservables(matriz, ket):
    if (matriz == np.conj(np.transpose(matriz))).all():
        matriz_1 = np.conj(np.dot(matriz, ket))
        media = np.inner(matriz_1, ket)
        matriz_media = media * np.identity(len(matriz))
        var_1 = np.dot(matriz - matriz_media, matriz - matriz_media)
        varianza = np.inner(np.conj(ket), np.dot(var_1, ket))
        return np.round(varianza, 2), np.round(media, 2)
    return 'El observable no es hermitiano'


def quantumMeasuring(omega, ket):
    valores, vectores = LNG.eig(omega)
    probs = []
    for item in vectores:
        probs += [np.round(LNG.norm(np.inner(np.conj(ket), item))**2, 2)]
    return probs

def quantumDynamics(ket, n ,matrices_u):
    if n == len(matrices_u):
        for item in matrices_u:
            ket = np.dot(item, ket)
        for i in range(len(ket)):
            ket[i] = np.round(ket[i], 2)
        return ket
    return 'No dígito la cantidad correspondientes de matrices U'
