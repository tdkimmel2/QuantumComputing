from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
#from qiskit_aer import AerSimulator
from matplotlib.pyplot import draw, show

qc = QuantumCircuit(2)

# This calculates what the state vector of our qubits would be
# after passing through the circuit 'qc'
"""
ket = Statevector(qc)
print(ket.draw('text'))

qc.cx(0,1)
ket = Statevector(qc)
print(ket.draw('text'))

qc.cx(1,0)
ket = Statevector(qc)
print(ket.draw('text'))
"""

qc.x(1)
qc.cx(1,0)
ket = Statevector(qc)
print(ket.draw('text'))

qc.draw('mpl')
draw()

show()
