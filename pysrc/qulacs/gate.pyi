from typing import Callable, List

from typing import overload
import numpy
import qulacs_core
import scipy.sparse

@overload
def Adaptive(gate: qulacs_core.QuantumGateBase, condition: Callable[[List[int]],bool]) -> qulacs_core.QuantumGateBase: ...
@overload
def Adaptive(gate: qulacs_core.QuantumGateBase, condition: Callable[[List[int],int],bool], id: int) -> qulacs_core.QuantumGateBase: ...
def AmplitudeDampingNoise(index: int, prob: float) -> qulacs_core.QuantumGate_CPTP: ...
def BitFlipNoise(index: int, prob: float) -> qulacs_core.QuantumGate_Probabilistic: ...
def CNOT(control: int, target: int) -> qulacs_core.ClsOneControlOneTargetGate: ...
def CP(kraus_list: List[qulacs_core.QuantumGateBase], state_normalize: bool, probability_normalize: bool, assign_zero_if_not_matched: bool) -> qulacs_core.QuantumGateBase: ...
def CPTP(kraus_list: List[qulacs_core.QuantumGateBase]) -> qulacs_core.QuantumGateBase: ...
def CZ(control: int, target: int) -> qulacs_core.ClsOneControlOneTargetGate: ...
@overload
def DenseMatrix(index: int, matrix: numpy.ndarray[numpy.complex128[m,n]]) -> qulacs_core.QuantumGateMatrix: ...
@overload
def DenseMatrix(index_list: List[int], matrix: numpy.ndarray[numpy.complex128[m,n]]) -> qulacs_core.QuantumGateMatrix: ...
def DephasingNoise(index: int, prob: float) -> qulacs_core.QuantumGate_Probabilistic: ...
def DepolarizingNoise(index: int, prob: float) -> qulacs_core.QuantumGate_Probabilistic: ...
def DiagonalMatrix(index_list: List[int], diagonal_element: numpy.ndarray[numpy.complex128[m,1]]) -> qulacs_core.QuantumGateBase: ...
def FREDKIN(control: int, target1: int, target2: int) -> qulacs_core.QuantumGateMatrix: ...
def H(index: int) -> qulacs_core.ClsOneQubitGate: ...
def Identity(index: int) -> qulacs_core.ClsOneQubitGate: ...
def IndependentXZNoise(index: int, prob: float) -> qulacs_core.QuantumGate_Probabilistic: ...
def Instrument(kraus_list: List[qulacs_core.QuantumGateBase], register: int) -> qulacs_core.QuantumGateBase: ...
def Measurement(index: int, register: int) -> qulacs_core.QuantumGate_Instrument: ...
def NoisyEvolution(hamiltonian: qulacs_core.Observable, c_ops: List[qulacs_core.GeneralQuantumOperator], time: float, dt: float) -> qulacs_core.ClsNoisyEvolution: ...
def NoisyEvolution_fast(hamiltonian: qulacs_core.Observable, c_ops: List[qulacs_core.GeneralQuantumOperator], time: float) -> qulacs_core.ClsNoisyEvolution_fast: ...
def P0(index: int) -> qulacs_core.ClsOneQubitGate: ...
def P1(index: int) -> qulacs_core.ClsOneQubitGate: ...
def ParametricPauliRotation(index_list: List[int], pauli_ids: List[int], angle: float) -> qulacs_core.QuantumGate_SingleParameter: ...
def ParametricRX(index: int, angle: float) -> qulacs_core.QuantumGate_SingleParameter: ...
def ParametricRY(index: int, angle: float) -> qulacs_core.QuantumGate_SingleParameter: ...
def ParametricRZ(index: int, angle: float) -> qulacs_core.QuantumGate_SingleParameter: ...
def Pauli(index_list: List[int], pauli_ids: List[int]) -> qulacs_core.QuantumGateBase: ...
def PauliRotation(index_list: List[int], pauli_ids: List[int], angle: float) -> qulacs_core.QuantumGateBase: ...
def Probabilistic(prob_list: List[float], gate_list: List[qulacs_core.QuantumGateBase]) -> qulacs_core.QuantumGateBase: ...
def ProbabilisticInstrument(prob_list: List[float], gate_list: List[qulacs_core.QuantumGateBase], register: int) -> qulacs_core.QuantumGateBase: ...
def RX(index: int, angle: float) -> qulacs_core.ClsOneQubitRotationGate: ...
def RY(index: int, angle: float) -> qulacs_core.ClsOneQubitRotationGate: ...
def RZ(index: int, angle: float) -> qulacs_core.ClsOneQubitRotationGate: ...
@overload
def RandomUnitary(index_list: List[int]) -> qulacs_core.QuantumGateMatrix: ...
@overload
def RandomUnitary(index_list: List[int], seed: int) -> qulacs_core.QuantumGateMatrix: ...
def ReversibleBoolean(index_list: List[int], func: Callable[[int,int],int]) -> qulacs_core.ClsReversibleBooleanGate: ...
def RotInvX(index: int, angle: float) -> qulacs_core.ClsOneQubitRotationGate: ...
def RotInvY(index: int, angle: float) -> qulacs_core.ClsOneQubitRotationGate: ...
def RotInvZ(index: int, angle: float) -> qulacs_core.ClsOneQubitRotationGate: ...
def RotX(index: int, angle: float) -> qulacs_core.ClsOneQubitRotationGate: ...
def RotY(index: int, angle: float) -> qulacs_core.ClsOneQubitRotationGate: ...
def RotZ(index: int, angle: float) -> qulacs_core.ClsOneQubitRotationGate: ...
def S(index: int) -> qulacs_core.ClsOneQubitGate: ...
def SWAP(target1: int, target2: int) -> qulacs_core.ClsTwoQubitGate: ...
def Sdag(index: int) -> qulacs_core.ClsOneQubitGate: ...
def SparseMatrix(index_list: List[int], matrix: scipy.sparse.csc_matrix[numpy.complex128]) -> qulacs_core.QuantumGateBase: ...
def StateReflection(state: qulacs_core.QuantumStateBase) -> qulacs_core.ClsStateReflectionGate: ...
def T(index: int) -> qulacs_core.ClsOneQubitGate: ...
def TOFFOLI(control1: int, control2: int, target: int) -> qulacs_core.QuantumGateMatrix: ...
def Tdag(index: int) -> qulacs_core.ClsOneQubitGate: ...
def TwoQubitDepolarizingNoise(index1: int, index2: int, prob: float) -> qulacs_core.QuantumGate_Probabilistic: ...
def U1(index: int, lambda: float) -> qulacs_core.QuantumGateMatrix: ...
def U2(index: int, phi: float, lambda: float) -> qulacs_core.QuantumGateMatrix: ...
def U3(index: int, theta: float, phi: float, lambda: float) -> qulacs_core.QuantumGateMatrix: ...
def X(index: int) -> qulacs_core.ClsOneQubitGate: ...
def Y(index: int) -> qulacs_core.ClsOneQubitGate: ...
def Z(index: int) -> qulacs_core.ClsOneQubitGate: ...
@overload
def add(gate1: qulacs_core.QuantumGateBase, gate2: qulacs_core.QuantumGateBase) -> qulacs_core.QuantumGateMatrix: ...
@overload
def add(gate_list: List[qulacs_core.QuantumGateBase]) -> qulacs_core.QuantumGateMatrix: ...
@overload
def merge(gate1: qulacs_core.QuantumGateBase, gate2: qulacs_core.QuantumGateBase) -> qulacs_core.QuantumGateMatrix: ...
@overload
def merge(gate_list: List[qulacs_core.QuantumGateBase]) -> qulacs_core.QuantumGateMatrix: ...
def sqrtX(index: int) -> qulacs_core.ClsOneQubitGate: ...
def sqrtXdag(index: int) -> qulacs_core.ClsOneQubitGate: ...
def sqrtY(index: int) -> qulacs_core.ClsOneQubitGate: ...
def sqrtYdag(index: int) -> qulacs_core.ClsOneQubitGate: ...
def to_matrix_gate(gate: qulacs_core.QuantumGateBase) -> qulacs_core.QuantumGateMatrix: ...
