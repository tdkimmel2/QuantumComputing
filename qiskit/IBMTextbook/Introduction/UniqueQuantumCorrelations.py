from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
#from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from matplotlib.pyplot import draw, show

sim = AerSimulator()

qc_charlie = QuantumCircuit(2, 2)
qc_charlie.ry(1.911,1)
qc_charlie.cx(1,0)
qc_charlie.ry(0.785,0)
qc_charlie.cx(1,0)
qc_charlie.ry(2.356,0)
qc_charlie.draw('mpl')
draw()

# Alice and Bob try making z measurements on their qubits
meas_zz = QuantumCircuit(2,2)
meas_zz.measure([0,1],[0,1])

job = sim.run(qc_charlie.compose(meas_zz))
result = job.result()
plot_histogram(result.get_counts())
draw()

# Alice makes a z measurement and Bob makes a x measurement
meas_zx = QuantumCircuit(2,2)
meas_zx.h(0)
meas_zx.measure([0,1],[0,1])

job = sim.run(qc_charlie.compose(meas_zx))
result = job.result()
plot_histogram(result.get_counts())
draw()

# Alice makes a x measurement and Bob makes a z measurement
meas_xz = QuantumCircuit(2,2)
meas_xz.h(1)
meas_xz.measure([0,1],[0,1])

job = sim.run(qc_charlie.compose(meas_xz))
result = job.result()
plot_histogram(result.get_counts())
draw()

# Alice and Bob make x measurements
meas_xx = QuantumCircuit(2,2)
meas_xx.h([0,1])
meas_xx.measure([0,1],[0,1])

job = sim.run(qc_charlie.compose(meas_xx))
result = job.result()
plot_histogram(result.get_counts())
draw()

show()
