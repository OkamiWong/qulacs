#define _USE_MATH_DEFINES
#include <cmath>
#include <cppsim/state.hpp>
#include <cppsim/gate_factory.hpp>
#include <cppsim/gate_merge.hpp>
#include <cppsim/gate_matrix.hpp>
#include <cppsim/gate_general.hpp>

int main() {
    ComplexMatrix one_qubit_matrix(2, 2);
    one_qubit_matrix << 0, 1, 1, 0;
    auto one_qubit_gate = gate::DenseMatrix(0, one_qubit_matrix);
    std::cout << one_qubit_gate << std::endl;

    ComplexMatrix two_qubit_matrix(4,4);
    two_qubit_matrix <<
        1, 0, 0, 0,
        0, 1, 0, 0,
        0, 0, 0, 1,
        0, 0, 1, 0;
    auto two_qubit_gate = gate::DenseMatrix({0,1}, two_qubit_matrix);
    std::cout << two_qubit_gate << std::endl;
    return 0;
}