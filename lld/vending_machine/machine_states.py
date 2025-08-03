from abc import ABC, abstractmethod
from .currency import Currency


class VendingMachineState(ABC):
    def __init__(self, machine):
        self.machine = machine

    @abstractmethod
    def select_item(self, item_name: str, quantity: int):
        pass

    @abstractmethod
    def add_currency(self, currency: Currency):
        pass

    @abstractmethod
    def press_lever(self):
        pass


class IdleVendingMachineState(VendingMachineState):
    def select_item(self, item_name: str, quantity: int):
        machine = self.machine
        item = machine.inventory.get(item_name)
        if item is None:
            raise ValueError("Item is not present in vending machine")
        if item.quantity < quantity:
            raise ValueError("Insufficient quantity")

        machine.selected_item = item
        machine.selected_quantity = quantity
        machine.current_state = machine.in_use_state

    def add_currency(self, currency: Currency):
        raise RuntimeError("An item need to be selected first")

    def press_lever(self):
        raise RuntimeError("An item need to be selected first")


class InUseVendingMachineState(VendingMachineState):
    def select_item(self, item_name: str, quantity: int):
        machine = self.machine
        raise RuntimeError(f"Item {machine.selected_item} is already selected")

    def add_currency(self, currency: Currency):
        machine = self.machine
        required_money = machine.selected_item.price * machine.selected_quantity
        machine.current_money += currency.value
        if machine.current_money >= required_money:
            machine.current_state = machine.dispensing_state

    def press_lever(self):
        raise ValueError("Insufficient funds")


class DispensingVendingMachineState(VendingMachineState):
    def select_item(self, item_name: str, quantity: int):
        machine = self.machine
        raise RuntimeError(f"Item {machine.selected_item} is already selected")

    def add_currency(self, currency: Currency):
        raise RuntimeError("Sufficient funds are present, please press lever")

    def press_lever(self):
        machine = self.machine
        required_money = machine.selected_item.price * machine.selected_quantity
        extra_money = machine.current_money - required_money
        print(f"Dispatching item {machine.selected_item.name} with change amout {extra_money}")

        machine.current_state = machine.idle_state
        machine.selected_item.quantity -= machine.selected_quantity
        machine.selected_item = None
        machine.selected_quantity = 0
        machine.current_money = 0
