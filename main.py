"""
Ant colony optimization library usase cases
"""
from aco.ants import PrimitiveAnt
from aco.state_machines import DynamicStateMachine01


def main():
    """
    Entry point
    """
    number_of_ants = 100
    accum = []
    best_ants = []
    current_record = 0
    for idx in range(number_of_ants):
        test_state_machine = DynamicStateMachine01()
        test_ant = PrimitiveAnt(test_state_machine, str(idx))
        while test_ant.walk() != -1:
            pass
        accum.append(test_ant.distance)
        print(
            "ant:",
            test_ant.name,
            "distance:",
            test_ant.distance,
            "path:",
            test_ant.path,
        )
        if test_ant.distance == current_record:
            best_ants.append(test_ant)
        elif test_ant.distance > current_record:
            current_record = test_ant.distance
            best_ants = [test_ant]

    print("\nBest ants")
    for ant in best_ants:
        print("ant:", ant.name, "distance:", ant.distance, "path:", ant.path)


if __name__ == "__main__":
    main()
