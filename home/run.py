import sys
import input_parser
from emitter import Emitter
from receiver import Receiver
from mirror import Mirror
from laser_circuit import LaserCircuit
import board_displayer
'''
Name:   QILONG ZHONG
SID:    540238846
Unikey: qzho0669

run - Runs the entire program. It needs to take in the inputs and process them
into setting up the circuit. The user can specify optional flags to perform
additional steps, such as -RUN-MY-CIRCUIT to run the circuit and -ADD-MY-MIRRORS
to include mirrors in the circuit.

You are free to add more functions, as long as you aren't modifying the
existing scaffold.
'''


def is_run_my_circuit_enabled(args: list[str]) -> bool:
    # only requires implementation once you reach RUN-MY-CIRCUIT
    '''
    Returns whether or not '-RUN-MY-CIRCUIT' is in args.
    
    Parameters
    ----------
    args - the command line arguments of the program
    '''
    # if args == "":
    #     return True
    # return False
    index = 0
    while index < len(args):
        if args[index] == '-RUN-MY-CIRCUIT':
            return True
        else:
            index += 1
    return False


def is_add_my_mirrors_enabled(args: list[str]) -> bool:
    # only requires implementation once you reach ADD-MY-MIRRORS
    '''
    Returns whether or not '-ADD-MY-MIRRORS' is in args.
    
    Parameters
    ----------
    args - the command line arguments of the program
    '''
    index = 0
    while index < len(args):
        if args[index] == '-ADD-MY-MIRRORS':
            return True
        index += 1
    return False


def initialise_circuit() -> LaserCircuit:
    # only requires implementation once you reach GET-MY-INPUTS
    '''
    Gets the inputs for the board size, emitters and receivers and processes
    it to create a LaserCircuit instance and return it. You should be using
    the functions you have implemented in the input_parser module to handle
    validating each input.

    Returns
    -------
    A LaserCircuit instance with a width and height specified by the user's
    inputted size. The circuit should also include each emitter and receiver
    the user has inputted.
    '''
    print("Creating circuit board...")
    circuit = None
    while True:
        user_input = input("> ")
        if not (input_parser.parse_size(user_input) == None):
            width, height = input_parser.parse_size(user_input)
            circuit = LaserCircuit(width, height)
            print(f"{width}x{height} board created.")
            print()
            break
    # Add emitter
    print("Adding emitter(s)...")
    Max_num_emitter = 10
    index = 0
    while index < Max_num_emitter:
        user_input = input("> ")
        if user_input == "END EMITTERS":
            print(f"{len(circuit.get_emitters())} emitter(s) added.\n")
            break
        # judge if it added successfully and check if it sasify the specifc condition
        if input_parser.parse_emitter(user_input) != None :
            N_Emitter = input_parser.parse_emitter(user_input)
            if circuit.add_emitter(N_Emitter):
                index += 1
                continue
            else:
                continue
    if index == 10:
        print(f"10 emitter(s) added.")
        print()

    # receiver
    print("Adding receiver(s)...")
    Max_num_receiver = 10
    index = 0
    while index < Max_num_receiver:
        user_input = input("> ")
        if user_input == "END RECEIVERS":
            print(f"{len(circuit.get_receivers())} receiver(s) added.\n")
            break
        # judge if it added successfully and check if it sasify the specifc condition
        if input_parser.parse_receiver(user_input) != None :
            N_receiver = input_parser.parse_receiver(user_input)
            if circuit.add_receiver(N_receiver):
                index += 1
            else:
                continue
    if index == 10:
        print(f"10 receiver(s) added.")
        print()
        ############finish!
    return circuit


