from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import QasmSimulator


def build_circuit():
    circ = QuantumCircuit(6, 6)
    circ.h(0)
    circ.h(1)
    circ.h(2)
    circ.x(5)
    circ.h(5)
    circ.ccx(0, 1, 3)
    circ.ccx(1, 2, 4)
    circ.ccx(3, 4, 5)
    circ.ccx(1, 2, 4)
    circ.ccx(0, 1, 3)
    circ.h(0)
    circ.h(1)
    circ.h(2)
    circ.x(0)
    circ.x(1)
    circ.x(2)
    circ.h(2)
    circ.ccx(0, 1, 2)
    circ.h(2)
    circ.x(0)
    circ.x(1)
    circ.x(2)
    circ.z(2)
    circ.x(2)
    circ.z(2)
    circ.x(2)
    circ.h(0)
    circ.h(1)
    circ.h(2)
    circ.ccx(0, 1, 3)
    circ.ccx(1, 2, 4)
    circ.ccx(3, 4, 5)
    circ.ccx(1, 2, 4)
    circ.ccx(0, 1, 3)
    circ.h(0)
    circ.h(1)
    circ.h(2)
    circ.x(0)
    circ.x(1)
    circ.x(2)
    circ.h(2)
    circ.ccx(0, 1, 2)
    circ.h(2)
    circ.x(0)
    circ.x(1)
    circ.x(2)
    circ.z(2)
    circ.x(2)
    circ.z(2)
    circ.x(2)
    circ.h(0)
    circ.h(1)
    circ.h(2)
    circ.measure([0, 1, 2], [0, 1, 2])

    return circ


def main(nshots=1000):
    circ = build_circuit()
    sim = QasmSimulator()
    
    compiled = transpile(circ, sim)
    job = sim.run(compiled, shots=nshots)
    result = job.result()

    counts = result.get_counts(compiled)

    for k in sorted(counts.keys()):
        print(f'{k}: {counts[k]}')


if __name__ == '__main__':
    main()
