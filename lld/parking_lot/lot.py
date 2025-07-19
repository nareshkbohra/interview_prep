from collections import defaultdict
from dataclasses import dataclass
from enum import Enum
import heapq
from typing import List, Tuple, Dict


class VehicleSize(Enum):
    SMALL = 0
    MEDIUM = 1
    LARGE = 2


@dataclass(frozen=True)
class Vehicle:
    size: VehicleSize
    number: str


@dataclass(frozen=True)
class Slot:
    floor: int
    index: int
    type: VehicleSize


class Gate:
    def __init__(self, slots: List[Slot], floor: int, index: int, vertical_distance: int = 1):
        self.floor = floor
        self.index = index
        self.vertical_distance = vertical_distance

        # Heap: VehicleSize -> List[(distance, Slot)]
        self.slots: Dict[VehicleSize, List[Tuple[int, Slot]]] = self._heapify_slots(slots)

    def _heapify_slots(self, slots: List[Slot]) -> Dict[VehicleSize, List[Tuple[int, Slot]]]:
        slot_collection: Dict[VehicleSize, List[Tuple[int, Slot]]] = defaultdict(list)

        for slot in slots:
            distance = self._calculate_distance(slot.floor, slot.index)
            slot_collection[slot.type].append((distance, slot))

        for sized_slots in slot_collection.values():
            heapq.heapify(sized_slots)

        return slot_collection

    def _calculate_distance(self, floor: int, index: int) -> int:
        # Same floor = horizontal distance
        if floor == self.floor:
            return abs(self.index - index)
        # Different floor = cost of vertical + reach 0 on both floors
        return (self.vertical_distance * abs(floor - self.floor)) + index + self.index

    def enter(self, vehicle_size: VehicleSize) -> Slot:
        free_slots_heap = self.slots[vehicle_size]
        if not free_slots_heap:
            raise ValueError("Parking lot is full for this vehicle type")

        _, slot = heapq.heappop(free_slots_heap)
        return slot

    def already_occupied(self, slot: Slot):
        heap = self.slots[slot.type]
        index_to_remove = -1

        for i, (_, s) in enumerate(heap):
            if s.floor == slot.floor and s.index == slot.index:
                index_to_remove = i
                break

        if index_to_remove != -1:
            del heap[index_to_remove]
            heapq.heapify(heap)

    def add_slot(self, slot: Slot):
        distance = self._calculate_distance(slot.floor, slot.index)
        heapq.heappush(self.slots[slot.type], (distance, slot))


class ParkingLot:
    def __init__(self, floors: int, slots_per_floor: int, gates: List[Tuple[int, int]]):
        self.vehicle_to_slot_mapping: Dict[str, Slot] = {}

        # Create the slots
        slots = []
        for floor in range(floors):
            for index in range(slots_per_floor):
                vtype = self._get_slot_type(index)
                slots.append(Slot(floor=floor, index=index, type=vtype))

        # Initialize each gate with slot copies and position
        self.gates: List[Gate] = []
        for floor, index in gates:
            gate = Gate(slots=list(slots), floor=floor, index=index)
            self.gates.append(gate)

    def _get_slot_type(self, index: int) -> VehicleSize:
        mod = index % 3
        if mod == 0:
            return VehicleSize.SMALL
        elif mod == 1:
            return VehicleSize.MEDIUM
        else:
            return VehicleSize.LARGE

    def enter(self, gate_number: int, vehicle: Vehicle):
        if vehicle.number in self.vehicle_to_slot_mapping:
            raise ValueError(f"Vehicle {vehicle.number} is already parked")

        gate = self.gates[gate_number]
        slot = gate.enter(vehicle.size)

        # Remove the slot from other gates
        for i, other_gate in enumerate(self.gates):
            if i != gate_number:
                other_gate.already_occupied(slot)

        self.vehicle_to_slot_mapping[vehicle.number] = slot

    def exit(self, vehicle_number: str):
        if vehicle_number not in self.vehicle_to_slot_mapping:
            raise ValueError(f"Vehicle '{vehicle_number}' not found")

        slot = self.vehicle_to_slot_mapping[vehicle_number]

        for gate in self.gates:
            gate.add_slot(slot)

        del self.vehicle_to_slot_mapping[vehicle_number]

    def get_parking_status(self) -> Dict[VehicleSize, int]:
        """Return number of free slots of each type (aggregated from any gate)."""
        status = defaultdict(int)
        # Use the first gate as source of truth (all gates are kept in sync)
        main_gate = self.gates[0]
        for vtype in VehicleSize:
            status[vtype] = len(main_gate.slots[vtype])
        return dict(status)

    def find_vehicle(self, vehicle_number: str) -> Tuple[int, int]:
        if vehicle_number not in self.vehicle_to_slot_mapping:
            raise ValueError(f"Vehicle '{vehicle_number}' not found")
        slot = self.vehicle_to_slot_mapping[vehicle_number]
        return (slot.floor, slot.index)

    def occupied_slots(self) -> Dict[str, Tuple[int, int, VehicleSize]]:
        result = {}
        for number, slot in self.vehicle_to_slot_mapping.items():
            result[number] = (slot.floor, slot.index, slot.type)
        return result
