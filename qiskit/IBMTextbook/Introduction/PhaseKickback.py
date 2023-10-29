from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
#from qiskit_aer import AerSimulator
from matplotlib.pyplot import draw, show

qc = QuantumCircuit(2)

# Get both qubits into superposition states
qc.h(0)
qc.h(1)
ket = Statevector(qc)
print(ket.draw('text'))

# CX has to effect on this state
qc.cx(1,0)
ket = Statevector(qc)
print(ket.draw('text'))

# Apply a phase flip to the target qubit to
# flip it from |+> to |->
qc.z(0)
ket = Statevector(qc)
print(ket.draw('text'))

# CX now flips the control qubit to |-> as well
qc.cx(1,0)
ket = Statevector(qc)
print(ket.draw('text'))

qc.draw('mpl')
draw()

show()
