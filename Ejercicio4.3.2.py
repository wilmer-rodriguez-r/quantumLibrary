import quantumLibrary

def main():
    observable = [[0,1],[1,0]]
    ket = [1,0]
    probs = quantumLibrary.quantumMeasuring(observable, ket)
    num = 1
    for item in probs:
        print(f'probabilidad {num}-->', item)
        num += 1

main()