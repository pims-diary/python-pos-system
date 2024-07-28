import Resources.Resources


class Discounts:
    def __init__(self):
        self.other_costs = {}
        self.mode = ''
        self.value = 0.0
        self.discounted_amount = 0.0

    @property  # this is also automatically the getter
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value: mode):
        self._mode = value

    @property  # this is also automatically the getter
    def value(self):
        return self._value

    @value.setter
    def value(self, value: int):
        self._value = value

    @property  # this is also automatically the getter
    def discounted_amount(self):
        return self._discounted_amount

    @discounted_amount.setter
    def discounted_amount(self, value: int):
        self._discounted_amount = value
