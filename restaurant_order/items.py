from restaurant_order.menu_items import MenuItems


class Idly(MenuItems):
    def __init__(self,name,price,type):
        super().__init__(name,price)
        self.type = type

    def get_item_details(self):
        return f"{self.type} Idly {self.get_price()}"


class Dosa(MenuItems):
    def __init__(self, name, price, type):
        super().__init__(name, price)
        self.type = type

    def get_item_details(self):
        return f"{self.type} Dosa {self.get_price()}"


class FriedRice(MenuItems):
    def __init__(self, name, price, type):
        super().__init__(name, price)
        self.type = type

    def get_item_details(self):
        return f"{self.type} FriedRice {self.get_price()}"






