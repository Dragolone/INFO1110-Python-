import sorter
from emitter import Emitter
from receiver import Receiver
from photon import Photon
from mirror import Mirror
from board_displayer import BoardDisplayer

'''
Name:   QILONG ZHONG
SID:    540238846
Unikey: qzho0669

LaserCircuit - Responsible for storing all the components of the circuit and
handling the computation of running the circuit. It's responsible for delegating 
tasks to the specific components e.g. making each emitter emit a photon, getting 
each photon to move and interact with components, etc. In general, this class is
responsible for handling any task related to the circuit.

You are free to add more attributes and methods, as long as you aren't 
modifying the existing scaffold.
'''

def valid_symbol(entity, entity_list):
    index = 0
    symbol = entity.get_symbol()
    while index < len(entity_list):
        if entity_list[index].get_symbol() == symbol:
            return False
        index += 1
    return True


def in_the_board(width, height, x, y):
    if x < 0 or y < 0:
        return False
    if y > (height - 1) or x > (width - 1):
        return False
    else:
        return True

def Active_Receiver_num(receivers):
    Index = 0
    j = 0
    while j < len(receivers):
        if receivers[j].is_activated():
            Index += 1
            j += 1
            continue
        if not receivers[j].is_activated():
            j += 1
            Index += 0 
    return Index


