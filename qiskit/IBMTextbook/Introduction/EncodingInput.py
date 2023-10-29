from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from matplotlib.pyplot import draw, show
# Create quantum circuit with 3 qubits and 3 classical bits
# (explain why we need to specify classical bits later)
qc = QuantumCircuit(3, 3)
qc.x([0,1]) # Perform X-gates on 0 & 1

# Measure qubits 0, 1, & 2 to the respective classical bits
qc.measure([0,1,2], [0,1,2])
qc.draw('mpl')
print(qc)

sim = AerSimulator() # Make a new simulator object
job = sim.run(qc) # Run the experiment
result = job.result() # Get the results
print(result.get_counts()) # Interpret the results as "counts" dictionary

show()
