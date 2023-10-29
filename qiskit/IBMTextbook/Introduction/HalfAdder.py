from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from matplotlib.pyplot import draw, show
# Create quantum circuit with 3 qubits and 3 classical bits
# (explain why we need to specify classical bits later)
qc = QuantumCircuit(4, 2)
qc.x(0)
qc.x(1)
qc.cx(0, 2) # CNOT controlled by qubit 0 and targeting qubit 2
qc.cx(1, 2) # CNOT controlled by qubit 1 and targeting qubit 2
qc.ccx(0, 1, 3) # CNOT controlled by two inputs

# Measure qubits 0, 1, & 2 to the respective classical bits
qc.measure([2,3], [0,1])
qc.draw('mpl')
print(qc)

sim = AerSimulator() # Make a new simulator object
job = sim.run(qc) # Run the experiment
result = job.result() # Get the results
print(result.get_counts()) # Interpret the results as "counts" dictionary

show()
