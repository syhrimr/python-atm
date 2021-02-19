class ATMCard:
    def __init__(self, defaultPin, defaultBalance):
        self.defaultBalance = defaultBalance
        self.defaultPin = defaultPin

    def cekPinAwal(self):
        return self.defaultPin

    def cekSaldoAwal(self):
        return self.defaultBalance