class supermarket():
    name = "Sai Mart"
    location = "Trichy"

    def __init__(self,customer):
        self.customer = customer

    def items(self, product_quantity, product):
        self.prod_quant = product_quantity
        self.prod = product
        print(self.prod_quant)
        print(self.prod)

obj = supermarket("Ranjith")
print(obj.name)
print(obj.location)
print(obj.customer)
obj.items(1, "paste")
