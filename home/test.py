from laser_circuit import LaserCircuit
from circuit_for_testing import get_my_lasercircuit
from run import set_pulse_sequence

'''
Name:   QILONG ZHONG
SID:    540238846
Unikey: qzho0669

This test program checks if the set_pulse_sequence function is implemented
correctly.

You can modify this scaffold as needed (changing function names, parameters, 
or implementations...), however, DO NOT ALTER the code in circuit_for_testing 
file, which provides the circuit. The circuit can be retrieved by calling 
get_my_lasercircuit(), and it should be used as an argument for the 
set_pulse_sequence function when testing.

Make sure to create at least six functions for testing: two for positive cases,
two for negative cases, and two for edge cases. Each function should take
different input files.

NOTE: Whenever we use ... in the code, this is a placeholder for you to
replace it with relevant code.
'''


def positive_test_1(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    '''
    Positive test case to verify the set_pulse_sequence function.
    This test is very basic and only checks if the pulse sequence is set
    correctly for each emitter.

    Paramaters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    '''
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, file_obj)
    emitters = my_circuit.get_emitters()

    # Assert Emitter A is set up correctly
    A = emitters[0]
    assert A.is_pulse_sequence_set(), "Emitter A's pulse sequence is not set"
    assert A.get_frequency() == 100, "Emitter A's frequency is not set correctly"
    assert A.get_direction() == "S", "Emitter A's direction is not set correctly"

    # Assert Emitter B is set up correctly
    B = emitters[1]
    assert B.is_pulse_sequence_set(), "Emitter B's pulse sequence is not set"
    assert B.get_frequency() == 256, "Emitter B's frequency is not set correctly"
    assert B.get_direction() == "E", "Emitter B's direction is not set correctly"

    # Assert Emitter C is set up correctly
    C = emitters[2]
    assert C.is_pulse_sequence_set(), "Emitter C's pulse sequence is not set"
    assert C.get_frequency() == 200, "Emitter C's frequency is not set correctly"
    assert C.get_direction() == "W", "Emitter C's direction is not set correctly"

    file_obj.close()


def positive_test_2(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    '''
    Positive test case to verify the set_pulse_sequence function.
    This positive test case contains some strange input format, but the
    function should still be able to set the pulse sequence correctly.

    Paramaters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    '''
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, file_obj)
    emitters = my_circuit.get_emitters()

    # Assert Emitter A is set up correctly
    A = emitters[0]
    assert A.is_pulse_sequence_set(), "Emitter A's pulse sequence is not set"
    assert A.get_frequency() == 100, "Emitter A's frequency is not set correctly"
    assert A.get_direction() == "S", "Emitter A's direction is not set correctly"

    # Assert Emitter B is set up correctly
    B = emitters[1]
    assert B.is_pulse_sequence_set(), "Emitter B's pulse sequence is not set"
    assert B.get_frequency() == 256, "Emitter B's frequency is not set correctly"
    assert B.get_direction() == "E", "Emitter B's direction is not set correctly"

    # Assert Emitter C is set up correctly
    C = emitters[2]
    assert C.is_pulse_sequence_set(), "Emitter C's pulse sequence is not set"
    assert C.get_frequency() == 200, "Emitter C's frequency is not set correctly"
    assert C.get_direction() == "W", "Emitter C's direction is not set correctly"

    file_obj.close()


def negative_test_1(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    '''
    Negative test case to verify the set_pulse_sequence function.
    This test focuses on the output of the parser, it should identify the
    error in the input file and print the error message to the console.

    Paramaters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    '''
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, file_obj)
    emitters = my_circuit.get_emitters()

    # Assert Emitter A is set up correctly
    A = emitters[0]
    assert A.is_pulse_sequence_set(), "Emitter A's pulse sequence is not set"
    assert A.get_frequency() == 100, "Emitter A's frequency is not set correctly"
    assert A.get_direction() == "S", "Emitter A's direction is not set correctly"

    # Assert Emitter B is set up correctly
    B = emitters[1]
    assert B.is_pulse_sequence_set(), "Emitter B's pulse sequence is not set"
    assert B.get_frequency() == 200, "Emitter B's frequency is not set correctly"
    assert B.get_direction() == "S", "Emitter B's direction is not set correctly"

    # Assert Emitter C is set up correctly
    C = emitters[2]
    assert C.is_pulse_sequence_set(), "Emitter C's pulse sequence is not set"
    assert C.get_frequency() == 300, "Emitter C's frequency is not set correctly"
    assert C.get_direction() == "N", "Emitter C's direction is not set correctly"

    file_obj.close()


