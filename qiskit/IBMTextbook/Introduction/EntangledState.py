from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
#from qiskit_aer import AerSimulator
from matplotlib.pyplot import draw, show

qc = QuantumCircuit(2)

# Get qubit 1 into a superposition state
qc.h(1)
ket = Statevector(qc)
print(ket.draw('text'))

# CNOT on the state, if qubit one is |0> no change
# if qubit 1 is |1>, qubit 0 flips to |1>
qc.cx(1,0)
ket = Statevector(qc)
print(ket.draw('text'))

qc.draw('mpl')
draw()

show()
