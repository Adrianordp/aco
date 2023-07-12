"""
Ant colony optimization library usage cases
"""
from aco.ants import PrimitiveAnt
from aco.state_machines import DynamicStateMachineExample01


def main():
    """
    Entry point
    """
    number_of_ants = 100
    ant_accumulator = []
    best_ants = []
    current_distance_record = 0
    for idx in range(number_of_ants):
        test_state_machine = DynamicStateMachineExample01()
        test_ant = PrimitiveAnt(test_state_machine, str(idx))
        while test_ant.walk() != -1:
            pass
        ant_accumulator.append(test_ant.distance)
        print(
            "ant:",
            test_ant.name,
            "distance:",
            test_ant.distance,
            "path:",
            test_ant.path,
        )
        if test_ant.distance == current_distance_record:
            best_ants.append(test_ant)
        elif test_ant.distance > current_distance_record:
            current_distance_record = test_ant.distance
            best_ants = [test_ant]

    print("\nBest ants")
    for ant in best_ants:
        print("ant:", ant.name, "distance:", ant.distance, "path:", ant.path)


if __name__ == "__main__":
    main()
