# 1. Create a simple quantum program called a 'quantum circuit'.
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from matplotlib.pyplot import draw, show
from qiskit.visualization import plot_histogram
qc = QuantumCircuit(3)
qc.h(0)
qc.cx(0, [1, 2])
qc.measure_all()

# 2. Ask IBM Quantum for its least busy device that isn't a simulator.
# If you're running this locally, load your IBM Quantum API token using
#     service = QiskitRuntimeService(channel="ibm_quantum", token="ABC")
"""
from qiskit_ibm_runtime import QiskitRuntimeService, Session, Sampler
service = QiskitRuntimeService(channel="ibm_quantum")
backend = service.least_busy(simulator=False, operational=True)
print(f'Running on {backend}')
# 3. Run your circuit on that device
with Session(backend=backend):
    sampler = Sampler()
    result = sampler.run(qc).result()
distribution = result.quasi_dists[0].binary_probabilities()
"""
# When running locally
simulator = AerSimulator()
#compiled_circuit = transpile(qc, simulator)
job = simulator.run(qc)
result = job.result()


# 4. Plot the results
#distribution = result.get_counts(compiled_circuit)
distribution = result.get_counts()

plot_histogram(distribution)
draw()
show()
