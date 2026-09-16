class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item : str, price : float | int, quantity : int = 1):
        if item in [i["item"] for i in self.items]:
            for i in self.items:
                if i["item"] == item:
                    i["quantity"] += quantity
                    i["price"] = price
                    break
        else:
            self.items.append({ "item": item, "price": price, "quantity": quantity })

    def remove_item(self, item):
            self.items.remove(next(i for i in self.items if i["item"] == item))

    def get_total(self):
        return sum(item["price"] * item["quantity"] for item in self.items)
