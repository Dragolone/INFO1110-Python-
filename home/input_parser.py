from emitter import Emitter
from receiver import Receiver
from mirror import Mirror

'''
Name:   QILONG ZHONG
SID:    540238846
Unikey: qzho0669

input_parser - A module that parses the inputs of the program. 
We define parsing as checking the validity of what has been entered 
to determine if it's valid. If it's not valid, an appropriate message 
should be printed. Whenever we retrieve input in the program, we 
should be using functions from this module to validate it.

You are free to add more functions, as long as you aren't modifying the
existing scaffold.
'''


def parse_size(user_input: str) -> tuple[int, int] | None:
    # only requires implementation once you reach GET-MY-INPUTS
    '''
    Checks if user_input is a valid input for the size of the circuit board by
    performing the following checks:
      1)  user_input contains exactly 2 tokens. If there are 2 tokens, we
          interpret the first token as width and the second token as height for
          the remaining checks.
      2)  width is an integer.
      3)  height is an integer.
      4)  width is greater than zero.
      5)  height is greater than zero.

    Parameters
    ----------
    user_input - the user input for the circuit's board size

    Returns
    -------
    If all checks pass, returns a tuple containing the width and height of
    the circuit board.
    Else, if at any point a check fails, prints an error message stating the cause
    of the error and returns None, skipping any further checks.

    Example 1:
    >>> size = parse_size('18 0')
    Error: height must be positive
    >>> size
    None

    Example 2:
    >>> size = parse_size('18 6')
    >>> size
    (18, 6)
    '''
    tokens = user_input.strip().split()
    if len(tokens) != 2:
        print("Error: <width> <height>")
        return None
    width_token, height_token = tokens

    try:
        width = int(width_token)
    except ValueError:
        print("Error: width is not an integer")
        return None

    try:
        height = int(height_token)
    except ValueError:
        print("Error: height is not an integer")
        return None

    if width <= 0:
        print("Error: width must be greater than zero")
        return None

    if width > 0:
        if height <= 0:
            print("Error: height must be greater than zero")
            return None

    return (width, height)



# Check whether the symbol is under the target_symbol
def check_Emitter_symbol(user_symbol): 
    target_symbol = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    index = 0
    while index < len(target_symbol):
        if target_symbol[index] == user_symbol:
            return True
        else:
            index += 1
    return False 


def parse_emitter(user_input: str) -> Emitter | None:
    # only requires implementation once you reach GET-MY-INPUTS
    '''
    Checks if user_input is a valid input for creating an emitter by
    performing the following checks in order for any errors: 
      1)  user_input contains exactly 3 tokens. If there are 3 tokens, we 
          interpret the first token  as symbol, the second token as x and the 
          third token as y for the remaining checks.
      2)  symbol is a character between 'A' to 'J'. 
      3)  x is an integer.
      4)  y is an integer.
      5)  x is greater than 0.
      6)  y is greater than 0

    Parameters
    ----------
    user_input - the user input for creating a new emitter

    Returns
    -------
    If all checks pass, returns a new Emitter instance with the specified
    symbol, x and y position set.
    Else, if at any point a check fails, prints an error message stating the cause
    of the error and returns None, skipping any further checks.
    '''
    user_input = user_input.strip().split()
    if not (len(user_input) == 3): 
        print("Error: <symbol> <x> <y>")
        return None
    x = user_input[1]
    y = user_input[2]
    user_symbol = user_input[0]
    if not check_Emitter_symbol(user_symbol):
        print("Error: symbol is not between 'A'-'J'")
        return None
    try:
        x = int(x)
    except ValueError:
        print("Error: x is not an integer")
        return None
    try:
        y = int(y)
    except ValueError:
        print("Error: y is not an integer")
        return None
    
    if int(x) < 0 :
        print("Error: x cannot be negative")
        return None
    if int(x) >= 0:
        if int(y) < 0:
            print("Error: y cannot be negative")
            return None

    return Emitter(user_symbol, x, y)

# Check whether the symbol is under the target_symbol2
def check_Receiver_symbol(user_symbol2):
    target_symbol2 = ["R0", "R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9"]
    index = 0
    while index < len(target_symbol2):
        if user_symbol2 == target_symbol2[index]:
            return True
        index += 1
    return False

