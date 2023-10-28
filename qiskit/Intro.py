from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from matplotlib.pyplot import draw, show

# Aer's AerSimulator
simulator = AerSimulator()

# Quantum Circuit
circuit = QuantumCircuit(2, 2)

# Add a H gate on qubit 0
circuit.h(0)

# Add a CX (CNOT) gate on control qubit 0 and target qubit 1
circuit.cx(0, 1)

# Map the quantum measurement to the classical bits
circuit.measure([0, 1], [0, 1])

# Compile the circuit for the support instruction set (basis_gates)
# and topology (coupling_map) of the backend
compiled_circuit = transpile(circuit, simulator)

# Execute the circuit on the aer simulator
job = simulator.run(compiled_circuit, shots=1000)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(compiled_circuit)
print("\nTotal count for 00 and 11 are:", counts)

# Draw the circuit
circuit.draw('mpl', filename = 'IntroCircuit.pdf') # In a notebook this is all you need
draw() # Draw and show in window at the end
print(circuit) # Draw in terminal

# Plot a histogram
plot_histogram(counts, filename = 'IntroCounts.pdf')
draw() # Draw and show in window at the end

plt.show()
