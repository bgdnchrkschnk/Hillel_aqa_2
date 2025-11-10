class BankAccount:

    def __init__(self, name, age, card="classic"):
        self.name = name # public
        self.age = age
        self._card = card # protected
        self.__creating_a_balance()
        self.__history = []

    def __creating_a_balance(self): # private
        self.__balance = 0 # private

    def get_my_balance(self):
        return self.__balance

    def send_money(self, amount, recipient):
        if self.__balance < amount:
            raise ValueError("Not enough money")
        self.__history.append({"recipient": recipient, "amount": amount})
        self.__balance -= amount

    def get_history(self):
        return self.__history

    def add_money_to_balance(self, amount, method="card"):
        self.__balance += amount


#
# account = BankAccount(name="Bohdan", age=29)
#
#
# print(account.name)
# print(account.age)
# print(account._card)
# print(account.get_my_balance())
#
# account.add_money_to_balance(100)
#
# account.send_money(amount=75, recipient="jkefnjk@test.com")
# print(account.get_my_balance())
#
#
# print(account.get_history())


