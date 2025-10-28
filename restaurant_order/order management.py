from restaurant_order.Payment import Card
from restaurant_order.items import Idly, Dosa, FriedRice


class Order:
    TAX_RATE = 0.05
    def __init__(self):
        self.items=[]

    def add_item(self,item):
        self.items.append(item)

    def calculate_total(self):
         sub_total = sum (item.get_price()for item in self.items)
         tax = sub_total * self.TAX_RATE
         return sub_total+tax

    def show_bill(self):
         print("--------your bill is--------")
         for item in self.items:
             print(item.get_item_details())
         total = self.calculate_total()
         print(f"Total (inc.GST):₹{round(total,2)}")
         return total

if __name__ == "__main__":
  idly = Idly("idly",95,"gheepodi")
  dosa = Dosa("dosa",110,"masala")
  rice= FriedRice("friedrice",225,"mushroom")
  order = Order()
  order.add_item(idly)
  order.add_item(dosa)
  order.add_item(rice)

  total_amount = order.show_bill()

  payment_method = Card()
  payment_method.make_payment(total_amount)





