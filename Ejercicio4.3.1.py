from numpy import linalg as LNG


def main():
    vectores = LNG.eig([[0, 1], [1, 0]])[1]
    for item in vectores:
        print('Vector propio--->', item)
main()