class LaserCircuit:


    def __init__(self, width: int, height: int):
        '''        
        Initialise a LaserCircuit instance given a width and height. All 
        lists of components and photons are empty by default.
        board_displayer is initialised to a BoardDisplayer instance. clock is
        0 by default.

        emitters:        list[Emitter]  - all emitters in this circuit
        receivers:       list[Receiver] - all receivers in this circuit
        photons:         list[Photon]   - all photons in this circuit
        mirrors:         list[Mirror]   - all mirrors in this circuit
        width:           int            - the width of this circuit board
        height:          int            - the height of this circuit board
        board_displayer: BoardDisplayer - helper class for storing and 
                                          displaying the circuit board
        clock:           int            - a clock keeping track of how many 
                                          nanoseconds this circuit has run for

        Parameters
        ----------
        width  - the width to set this circuit board to
        height - the width to set this circuit board to
        '''
        self.mirrors = []
        self.receivers = []
        self.photons = []
        self.emitters = []
        self.width = width
        self.height = height
        self.clock = 0
        self.board_displayer = BoardDisplayer(width, height)


    def emit_photons(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Gets each emitter in this circuit's list of emitters to emit a photon.
        The photons emitted should be added to this circuit's photons list.
        '''
        index = 0
        while index < len(self.emitters):
            photon = self.emitters[index].emit_photon()
            self.add_photon(self.emitters[index].emit_photon())
            index += 1 


    def is_finished(self) -> bool:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Returns whether or not this circuit has finished running. The
        circuit is finished running if every photon in the circuit has been
        absorbed.

        Returns
        -------
        True if the circuit has finished running or not, else False.
        '''
        index = 0
        while index < len(self.photons):
            if not self.photons[index].is_absorbed():
                return False
            else:
                index += 1
        return True



    def print_emit_photons(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Prints the output for each emitter emitting a photon.
        
        It will also need to write the output into a
        /home/output/emit_photons.out output file. 
        
        You can assume the /home/output/ path exists.
        '''
        Out_file_name = "./output/emit_photons.out"
        Out_file = open(Out_file_name, 'w')
        index = 0
        print("0ns: Emitting photons.")
        while index < len(self.emitters):
            print(self.emitters[index])
            print(self.emitters[index], file=Out_file)
            index += 1
        
        Out_file.close()


    # def print_activation_times(self) -> None:
    #     # only requires implementation once you reach RUN-MY-CIRCUIT
    #     '''
    #     Prints the output for the activation times for each receiver, sorted
    #     by activation time in ascending order. Any receivers that have not
    #     been activated should not be included.
        
    #     It will also need to write the output into a
    #     /home/output/activation_times.out output file.

    #     You can assume the /home/output/ path exists.
    #     '''
    #     sorted_by_time = sorter.sort_receivers_by_activation_time(self.receivers)

    #     Out_file_name = "/home/output/activation_times.out"
    #     Out_file = open(Out_file_name, 'w')
    #     i = 0
    #     print("Activation times:")
    #     while i < len(sorted_by_time):
    #         Current_receiver = sorted_by_time[i]
    #         if Current_receiver.is_activated():
    #             Info = f"R{Current_receiver.get_symbol()}: {Current_receiver.get_activation_time()}ns"
    #             print(Info)
    #             print(Info, file=Out_file)

    #         i += 1
    #     Out_file.close()
    def print_activation_times(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Prints the output for the activation times for each receiver, sorted
        by activation time in ascending order. Any receivers that have not
        been activated should not be included.
        
        It will also need to write the output into a
        /home/output/activation_times.out output file.

        You can assume the /home/output/ path exists.
        '''
        sorted_by_time = sorter.sort_receivers_by_activation_time(self.receivers)

        Out_file_name = "./output/activation_times.out"
        with open(Out_file_name, 'w') as Out_file:
            print("Activation times:")
            index = 0
            while index < len(sorted_by_time):
                current_receiver = sorted_by_time[index]
                if current_receiver.is_activated():
                    Info = f"R{current_receiver.get_symbol()}: {current_receiver.get_activation_time()}ns"
                    print(Info.strip())  
                    Out_file.write(Info + '\n')
                index += 1


    def print_total_energy(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Prints the output for the total energy absorbed for each receiver,
        sorted by total energy absorbed in descending order. Any receivers
        that have not been activated should not be included.
        
        It will also need to write the output into a
        /home/output/total_energy_absorbed.out output file.

        You can assume the /home/output/ path exists.
        '''
        Sorted_receivers_by_Total_energy = sorter.sort_receivers_by_total_energy(self.receivers)
        Out_file_name = "./output/total_energy.out"
        Out_file = open(Out_file_name, 'w')
        i = 0
        print("Total energy absorbed:")
        while i < len(Sorted_receivers_by_Total_energy):
            Current_total_energy = Sorted_receivers_by_Total_energy[i]
            if Current_total_energy.is_activated():
                
                print(Current_total_energy)
                print(Current_total_energy, file=Out_file)

            i += 1
        Out_file.close()

    
    def print_board(self) -> None:
        '''Calls the print_board method in board_displayer.'''
        self.board_displayer.print_board() #print(LaserCircuit(width, height).print_board())


    def get_collided_emitter(self, entity: Emitter | Receiver | Photon | Mirror | None) -> Emitter | None:
        '''
        Takes in one argument entity which is either a component or a photon
        and checks if it has the same position as another emitter in the 
        circuit. 

        If it does, return the emitter already in the entity's position.
        Else, return None, indicating there is no emitter occupying entity's
        position.
        
        Parameter
        ---------
        entity - an emitter, receiver, photon or mirror

        Returns
        -------
        An emitter if it has the same position as entity, else None.
        '''
        #remove the line below once you start implementing this function
        #raise NotImplementedError
        i = 0
        while i < len(self.emitters):
            current_emitter = self.emitters[i]
            x0 = current_emitter.get_x()
            y0 = current_emitter.get_y()
            x1 = entity.get_x()
            y1 = entity.get_y()
            if x0 == x1 and y0 == y1 :
                return current_emitter
            i += 1
        return None



    def get_collided_receiver(self, entity: Emitter | Receiver | Photon | Mirror | None) -> Receiver | None:
        '''
        Takes in one argument entity which is either a component or a photon
        and checks if it has the same position as another receiver in the 
        circuit. 

        If it does, return the emitter already in the entity's position.
        Else, return None, indicating there is no receiver occupying entity's
        position.
        
        Parameter
        ---------
        entity - an emitter, receiver, photon or mirror

        Returns
        -------
        A receiver if it has the same position as entity, else None.
        '''
        #remove the line below once you start implementing this function
        #raise NotImplementedError
        i = 0
        while i < len(self.receivers):
            current_receiver = self.receivers[i]
            x0 = current_receiver.get_x()
            y0 = current_receiver.get_y()
            x1 = entity.get_x()
            y1 = entity.get_y()
            if x0 == x1 and y0 == y1 :
                return current_receiver
            i += 1
        return None


    def get_collided_mirror(self, entity: Emitter | Receiver | Photon | Mirror | None) -> Mirror | None:
        '''
        Takes in one argument entity which is either a component or a photon
        and checks if it has the same position as another mirror in the 
        circuit. 

        If it does, return the mirror already in the entity's position.
        Else, return None, indicating there is no mirror occupying entity's
        position.
        
        Parameter
        ---------
        entity - an emitter, receiver, photon or mirror

        Returns
        -------
        A mirror if it has the same position as entity, else None.
        '''
        #remove the line below once you start implementing this function
        i = 0
        while i < len(self.mirrors):
            if self.mirrors[i].get_x() == entity.get_x() and self.mirrors[i].get_y() == entity.get_y():
                return self.mirrors[i]
            i += 1
        return None

    def get_collided_component(self, photon: Photon) -> Emitter | Receiver | Mirror | None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        # will require extensions in ADD-MY-MIRRORS
        '''
        Given a photon, returns the component it has collided with (if any).
        A collision occurs if the positions of photon and the component are
        the same.

        Parameters
        ----------
        photon - a photon to check for collision with the circuit's components

        Returns
        -------
        If the photon collided with a component, return that component.
        Else, return None.

        Hint
        ----
        Use the three collision methods above to handle this.
        '''
        if self.get_collided_emitter(photon):
            return self.get_collided_emitter(photon)
        elif self.get_collided_receiver(photon):
            return self.get_collided_receiver(photon)
        elif self.get_collided_mirror(photon):
            return self.get_collided_mirror(photon)
        
             


    # def tick(self) -> None:
    #     # only requires implementation once you reach RUN-MY-CIRCUIT
    #     '''
    #     Runs a single nanosecond (tick) of this circuit. If the circuit has
    #     already finished, this method should return out early.
        
    #     Otherwise, for each photon that has not been absorbed, this method is
    #     responsible for moving it, updating the board to show its new position
    #     and checking if it collided with a component (and handling it if did
    #     occur). At the end, we then increment clock.
    #     '''
    #     index = 0
    #     self.clock += 1
    #     while index < len(self.photons):
    #         self.photons[index].move(self.width, self.height)
    #         A = self.photons[index]
    #         self.board_displayer.add_photon_to_board(A)
    #         Component = self.get_collided_component(A)
    #         if not (Component == None):
    #             self.photons[index].interact_with_component(Component, self.clock)
    #         index += 1

    def tick(self) -> None:
        '''
        Runs a single nanosecond (tick) of this circuit. If the circuit has
        already finished, this method should return out early.

        Otherwise, for each photon that has not been absorbed, this method is
        responsible for moving it, updating the board to show its new position
        and checking if it collided with a component (and handling it if did
        occur). At the end, we then increment clock.
        '''
        if self.is_finished():  # Check if the circuit is already finished
            return

        self.clock += 1 
        index = 0
        while index < len(self.photons):
            photon = self.photons[index]  
            if not photon.is_absorbed():  
                photon.move(self.width, self.height)  
                self.board_displayer.add_photon_to_board(photon)  
                component = self.get_collided_component(photon)  
                if component:
                    photon.interact_with_component(component, self.clock)  
            index += 1


    def run_circuit(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Runs the entire circuit from start to finish. This involves getting
        each emitter to emit a photon, and continuously running tick until the
        circuit is finished running. All output in regards of running the 
        circuit should be contained in this method.
        '''
        print(f'''========================
   RUNNING CIRCUIT...
========================''')
        # self.print_emit_photons()
        print()
        self.emit_photons()
        self.print_emit_photons()
        print()
        while True:
            self.tick()
            if self.is_finished():
                break
            if self.clock % 5 == 0:
                print(f'{self.clock}ns: {Active_Receiver_num(self.receivers)}/{len(self.receivers)} receiver(s) activated.')
                self.board_displayer.print_board()
                print()

        print(f'{self.clock}ns: {Active_Receiver_num(self.receivers)}/{len(self.receivers)} receiver(s) activated.')
        self.board_displayer.print_board()
        print()

        self.print_activation_times()
        print()
        self.print_total_energy()
        print()
        print(f'''========================
   CIRCUIT FINISHED!
========================''')


    
    def add_emitter(self, emitter: Emitter) -> bool:
        '''
        If emitter is not an Emitter instance, return False. Else, you need to
        perform the following checks in order for any errors:
          1)  The emitter's position is within the bounds of the circuit.
          2)  The emitter's position is not already taken by another emitter in
              the circuit.
          3)  The emitter's symbol is not already taken by another emitter in 
              the circuit.
          
        If at any point a check is not passed, an error message is printed
        stating the causeof the error and returns False, skipping any further
        checks. If all checks pass, then the following needs to occur:
          1)  emitter is added in the circuit's list of emitters. emitter
              needs to be added such that the list of emitters remains sorted
              in alphabetical order by the emitter's symbol. You can assume the
              list of emitters is already sorted before you add the emitter.
          2)  emitter's symbol is added into board_displayer.
          3)  The method returns True.   

        Paramaters
        ----------
        emitter - the emitter to add into this circuit's list of emitters

        Returns
        ----------
        Returns true if all checks are passed and the emitter is added into
        the circuit.
        Else, if any of the checks are not passed, prints an error message
        stating the cause of the error and returns False, skipping any
        remaining checks.

        Hint
        ----
        Use the get_collided_emitter method to check for position collision.
        You will need to find your own way to check for symbol collisions
        with other emitters.
        '''
        if not isinstance(emitter, Emitter):
            return False
        else:
            x = emitter.get_x()
            y = emitter.get_y()
            if not in_the_board(self.width, self.height, x, y):
                print(f'Error: position ({x}, {y}) is out-of-bounds of {self.width}x{self.height} circuit board')
                return False
            elif not (self.get_collided_emitter(emitter) == None):
                print(f"Error: position ({x}, {y}) is already taken by emitter '{self.get_collided_emitter(emitter).get_symbol()}'")
                return False
            elif not valid_symbol(emitter, self.emitters):
                print(f"Error: symbol '{emitter.get_symbol()}' is already taken.")
                return False
            
            self.emitters.append(emitter)
            self.emitters = sorter.sort_receivers_by_symbol(self.emitters)
            self.board_displayer.add_component_to_board(emitter)
            return True
                 

    
    def get_emitters(self) -> list[Emitter]:
        '''Returns emitters.'''
        return self.emitters
    
    def add_receiver(self, receiver: Receiver) -> bool:
        '''
        If receiver is not a Receiver instance, return False. Else, you need to
        perform the following checks in order for any errors:
          1)  The receiver's position is within the bounds of the circuit.
          2)  The receiver's position is not already taken by another emitter
              or receiver in the circuit.
          3)  The receiver's symbol is not already taken by another receiver in
              the circuit. 
             
        If at any point a check is not passed, an error message is printed stating
        the cause of the error and returns False, skipping any further checks. If 
        all checks pass, then the following needs to occur:
          1)  receiver is added in the circuit's list of receivers. receiver
              needs to be added such that the list of receivers  remains sorted
              in alphabetical order by the receiver's symbol. You can assume the
              list of receivers is already sorted before you add the receiver. 
          2)  receiver's symbol is added into board_displayer.
          3)  The method returns True.

        Paramaters
        ----------
        receiver - the receiver to add into this circuit's list of receivers

        Returns
        ----------
        Returns true if all checks are passed and the receiver is added into
        the circuit.
        Else, if any of the checks are not passed, prints an error message
        stating the cause of the error and returns False, skipping any
        remaining checks.

        Hint
        ----
        Use the get_collided_emitter and get_collided_receiver methods to
        check for position collisions.
        You will need to find your own way to check for symbol collisions
        with other receivers.
        '''
        if not isinstance(receiver, Receiver):
            return False
        else:
            x = receiver.get_x()
            y = receiver.get_y()
            if not in_the_board(self.width, self.height, x, y):
                print(f'Error: position ({x}, {y}) is out-of-bounds of {self.width}x{self.height} circuit board')
                return False
            elif not (self.get_collided_emitter(receiver) == None):
                collided_emitter = self.get_collided_emitter(receiver)
                print(f"Error: position ({receiver.get_x()}, {receiver.get_y()}) is already taken by emitter '{collided_emitter.get_symbol()}'")
                return False

            elif not (self.get_collided_receiver(receiver) == None):
                print(f"Error: position ({x}, {y}) is already taken by receiver '{self.get_collided_receiver(receiver).get_full_symbol()}'")
                return False
            elif not valid_symbol(receiver, self.receivers):
                print(f"Error: symbol '{receiver.get_full_symbol()}' is already taken")
                return False
            
            self.receivers.append(receiver)
            self.receivers = sorter.sort_receivers_by_symbol(self.receivers)
            self.board_displayer.add_component_to_board(receiver)
            return True



    def get_receivers(self) -> list[Receiver]:
        '''Returns receivers.'''
        return self.receivers


    def add_photon(self, photon: Photon) -> bool:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        If the photon passed in is not a Photon instance, it does not add it in
        and returns False. Else, it adds photon in this circuit's list of
        photons and returns True.

        Paramaters
        ----------
        photon - the photon to add into this circuit's list of photons

        Returns
        -------
        Returns True if the photon is added in, else False.
        '''
        if isinstance(photon, Photon):
            self.photons.append(photon)
            return True
        else:
            return False
            



    def get_photons(self) -> list[Photon]:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''Returns photons.'''
        return self.photons


    def add_mirror(self, mirror: Mirror) -> bool:
        # only requires implementation once you reach ADD-MY-MIRRORS
        '''
        If mirror is not a Mirror instance, return False. Else, you need to
        perform the following checks in order for any errors:
          1)  The mirror's position is within the bounds of the circuit.
          2)  The mirror's position is not already taken by another emitter, 
              receiver or mirror in the circuit.
             
        If at any point a check is not passed, an error message is printed
        stating the cause of theerror and returns False, skipping any further
        checks. If all checks pass, then the following needs to occur: 
          1)  mirror is added in the circuit's list of mirrors.
          2) mirror's symbol is added into board_displayer.
          3)   The method returns True.

        Paramaters
        ----------
        mirror - the mirror to add into this circuit's list of mirrors

        Returns
        ----------
        Returns true if all checks are passed and the mirror is added into
        the circuit.
        Else, if any of the checks are not passed, prints an error message
        stating the cause of the error and returns False, skipping any
        remaining checks.
        '''
        if not isinstance(mirror, Mirror):
            return False
        else:
            x = mirror.get_x()
            y = mirror.get_y()
            if not in_the_board(self.width, self.height, x, y):
                print(f'Error: position ({x}, {y}) is out-of-bounds of {self.width}x{self.height} circuit board')
                return False
            elif not (self.get_collided_emitter(mirror) == None):
                collided_emitter = self.get_collided_emitter(mirror)
                print(f"Error: position ({x}, {y}) is already taken by emitter '{self.get_collided_emitter(mirror).get_symbol()}'")
                return False
            elif not (self.get_collided_receiver(mirror) == None):
                print(f"Error: position ({x}, {y}) is already taken by receiver '{self.get_collided_receiver(mirror).get_full_symbol()}'")
                return False
            elif not (self.get_collided_mirror(mirror) == None):
                print(f"Error: position ({x}, {y}) is already taken by mirror '{self.get_collided_mirror(mirror).get_full_symbol()}'")
                return False                
            # elif not valid_symbol(mirror, self.mirrors):
            #     print(f"Error: symbol '{mirror.get_full_symbol()}' is already taken")
            #     return False

            else:
                self.board_displayer.add_component_to_board(mirror)
                self.mirrors.append(mirror)
                return True



    def get_mirrors(self) -> list[Mirror]:
        # only requires implementation once you reach ADD-MY-MIRRORS
        '''Returns mirrors.'''
        return self.mirrors

    
    def get_width(self) -> int:
        '''Returns width.'''
        return self.width


    def get_height(self) -> int:
        '''Returns height.'''
        return self.height 

