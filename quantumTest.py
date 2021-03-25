import unittest
import quantumLibrary as ql

class TestStringMethods(unittest.TestCase):

    def test_quantum_states(self):
        ket = [-3-1j, -2j, 1j, 2]
        pos = 2
        self.assertEqual(ql.quantumStates(ket, pos), 0.05)
        ket = [3-4j, 7+2j]
        pos = 0
        self.assertEqual(ql.quantumStates(ket, pos), 0.32)

    def test_quantum_Transition(self):
        ket = [1, -1j]
        bra = [1j, 1]
        self.assertEqual(ql.quantumTransition(ket, bra), -1j)
        ket = [(2**(1/2))/2, (2**(1/2))*1j/2]
        bra = [(2**(1/2))*1j/2, -(2**(1/2))/2]
        self.assertEqual(ql.quantumTransition(ket, bra), -1j)

    def test_quantum_Observables(self):
        observable = [[1, -1j], [1j, 2]]
        ket = [(2**(1/2))/2, ((2**(1/2))/2)*1j]
        self.assertEqual(ql.quantumObservables(observable, ket), (0.25, 2.5))
        observable = [[0,-1j],[1j,0]]
        ket = [1/2**(1/2),1j/2**(1/2)]
        self.assertEqual(ql.quantumObservables(observable, ket), (0, 1))

    def test_quantum_Measuring(self):
        observable = [[0, 1],[1, 0]]
        ket = [1, 0]
        self.assertEqual(ql.quantumMeasuring(observable, ket), [0.5, 0.5])

    def test_quantum_Dynamics(self):
        unitarias = [[[0,1/2**(1/2),1/2**(1/2),0],
                     [1j/2**(1/2),0,0,1/2**(1/2)],
                     [1/2**(1/2),0,0,1j/2**(1/2)],
                     [0,1/2**(1/2),-1/2**(1/2),0]],
                     [[0, 1 / 2 ** (1 / 2), 1 / 2 ** (1 / 2), 0],
                     [1j / 2 ** (1 / 2), 0, 0, 1 / 2 ** (1 / 2)],
                     [1 / 2 ** (1 / 2), 0, 0, 1j / 2 ** (1 / 2)],
                     [0, 1 / 2 ** (1 / 2), -1 / 2 ** (1 / 2), 0]],
                     [[0, 1 / 2 ** (1 / 2), 1 / 2 ** (1 / 2), 0],
                     [1j / 2 ** (1 / 2), 0, 0, 1 / 2 ** (1 / 2)],
                     [1 / 2 ** (1 / 2), 0, 0, 1j / 2 ** (1 / 2)],
                     [0, 1 / 2 ** (1 / 2), -1 / 2 ** (1 / 2), 0]]]
        n = 3
        ket= [1,0,0,0]
        self.assertTrue((ql.quantumDynamics(ket, n, unitarias) == [0, -0.71+0.71j, 0, 0]).any())

if __name__ == '__main__':
    unittest.main()
