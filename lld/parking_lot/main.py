import logging
import os

from lot import ParkingLot, VehicleSize, Vehicle


def setup_logging():
    log_level = os.environ.get("LOG_LEVEL") or "DEBUG"
    numeric_level = getattr(logging, log_level.upper(), None)

    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {log_level}")

    logging.basicConfig(level=numeric_level)


def main():
    setup_logging()
    parking_lot = ParkingLot(floors=5, slots_per_floor=10, gates=[(1, 2), (4, 8)])
    first_car = Vehicle(size=VehicleSize.MEDIUM, number="ABC")
    parking_lot.enter(1, first_car)
    parking_lot.exit(first_car.number)


if __name__ == "__main__":
    main()
