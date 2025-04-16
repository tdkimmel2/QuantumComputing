from qiskit import QuantumCircuit, QuantumRegister
from matplotlib.pyplot import show

qubits = QuantumRegister(2, name='q')
circuit = QuantumCircuit(qubits)

q0, q1 = qubits
circuit.h(q0)
circuit.cx(q0, q1)
circuit.measure_all()

circuit.draw("mpl")
show()
