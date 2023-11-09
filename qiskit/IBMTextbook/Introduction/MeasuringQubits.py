from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from matplotlib.pyplot import draw, show

# An x measurement is to apply an H gate immediately before measurement
meas_x = QuantumCircuit(1,1)
meas_x.h(0)
meas_x.measure(0,0)
meas_x.draw('mpl')
print(meas_x)

qc = QuantumCircuit(1,1)
sim = AerSimulator() # Make a new simulator object
job = sim.run(qc.compose(meas_x)) # Run the experiment
result = job.result() # Get the results
print(result.get_counts()) # Interpret the results as "counts" dictionary

# A z measurement is to simply measure
meas_z = QuantumCircuit(1,1)
meas_z.measure(0,0)
meas_z.draw('mpl')
print(meas_z)

qc = QuantumCircuit(1,1)
job = sim.run(qc.compose(meas_z)) # Run the experiment
result = job.result() # Get the results
print(result.get_counts()) # Interpret the results as "counts" dictionary

# Measurements on |+> and |->
qc = QuantumCircuit(1,1)
qc.h(0) # Now in |+>

# x measurement
qc.h(0)
qc.measure(0,0)
job = sim.run(qc) # Run the experiment
result = job.result()
print('x measurement on |+>: ', result.get_counts())

# z measurement
qc = QuantumCircuit(1,1)
qc.h(0) # Now in |+>
qc.measure(0,0)
job = sim.run(qc) # Run the experiment
result = job.result()
print('z measurement on |+>: ', result.get_counts())

qc = QuantumCircuit(1,1)
qc.x(0)
qc.h(0) # Now in |->

# x measurement
qc.h(0)
qc.measure(0,0)
job = sim.run(qc) # Run the experiment
result = job.result()
print('x measurement on |->: ', result.get_counts())

# z measurement
qc.x(0)
qc.h(0) # Now in |->
qc.measure(0,0)
job = sim.run(qc) # Run the experiment
result = job.result()
print('z measurement on |->: ', result.get_counts())

show()
