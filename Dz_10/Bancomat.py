


class Bancomat:
    def __init__(self, deposit):
        self.deposit = deposit

    def __str__(self):
        return f"На вашем счету {self.deposit} рублей"

    def replenish(self, money):
        if money < 50:
            raise TypeError("Сумма должна быть не менее 50 рублей")
        if money % 50 != 0:
            raise TypeError("Сумма должна быть кратна 50")
        self.deposit += money

    def  take_money(self, money):
        if money > self.deposit:
            raise TypeError("Не достаточно средств")
        if money % 50 != 0:
            raise TypeError("Сумма должна быть кратна 50")
        self.deposit -= money

mon = Bancomat(100)
print(mon)
mon.replenish(1000)
print(mon)
mon.take_money(500)
print(mon)