"""
State Machine catalog
"""

import numpy as np


class DynamicStateMachineExample01:
    """Dynamic state machine implementation 01"""

    def __init__(self):
        """
        self.initial_map (np.ndarray): square matrix with likelyhood weight on each path. Lines
        represent the "from state" and columns represet "to state". This variable is stored and
        preferrably not modified in case of reset of the machine.
        Consider the matrix:
        [[0, 5, 0],
         [2, 0, 8],
         [0, 0, 0]]
        It gives 3 states {0, 1 , 2}, one for each line (or column).
        - The first row indicates that there is a path connecting from state 0 and to state 1 and
          its reward is 5.
        - The second row: path connecting from state 1 to state 0 (reward 2) and other connecting
          from state 1 to state 2 (reward 8). Thus, it is 4 times more likely moving from from
          state 1 to state 2 than to state 0.
        - The third row: no path available. There is nowhere to go once this state is reached.

        self.map (np.ndarray): records the initial map and performs modifications as the machine
        updates

        self.num_states (int): records how many states are in the machine

        self.current_state (int): stores the current state where the machine is operating

        self.last_state (int): stores the last state where the machine was just operating before
        moving to current state
        """
        self.inital_map = np.array(
            [
                [0, 1, 0, 0, 0],
                [0, 0, 1, 0, 1],
                [0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
        self.map = self.inital_map
        self.num_states = len(self.inital_map)
        self.current_state = 0
        self.last_state = -1

    def update(self):
        """_summary_

        Args:
            current_state (int): _description_
        """

        # Check the current state and perform respective actions
        match self.current_state:
            case 0:
                self.state_0()
            case 1:
                self.state_1(self.last_state)
            case 2:
                self.state_2(self.last_state)
            case 3:
                self.state_3(self.last_state)
            case 4:
                self.state_4(self.last_state)
            case _:
                Exception("Unkown state")

    # Action performed on state 0
    def state_0(self):
        """State 0
        Do nothing.
        """
        self.current_state = 0
        self.last_state = -1

    # Action performed on state 1
    def state_1(self, origin: int):
        """State 1
        Do nothing.

        Args:
            origin (int): index of the state just before entering this state
        """
        self.current_state = 1
        self.last_state = origin

    # Action performed on state 2
    def state_2(self, origin: int):
        """State 2
        When it comes from state 1
        - removes path from state 1 to state 2;
        - creates path from state 1 to state 3;
        - creates path from state 3 to state 1.

        Args:
            origin (int): index of the state just before entering this state
        """
        self.current_state = 2
        self.last_state = origin

        if origin == 1:
            self.map[1][2] = 0
            self.map[1][3] = 1
            self.map[3][1] = 1

    # Action performed on state 3
    def state_3(self, origin: int):
        """State 3
        When it comes from state 1
        - removes path from state 1 to state 3;
        - creates path from state 1 to state 2;
        - creates path from state 2 to state 1.

        Args:
            origin (int): index of the state just before entering this state
        """
        self.current_state = 3
        self.last_state = origin

        if origin == 1:
            self.map[1][3] = 0
            self.map[1][2] = 1
            self.map[2][1] = 1

    # Action performed on state 4
    def state_4(self, origin: int):
        """State 4
        Do nothing.

        Args:
            origin (int): index of the state just before entering this state
        """
        self.current_state = 4
        self.last_state = origin


if __name__ == "__main__":
    print("No implementation for State Machine Catalog")
