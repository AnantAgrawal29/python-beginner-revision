
class MenuItem:
    def __init__(self):
        self.name = ""
        self.cost = 0.0
        self.ingredients = {}

class Menu:
    def __init__(self):
        self.coffee = {
                'espresso': {
                    'resources': {
                    'Water': 50,
                    'Milk': 0,
                    'Coffee': 18, 
                },
                    'Money': 1.5 
                },
            'latte':{
                'resources': {
                    'Water': 200, 
                    'Milk': 150, 
                    'Coffee': 24, 
                },
                'Money': 2.5
            },
            'cappuccino': {
                'resources': {
                    'Water': 250, 
                    'Milk': 100, 
                    'Coffee': 24, 
                },
                'Money': 3.0
            }
        }
    
    def get_items(self):
        coffee = ""
        for item in self.coffee:
            coffee += item + "/"
        return coffee
    
    def find_drink(self,order):
        for item in self.coffee:
            if item == order:
                coffee = MenuItem()
                coffee.name = item
                coffee.cost = self.coffee[item]['Money']
                coffee.ingredients = self.coffee[item]['resources']
                return coffee
        return 'None'