def set_pulse_sequence(circuit: LaserCircuit, file_obj) -> None:
    # only requires implementation once you reach RUN-MY-CIRCUIT
    '''
    Handles setting the pulse sequence of the circuit. 
    The lines for the pulse sequence will come from the a file named
    /home/input/<file_name>.in. 
    You should be using the functions you have implemented in the input_parser module 
    to handle validating lines from the file.

    Parameter
    ---------
    circuit - The circuit to set the pulse sequence for.
    file_obj - A file like object returned by the open()
    '''
    print("Setting pulse sequence...") 
    Ls1 = []
    Count = 1
    while True:
        Line = file_obj.readline()
        if Line == "":
            break
        emitters = circuit.get_emitters()
        index = 0
        info = "-- ("
        while index < len(emitters):
            if not emitters[index].is_pulse_sequence_set():
                info += emitters[index].get_symbol() + ", "
            index += 1
        
        info = info.strip(", ") + ")"
        Line = Line.strip()
        print(info)
        print(f'Line {Count}: {Line}')
    #setting
        Result = input_parser.parse_pulse_sequence(Line)
        if not (Result == None):
            direction = Result[2]
            symbol = Result[0]
            frequency = Result[1]
            if not symbol_have_already_had(emitters, symbol):
                Count += 1
                continue

            if not symbol_have_already_had(emitters, symbol):
                Count += 1
                continue

            found = True
            j = 0
            while j < len(emitters):
                if emitters[j].get_symbol() == symbol:
                    emitters[j].set_pulse_sequence(frequency, direction)
                    found = False
                j += 1
            if found:
                print(f"Error: emitter '{symbol}' does not exist")
            
        Count += 1



def add_mirrors(circuit: LaserCircuit) -> None:
    # only requires implementation once you reach ADD-MY-MIRRORS
    '''
    Handles adding the mirrors into the circuit. You should be using the
    functions you have implemented in the input_parser module to handle
    validating each input. 
    
    Parameters
    ----------
    circuit - the laser circuit to add the mirrors into
    '''
    print('Adding mirror(s)...')
    while True :
        userinput = input("> ")
        if userinput == "END MIRRORS":
            print(f"{len(circuit.get_mirrors())} mirror(s) added.")
            break
        if not (input_parser.parse_mirror(userinput) == None):
            circuit.add_mirror(input_parser.parse_mirror(userinput))
            continue

def symbol_have_already_had(emitters, symbol):
    index = 0
    while index < len(emitters):
        if emitters[index].get_symbol() == symbol:
            if emitters[index].is_pulse_sequence_set():
                print("Error: emitter '{symbol}' already has its pulse sequence set")
                return False
        index += 1
    # print("Error: emitter '{symbol}' does not exist")
    return True

def Check_Sequence_Set_Emitter(emitters, symbol):
     Count = 0
     i = 0
     while i < len(emitters):
        if emitters[i].get_symbol() == symbol:
            return True
        i += 1
     return False


def implement_circuit(circuit):
    try:
        print("<RUN-MY-CIRCUIT FLAG DETECTED!>\n")
        input_file = open("./input/pulse_sequence.in", "r")
        set_pulse_sequence(circuit, input_file)
        print("Pulse sequence set.\n")
        circuit.run_circuit()
        input_file.close()
    except FileNotFoundError:
        print("Error: -RUN-MY-CIRCUIT flag detected but /home/input/pulse_sequence.in does not exist")

def implement_mirror(circuit):
    print("<ADD-MY-MIRRORS FLAG DETECTED!>\n")
    add_mirrors(circuit)
    print()
    circuit.board_displayer.print_board()
    print()

def main(args: list[str]) -> None:
    # only requires implementation once you reach GET-MY-INPUTS
    # will require extensions in RUN-MY-CIRCUIT and ADD-MY-MIRRORS
    '''
    Responsible for running all code related to the program.

    Parameters
    ----------
    args - the command line arguments of the program
    '''


    circuit = initialise_circuit()
    if len(sys.argv) == 1:
        circuit.print_board()
        print()
    elif len(sys.argv) == 2:
        Run_Flag = is_run_my_circuit_enabled(sys.argv)
        add_mirror = is_add_my_mirrors_enabled(sys.argv)

        if Run_Flag:
            circuit.print_board()
            print()
            implement_circuit(circuit)

        if add_mirror:
            implement_mirror(circuit)
    elif len(sys.argv) == 3:
        if is_run_my_circuit_enabled(sys.argv) and is_add_my_mirrors_enabled(sys.argv):
            implement_mirror(circuit)
            implement_circuit(circuit)
            



if __name__ == '__main__':
    '''
    Entry point of program. We pass the command line arguments to our main
    program. We do not recommend modifying this.
    '''

    # l = LaserCircuit(100, 100)
    # l.add_mirror(Mirror('v', 5, 2))
    # l.add_mirror(Mirror('\\', 15, 2))
    # l.add_mirror(Mirror('>', 4, 2))
    # l.add_emitter(Emitter('B', 8, 4))
    # l.add_receiver(Receiver('R1', 9, 3))
    # print(l.get_collided_mirror(Receiver('R0', 15, 2)))

    main(sys.argv)

