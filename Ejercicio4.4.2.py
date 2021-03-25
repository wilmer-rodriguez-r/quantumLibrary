import quantumLibrary


def main():
    unitarias = [[[0, 1 / 2 ** (1 / 2), 1 / 2 ** (1 / 2), 0],
                  [1j / 2 ** (1 / 2), 0, 0, 1 / 2 ** (1 / 2)],
                  [1 / 2 ** (1 / 2), 0, 0, 1j / 2 ** (1 / 2)],
                  [0, 1 / 2 ** (1 / 2), -1 / 2 ** (1 / 2), 0]],
                 [[0, 1 / 2 ** (1 / 2), 1 / 2 ** (1 / 2), 0],
                  [1j / 2 ** (1 / 2), 0, 0, 1 / 2 ** (1 / 2)],
                  [1 / 2 ** (1 / 2), 0, 0, 1j / 2 ** (1 / 2)],
                  [0, 1 / 2 ** (1 / 2), -1 / 2 ** (1 / 2), 0]],
                 [[0, 1 / 2 ** (1 / 2), 1 / 2 ** (1 / 2), 0],
                  [1j / 2 ** (1 / 2), 0, 0, 1 / 2 ** (1 / 2)],
                  [1 / 2 ** (1 / 2), 0, 0, 1j / 2 ** (1 / 2)],
                  [0, 1 / 2 ** (1 / 2), -1 / 2 ** (1 / 2), 0]]]
    n = 3
    ket = [1, 0, 0, 0]
    print('Resultado')
    print(quantumLibrary.quantumDynamics(ket, n, unitarias))
main()