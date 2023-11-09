from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from matplotlib.pyplot import draw, show
import math

qc = QuantumCircuit(1, 1)
qc.ry(-math.pi/4,0)

qc.measure([0], [0])
qc.draw('mpl')
print(qc)

sim = AerSimulator() # Make a new simulator object
job = sim.run(qc) # Run the experiment
result = job.result() # Get the results
print(result.get_counts()) # Interpret the results as "counts" dictionary

show()
