from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from matplotlib.pyplot import draw, show
# Create quantum circuit with 3 qubits and 3 classical bits
# (explain why we need to specify classical bits later)
qc = QuantumCircuit(1, 1)
#qc.x(0)
#qc.y(0)
qc.h(0)
qc.x(0)
qc.h(0)

# Measure qubits 0, 1, & 2 to the respective classical bits
qc.measure([0], [0])
qc.draw('mpl')
print(qc)

sim = AerSimulator() # Make a new simulator object
job = sim.run(qc, shots=1000) # Run the experiment
result = job.result() # Get the results
print(result.get_counts()) # Interpret the results as "counts" dictionary

show()
