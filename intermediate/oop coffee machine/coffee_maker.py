class CoffeeMaker:
    def __init__(self):
        self.resources = {
                        'Water': 300, 
                        'Milk': 200, 
                        'Coffee': 100,
                }

    def report(self):
        for items in self.resources:
            if items == 'Water' or items == 'Milk':
                print(f"{items} : {self.resources[items]}ml")
            else:
                print(f"{items} : {self.resources[items]}g")

    def is_resource_sufficient(self,drink):
        resources = drink.ingredients
        for items in resources:
            if resources[items] > self.resources[items]:
                return False
        return True
    
    def make_coffee(self,order):
        resources = order.ingredients
        if self.is_resource_sufficient(order):
            for item in self.resources:
                self.resources[item] -= resources[item]
            return True
        for items in resources:
            if resources[items] > self.resources[items]:
                print(f"Sorry there is not enough {items.lower()}")
                break
        return False