def parse_receiver(user_input: str) -> Receiver | None:
    # only requires implementation once you reach GET-MY-INPUTS
    '''
    Identical to parse_emitter, with the only differences being
    that the symbol must be between 'R0' to 'R9', and that a new Receiver
    instance is returned if all checks pass.

    Parameters
    ----------
    user_input - the user input for creating a new receiver

    Returns
    -------
    If all checks pass, returns a new Receiver instance with the specified
    symbol, x and y position set.
    Else, if at any point a check fails, prints an error message stating the cause
    of the error and returns None, skipping any further checks.    
    '''
    user_input = user_input.strip().split()
    if not (len(user_input) == 3): 
        print("Error: <symbol> <x> <y>")
        return None
    x = user_input[1]
    user_symbol2 = user_input[0]
    y = user_input[2]
    if not check_Receiver_symbol(user_symbol2):
        print("Error: symbol is not between R0-R9")
        return None

    try:
        x = int(x)
    except ValueError:
        print("Error: x is not an integer")
        return None
    try:
        y = int(y)
    except ValueError:
        print("Error: y is not an integer")
        return None
    
    if int(x) < 0 :
        print("Error: x cannot be negative")
        return None
    if int(x) >= 0:
        if int(y) < 0:
            print("Error: y cannot be negative")
            return None
    return Receiver(user_symbol2, x, y)


def parse_pulse_sequence(line: str) -> tuple[str, int, str] | None:
    # only requires implementation once you reach RUN-MY-CIRCUIT
    '''
    Checks if line is valid for setting the pulse sequence of an emitter by
    performing the following checks in order for any errors:
      1)  line contains exactly 3 tokens.
          If there are 3 tokens, we interpret the first token as symbol, the
          second token as frequency and the third token as direction for the
          remaining checks.
      2)  symbol is a character between 'A' to 'J'.
      3)  frequency is an integer.
      4)  frequency is greater than zero.
      5)  direction is either 'N', 'E', 'S' or 'W'.

    Parameters
    ----------
    user_input - the user input for setting the pulse sequence of an emitter

    Returns
    -------
    If all checks pass, returns a tuple containing the specified symbol,
    frequency and direction which can be used for setting the pulse sequence
    of the emitter.
    Else, if at any point a check fails, prints an error message stating the cause
    of the error and returns None, skipping any further checks.    
    '''
    user_input = line.strip().split()
    if not (len(user_input) == 3): 
        print("Error: <symbol> <frequency> <direction>")
        return None
    symbol, frequency, direction = user_input
    if not check_Emitter_symbol(symbol):
        print("Error: symbol is not between A-J")
        return None
    try:
        frequency = int(frequency)
    except ValueError:
        print("Error: frequency is not an integer")
        return None
    if frequency <= 0:
        print("Error: frequency must be greater than zero")
        return None
    elif direction == 'N' or direction == 'E' or direction == 'S' or direction == 'W':
        return (symbol, frequency, direction)
    else:
        print("Error: direction must be 'N', 'E', 'S' or 'W'")
        return None

def parse_mirror(user_input: str) -> Mirror | None:
    # only requires implementation once you reach ADD-MY-MIRRORS
    '''
    Checks if user_input is a valid input for creating a mirror by performing
    the following checks in order for any errors:
      1)  user_input contains exactly 3 tokens. If there are 3 tokens, we
          interpret the first token  as symbol, the second token as x and the
          third token as y for the remaining checks.
      2)  symbol is either '/', '\', '>', '<', '^', or 'v'.
      3)  x is an integer.
      4)  y is an integer.
      5)  x is greater than 0.
      6)  y is greater than 0.

    Parameters
    ----------
    user_input - the user input for creating a mirror

    Returns
    -------
    If all checks pass, returns a new Mirror instance with the specified
    symbol, x and y position set.
    Else, if at any point a check fails, prints an error message stating the cause
    of the error and returns None, skipping any further checks.    
    '''
    tokens = user_input.strip().split()
    if len(tokens) != 3:
        print("Error: <symbol> <x> <y>")
        return None
    
    symbol = tokens[0]
    x_str = tokens[1]
    y_str = tokens[2]

    
    if symbol != '/' and symbol != '\\' and symbol != '>' and symbol != '<' and symbol != '^' and symbol != 'v':
        print("Error: symbol must be '/', '\\', '>', '<', '^' or 'v'")
        return None

    try:
        x = int(x_str)
        if x < 0:
            print("Error: x cannot be negative")
            return None
    except ValueError:
        print("Error: x is not an integer")
        return None

    try:
        y = int(y_str)
        if y < 0:
            print("Error: y cannot be negative")
            return None
    except ValueError:
        print("Error: y is not an integer")
        return None

    return Mirror(symbol, x, y)


