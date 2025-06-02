class MoneyMachine:
    def __init__(self):
        self.coins = {
            'Penny' : 0.01,
            'Dime': 0.10,
            'Nickel': 0.05,
            'Quarter': 0.25
        }
        self.money = 0.0

    def report(self):
        print(f"Money : ${self.money}")
    
    def make_payment(self,cost):
        money = 0.0
        for coin in self.coins:
            coin_entered = float(input(f"How many {coin}?: "))
            money += coin_entered*self.coins[coin]
        if cost<=money:
            self.money+=cost
            if cost<money:
                 print(f"Here is ${round(money - cost,2)} dollars in change.")
            return True
        print("Sorry that's not enough money. Money refunded")
        return False
        