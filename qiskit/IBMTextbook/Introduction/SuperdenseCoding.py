from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
#from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator
from matplotlib.pyplot import draw, show

# The message
MESSAGE = '00'



#########################################
#########NO ENTANGLEMENT VERSION#########
#########################################

qc_alice = QuantumCircuit(2, 2)
# Alice encodes the message
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

#########################################
########WITH ENTANGLEMENT VERSION########
#########################################

qc_alice_entangle = QuantumCircuit(2, 2)
# Alice creates entangled states
qc_alice_entangle.h(1)
qc_alice_entangle.cx(1,0)
ket = Statevector(qc_alice_entangle)
print(ket.draw('text'))
# Alice encodes the message
# Alice only needs to apply a gate to a single qubit
# to encode this message
if MESSAGE[-2] == '1':
    qc_alice_entangle.z(1)
if MESSAGE[-1] == '1':
    qc_alice_entangle.x(1)


qc_bob_entangle = QuantumCircuit(2,2)
# Bob disentangles them
qc_bob_entangle.cx(1,0)
qc_bob_entangle.h(1)
# Then measures
qc_bob_entangle.measure([0,1],[0,1])
qc_bob_entangle.draw('mpl')
draw()

job = sim.run(qc_alice_entangle.compose(qc_bob_entangle))
result = job.result()
print(result.get_counts())

# Now imagine a thrid party creates the entangled state
# and sends qubit 1 to Alice and qubit 0 to Bob
qc_charlie = QuantumCircuit(2, 2)
qc_charlie.h(1)
qc_charlie.cx(1,0)
qc_charlie.draw('mpl')
draw()

# New message
MESSAGE = '01'
qc_alice_complete = QuantumCircuit(2,2)
# Alice encodes the message on qubit 1 and sends it to Bob
# She only has to send one qubit to send two-bits worth of information
if MESSAGE[-2] == '1':
    qc_alice_complete.z(1)
if MESSAGE[-1] == '1':
    qc_alice_complete.x(1)

# Bob then disentangles the state and measures
qc_bob_complete = QuantumCircuit(2,2)
qc_bob_complete.cx(1,0)
qc_bob_complete.h(1)
qc_bob_complete.measure([0,1],[0,1])
complete_qc = qc_charlie.compose(qc_alice_complete.compose(qc_bob_complete))
complete_qc.draw('mpl')
job = sim.run(complete_qc)
result = job.result()
print(result.get_counts())

show()
