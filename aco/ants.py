"""
Ant catalog
"""

import numpy as np


class PrimitiveAnt:
    """
    Primitive ant without pherormones
    """

    def __init__(self, state_machine: "StateMachine", name: str = ""):
        """_summary_

        Args:
            state_machine (StateMachine): State machine implementation where the ant is moving
            through
        self.name (str): ant's name
        self.current_state (int): state where the ant is on (>=-1)
        self.last_state (int): last state where the ant went from (>=-1)
        self.distance (float): total distance walked by the ant (>=0)
        self.path (list[int]): ordered list of the states walked by the ant
        """
        self.name = name
        self.state_machine = state_machine
        # self.current_state = state_machine.current_state
        # self.last_state = state_machine.last_state
        self.distance = 0
        self.path = []

    def walk(self) -> int:
        """The ant walks through states of the state machine

        Returns:
            int: index of the stage where the ant last visited.
            -1: ant has nowhere to go and the ant stays where it was
        """

        # Remembers the path it went through
        self.path.append(self.state_machine.current_state)

        # Lets the state machine operates its functions and updates its states ans paths
        self.state_machine.update()

        # Computes the probability of the ant chosing a specific path based on the machine
        # predefined path weights
        total_weight_sum = np.sum(
            self.state_machine.map[self.state_machine.current_state]
        )
        # If no path is available, return code -1: ant didn't move
        if total_weight_sum == 0:
            return -1
        sparse_probability = (
            np.cumsum(self.state_machine.map[self.state_machine.current_state])
            / total_weight_sum
        )
        random_choice = np.random.rand()
        # This is the state the ant is moving to
        next_state = np.argmax(sparse_probability > random_choice)

        # Adds the distance of the current track to the distante already walked
        self.distance += self.state_machine.map[self.state_machine.current_state][
            next_state
        ]

        # Records the new current state as the next state, since the ant has moved to next state
        self.state_machine.last_state = self.state_machine.current_state
        self.state_machine.current_state = next_state


if __name__ == "__main__":
    print("No implementation for Ant Catalog")
