import pytest
from ..lot import ParkingLot, Vehicle, VehicleSize


@pytest.fixture
def simple_parking_lot():
    # Create a parking lot with 1 floor, 6 slots, 2 gates
    # Slot types pattern: [SMALL, MEDIUM, LARGE, SMALL, MEDIUM, LARGE]
    return ParkingLot(floors=1, slots_per_floor=6, gates=[(0, 0), (0, 5)])


def test_can_park_vehicle(simple_parking_lot):
    vehicle = Vehicle(VehicleSize.SMALL, "KA01AB1234")
    simple_parking_lot.enter(gate_number=0, vehicle=vehicle)
    assert "KA01AB1234" in simple_parking_lot.occupied_slots()


def test_unparking_frees_the_slot(simple_parking_lot):
    vehicle = Vehicle(VehicleSize.MEDIUM, "MH12YY9999")
    simple_parking_lot.enter(0, vehicle)
    before_exit = simple_parking_lot.get_parking_status()[VehicleSize.MEDIUM]

    simple_parking_lot.exit("MH12YY9999")
    after_exit = simple_parking_lot.get_parking_status()[VehicleSize.MEDIUM]

    # One more slot should be available
    assert after_exit == before_exit + 1


def test_unpark_and_reuse_same_slot(simple_parking_lot):
    """Verify same slot is reused (nearest) after it's freed."""
    v1 = Vehicle(VehicleSize.LARGE, "DL05AB8888")
    simple_parking_lot.enter(0, v1)
    slot1 = simple_parking_lot.find_vehicle("DL05AB8888")

    simple_parking_lot.exit("DL05AB8888")

    v2 = Vehicle(VehicleSize.LARGE, "DL05CD9999")
    simple_parking_lot.enter(0, v2)
    slot2 = simple_parking_lot.find_vehicle("DL05CD9999")

    assert slot1 == slot2  # Slot is reused if it's still nearest


def test_duplicate_vehicle_raises_error(simple_parking_lot):
    v = Vehicle(VehicleSize.SMALL, "KA02AA0001")
    simple_parking_lot.enter(0, v)

    with pytest.raises(ValueError, match="already parked"):
        simple_parking_lot.enter(1, v)  # Same vehicle, different gate


def test_full_lot_raises_error(simple_parking_lot):
    # Only 2 SMALL slots in pattern [S, M, L, S, M, L]
    v1 = Vehicle(VehicleSize.SMALL, "V1")
    v2 = Vehicle(VehicleSize.SMALL, "V2")
    v3 = Vehicle(VehicleSize.SMALL, "V3")

    simple_parking_lot.enter(0, v1)
    simple_parking_lot.enter(0, v2)

    with pytest.raises(ValueError, match="full"):
        simple_parking_lot.enter(0, v3)


def test_vehicle_lookup(simple_parking_lot):
    v = Vehicle(VehicleSize.MEDIUM, "FIND123")
    simple_parking_lot.enter(1, v)
    floor, slot = simple_parking_lot.find_vehicle("FIND123")
    assert isinstance(floor, int)
    assert isinstance(slot, int)


def test_multi_gate_consistency(simple_parking_lot):
    v1 = Vehicle(VehicleSize.LARGE, "G1")
    v2 = Vehicle(VehicleSize.LARGE, "G2")

    simple_parking_lot.enter(0, v1)
    simple_parking_lot.enter(1, v2)

    occupied = list(simple_parking_lot.occupied_slots().values())
    assert len(occupied) == 2
    assert occupied[0][:2] != occupied[1][:2]  # Different slots for each gate
