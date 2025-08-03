from typing import List
from .machine_states import IdleVendingMachineState, InUseVendingMachineState, DispensingVendingMachineState
from .currency import Currency


class Item:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity


class VendingMachine:
    def __init__(self, items: List[Item]):
        self.inventory = {item.name: item for item in items}

        self.selected_item = None
        self.selected_quantity = 0
        self.current_money = 0

        self.idle_state = IdleVendingMachineState(self)
        self.in_use_state = InUseVendingMachineState(self)
        self.dispensing_state = DispensingVendingMachineState(self)

        self.current_state = self.idle_state

    def select_item(self, item_name: str, quantity: int):
        self.current_state.select_item(item_name, quantity)

    def add_currency(self, currency: Currency):
        self.current_state.add_currency(currency)

    def press_lever(self):
        return self.current_state.press_lever()