def negative_test_2(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    '''
    Negative test case to verify the set_pulse_sequence function.
    This test focuses on strange and errorneous input file format, or it is
    valid at parsing stage but invalid at setting the pulse sequence. The
    function should identify the error in the input file and print the error
    message to the console.

    Paramaters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    '''
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, file_obj)
    emitters = my_circuit.get_emitters()

    # Assert Emitter A is set up correctly
    A = emitters[0]
    assert A.is_pulse_sequence_set(), "Emitter A's pulse sequence is not set"
    assert A.get_frequency() == 100, "Emitter A's frequency is not set correctly"
    assert A.get_direction() == "S", "Emitter A's direction is not set correctly"

    # Assert Emitter B is set up correctly
    B = emitters[1]
    assert B.is_pulse_sequence_set(), "Emitter B's pulse sequence is not set"
    assert B.get_frequency() == 400, "Emitter B's frequency is not set correctly"
    assert B.get_direction() == "N", "Emitter B's direction is not set correctly"

    # Assert Emitter C is set up correctly
    C = emitters[2]
    assert not C.is_pulse_sequence_set(), "Emitter C's pulse sequence is not set"
    assert C.get_frequency() == 0, "Emitter C's frequency is not set correctly"
    assert C.get_direction() == None, "Emitter C's direction is not set correctly"

    file_obj.close()


def edge_test_1(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    '''
    Edge test case to verify the set_pulse_sequence function.
    The input file is empty, the function should do nothing and return

    Paramaters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    '''
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, file_obj)
    emitters = my_circuit.get_emitters()

    # Assert Emitter A is set up correctly
    A = emitters[0]
    assert not A.is_pulse_sequence_set(), "Emitter A's pulse sequence is not set"
    assert A.get_frequency() == 0, "Emitter A's frequency is not set correctly"
    assert A.get_direction() == None, "Emitter A's direction is not set correctly"

    # Assert Emitter B is set up correctly
    B = emitters[1]
    assert not B.is_pulse_sequence_set(), "Emitter B's pulse sequence is not set"
    assert B.get_frequency() == 0, "Emitter B's frequency is not set correctly"
    assert B.get_direction() == None, "Emitter B's direction is not set correctly"

    # Assert Emitter C is set up correctly
    C = emitters[2]
    assert not C.is_pulse_sequence_set(), "Emitter C's pulse sequence is not set"
    assert C.get_frequency() == 0, "Emitter C's frequency is not set correctly"
    assert C.get_direction() == None, "Emitter C's direction is not set correctly"

    file_obj.close()


def edge_test_2(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    '''
    Edge test case to verify the set_pulse_sequence function.
    The input file contains very large numbers and very strange input format,
    such as a large number of spaces, tabs, and newlines. The function should
    still be able to set the pulse sequence correctly.

    Paramaters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    '''
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, file_obj)
    emitters = my_circuit.get_emitters()

    # Assert Emitter A is set up correctly
    A = emitters[0]
    assert A.is_pulse_sequence_set(), "Emitter A's pulse sequence is not set"
    assert A.get_frequency() == 10**56, "Emitter A's frequency is not set correctly"
    assert A.get_direction() == "N", "Emitter A's direction is not set correctly"

    # Assert Emitter B is set up correctly
    B = emitters[1]
    assert B.is_pulse_sequence_set(), "Emitter B's pulse sequence is not set"
    assert B.get_frequency() == 123, "Emitter B's frequency is not set correctly"
    assert B.get_direction() == "S", "Emitter B's direction is not set correctly"

    # Assert Emitter C is set up correctly
    C = emitters[2]
    assert not C.is_pulse_sequence_set(), "Emitter C's pulse sequence is not set"
    assert C.get_frequency() == 0, "Emitter C's frequency is not set correctly"
    assert C.get_direction() == None, "Emitter C's direction is not set correctly"

    file_obj.close()


if __name__ == '__main__':
    # Run each function for testing
    positive_test_1(get_my_lasercircuit(), '/home/input/pulse_sequence.in')
    positive_test_2(get_my_lasercircuit(), '/home/input/pulse_sequence_2.in')
    negative_test_1(get_my_lasercircuit(), '/home/input/pulse_sequence_3.in')
    negative_test_2(get_my_lasercircuit(), '/home/input/pulse_sequence_4.in')
    edge_test_1(get_my_lasercircuit(), '/home/input/pulse_sequence_5.in')
    edge_test_2(get_my_lasercircuit(), '/home/input/pulse_sequence_6.in')


