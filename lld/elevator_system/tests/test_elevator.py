import pytest
from ..elevators import Elevator, ElevatorSystem, Direction


@pytest.fixture
def elevator():
    return Elevator(max_floor=15, min_floor=0)


@pytest.fixture
def system():
    return ElevatorSystem(max_floor=15, min_floor=0, number_of_elevators=2)


def test_add_internal_request_changes_direction_up(elevator):
    elevator.current_floor = 0
    elevator.add_internal_request(5)

    elevator.step()
    assert elevator.current_dir == Direction.UP
    assert elevator.current_floor == 0

    elevator.step()
    assert elevator.current_floor == 1


def test_add_internal_request_changes_direction_down(elevator):
    elevator.current_floor = 10
    elevator.add_internal_request(5)

    elevator.step()
    assert elevator.current_dir == Direction.DOWN
    assert elevator.current_floor == 10

    elevator.step()
    assert elevator.current_floor == 9


def test_step_movement_up_and_down(elevator):
    elevator.current_floor = 0
    elevator.add_internal_request(3)

    elevator.step()  # direction set
    elevator.step()  # 1
    elevator.step()  # 2
    elevator.step()  # 3 (reached)

    elevator.step()  # Evaluate to IDLE
    assert elevator.current_dir == Direction.IDLE
    assert elevator.current_floor == 3


def test_idle_behavior_with_no_requests(elevator):
    elevator.current_dir = Direction.IDLE
    floor = elevator.current_floor

    for _ in range(3):
        elevator.step()
        assert elevator.current_floor == floor
        assert elevator.current_dir == Direction.IDLE


def test_elevator_direction_switch(elevator):
    elevator.current_floor = 5
    elevator.add_internal_request(8)
    elevator.add_internal_request(2)

    assert elevator.current_dir == Direction.IDLE
    elevator.step()  # sets UP
    assert elevator.current_dir == Direction.UP

    # Move toward 8
    while elevator.current_floor < 8:
        elevator.step()

    # Reach 8
    assert elevator.current_floor == 8
    assert elevator.current_dir == Direction.UP

    elevator.step()  # serves floor 8, transitions to IDLE
    assert elevator.current_dir == Direction.IDLE

    elevator.step()  # sets direction to DOWN due to pending request at 2
    assert elevator.current_dir == Direction.DOWN

    while elevator.current_floor > 2:
        elevator.step()

    elevator.step()  # serve 2
    elevator.step()  # become IDLE
    assert elevator.current_floor == 2
    assert elevator.current_dir == Direction.IDLE


def test_external_request_assigns_correct_elevator(system):
    system.add_request(5, Direction.UP)
    assigned = any(5 in e.up_requests_queue.requests_set for e in system.elevators)
    assert assigned


def test_external_request_skips_wrong_direction(system):
    e0 = system.elevators[0]
    e0.current_floor = 3
    e0.add_internal_request(10)
    e0.step()  # going UP

    # Elevator 1 is idle
    system.add_request(6, Direction.DOWN)

    assert 6 not in e0.down_requests_queue.requests_set
    assert 6 in system.elevators[1].down_requests_queue.requests_set


def test_cost_to_reach_logic(elevator):
    elevator.current_floor = 5
    elevator.current_dir = Direction.IDLE
    assert elevator.cost_to_reach(8, Direction.UP) == 3

    elevator.current_dir = Direction.UP
    assert elevator.cost_to_reach(7, Direction.UP) == 2
    assert elevator.cost_to_reach(2, Direction.UP) == 1_000_000

    elevator.current_dir = Direction.DOWN
    elevator.current_floor = 10
    assert elevator.cost_to_reach(7, Direction.DOWN) == 3
    assert elevator.cost_to_reach(12, Direction.DOWN) == 1_000_000
