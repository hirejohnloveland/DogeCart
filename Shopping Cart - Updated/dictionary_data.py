class ShoppingCart():
    def __init__(self):
        self.dict_prices = {
            "Onions": .50,
            "Tomatoes": .99,
            "Eggs": 2.99,
            "Ice Cream": 4.99
        }
        self.dict_quant = {
            "Onions": 0,
            "Tomatoes": 0,
            "Eggs": 0,
            "Ice Cream": 0
        }

    def add_item(self, key):
        self.dict_quant[key] += 1

    def remove_item(self, key):
        if self.dict_quant[key] == 0:
            return
        else:
            self.dict_quant[key] -= 1

    def clear_cart(self):
        for keys in self.dict_quant.keys():
            self.dict_quant[keys] = 0

    def get_qty(self, key):
        return self.dict_quant[key]

    def get_pr(self, key):
        return '${:,.2f}'.format(self.dict_prices[key])

    def item_total(self, key):
        return '${:,.2f}'.format(self.dict_prices[key] * self.dict_quant[key])

    def subtotal(self):
        dict_subtotal = {}
        for k, v in self.dict_prices.items():
            dict_subtotal[k] = v * self.dict_quant[k]
        return dict_subtotal

    def get_total(self):
        total = 0
        subtotals = self.subtotal()
        for values in subtotals.values():
            total += values
        return '${:,.2f}'.format(total)
