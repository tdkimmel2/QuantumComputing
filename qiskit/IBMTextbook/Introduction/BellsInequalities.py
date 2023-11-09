import random
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

def setup_variables():
    r = random.random()

    A = r*(2/3)
    B = r*(1/3)

    return A, B

def hash2bit(variable, hash_type):
    if hash_type == 'V':
        bit = (variable < 0.5)
    elif hash_type == 'H':
        bit = (variable < 0.25)

    bit = str(int(bit))

    return bit

shots = 8192
def calculate_P():
    P = {}
    for hashes in ['VV', 'VH', 'HV', 'HH']:
        # Calculate each P[hashes] by sampling over 'shots' samples
        P[hashes] = 0
        for shot in range(shots):
            A, B = setup_variables()

            a = hash2bit(A, hashes[0])
            b = hash2bit(B, hashes[1])

            P[hashes] += (a != b)/shots

    return P


def bell_test(P):
    sum_P = sum(P.values())
    for hashes in P:

        bound = sum_P - P[hashes]

        print("The upper bound for P['"+hashes+"'] is "+str(bound))
        print("The value of P['"+hashes+"'] is "+str(P[hashes]))
        if P[hashes] <= bound:
            print("The upper bound is obeyed :)\n")
        else:
            if P[hashes] - bound < 0.1:
                print("This seems to have gone over the upper bound, "
                      "but only by a little bit :S\nProbably just rounding"
                      " errors or statistical noise.\n")
            else:
                print("This has gone well over the upper bound :O !!!!!\n")

P = calculate_P()
print(P,"\n")
bell_test(P)
