from qiskit import QuantumCircuit
#from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator
from matplotlib.pyplot import draw, show

# The message
MESSAGE = '00'

# Alice encodes the message
qc_alice = QuantumCircuit(2, 2)

if MESSAGE[-1] == '1':
    qc_alice.x(0)
if MESSAGE[-2] == '1':
    qc_alice.x(1)

# Bob measures
qc_bob = QuantumCircuit(2, 2)
qc_bob.measure([0,1],[0,1])

sim = AerSimulator()
job = sim.run(qc_alice.compose(qc_bob))
result = job.result()
print(result.get_counts())
