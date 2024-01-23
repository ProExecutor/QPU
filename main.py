from pyquil import Program, get_qc
from pyquil.gates import H, CNOT

# Create a quantum program
p = Program()

# Apply a Hadamard gate to the 0th qubit
p += H(0)

# Apply a CNOT gate to the 0th and 1st qubits
p += CNOT(0, 1)

# Get a quantum computer simulator with 2 qubits
qc = get_qc('2q-qvm')

# Run the quantum program on the simulator
result = qc.run_and_measure(p, trials=10)

print(result)
