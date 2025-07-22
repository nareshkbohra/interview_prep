from enum import Enum
import heapq
from time import sleep


class Direction(Enum):
    IDLE = 0
    UP = 1
    DOWN = -1


class RequestQueue:
    def __init__(self, min_first=True):
        self.requests = []
        self.requests_set = set()
        self.min_first = min_first

    def add(self, floor):
        if floor in self.requests_set:
            return

        self.requests_set.add(floor)
        if not self.min_first:
            floor = -floor
        heapq.heappush(self.requests, floor)

    def next_item(self):
        item = self.requests[0]
        if not self.min_first:
            item = -item
        return item

    def pop(self):
        floor = heapq.heappop(self.requests)
        if not self.min_first:
            floor = -floor
        self.requests_set.remove(floor)

    def is_empty(self):
        return len(self.requests) == 0


class Elevator:
    def __init__(self, max_floor: int, min_floor: int):
        self.max_floor = max_floor
        self.min_floor = min_floor

        self.up_requests_queue = RequestQueue(min_first=True)
        self.down_requests_queue = RequestQueue(min_first=False)

        self.current_dir = Direction.IDLE
        self.current_floor = 0

    def add_external_request(self, floor: int, direction: Direction):
        if direction == Direction.UP:
            self.up_requests_queue.add(floor)
        else:
            self.down_requests_queue.add(floor)

    def add_internal_request(self, floor):
        if floor > self.current_floor:
            self.up_requests_queue.add(floor)
        else:
            self.down_requests_queue.add(floor)

    def step(self):
        """
        This is a function which need to call to "take a step" in elevator.
        At each "step", elevator can do below things:
            1. Do nothing if there are no requests.
            2. If it is moving up and their are any up request keep moving up.
            3. If it is moving down and their are any down request keep moving down.
            4. If it is ideal, check if there are any request in any direction then start moving
               in that direction

        NOTE: Here changing direction is also a step which simplify the design.
        """
        if self.current_dir == Direction.IDLE:
            if not self.up_requests_queue.is_empty():
                self.current_dir = Direction.UP
            elif not self.down_requests_queue.is_empty():
                self.current_dir = Direction.DOWN
            return

        if self.current_dir == Direction.UP:
            if self.up_requests_queue.is_empty():
                self.current_dir = Direction.IDLE
                return

            # Just move to 1 floor above and see if the floor is in request
            self.current_floor += 1
            next_request = self.up_requests_queue.next_item()
            if next_request == self.current_floor:
                print(f"Reached floor {next_request}")
                sleep(1)
                self.up_requests_queue.pop()

            return

        # we are here which means we are moving in down direction
        if self.down_requests_queue.is_empty():
            self.current_dir = Direction.IDLE
            return

        self.current_floor -= 1
        next_request = self.down_requests_queue.next_item()
        if next_request == self.current_floor:
            print(f"Reached floor {next_request}")
            sleep(1)
            self.down_requests_queue.pop()

    def cost_to_reach(self, floor: int, direction: Direction):
        """
        Cost to reach and go to given direction is calculated as follows:
            1. If elevator is idle, then it is simple distance between floors.
            2. If it is going in the same direction as request and CAN pick request up, then also
               it is just distance between floors.
            3. Otherwise elevator have to do round trip, just assume it to be infinity.
               It can be optimized but there are too many combinations.
        """
        if self.current_dir == Direction.IDLE:
            return abs(self.current_floor - floor)

        if self.current_dir != direction:
            return 1_000_000

        if self.current_dir == Direction.UP and self.current_floor > floor:
            return 1_000_000

        if self.current_dir == Direction.DOWN and self.current_floor < floor:
            return 1_000_000

        return abs(self.current_floor - floor)


class ElevatorSystem:
    def __init__(self, max_floor: int, min_floor: int, number_of_elevators: int):
        self.elevators = [Elevator(max_floor=max_floor, min_floor=min_floor) for _ in range(number_of_elevators)]

    def add_request(self, floor: int, direction: Direction):
        _, elevator_id = min((elevator.cost_to_reach(floor, direction), i) for i, elevator in enumerate(self.elevators))
        elevator = self.elevators[elevator_id]
        elevator.add_external_request(floor, direction)

    def add_internal_request(self, elevator_id: int, floor: int):
        self.elevators[elevator_id].add_internal_request(floor)
