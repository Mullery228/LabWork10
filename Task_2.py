
class Clothes:

    def __init__(self, value: float):
        self.value = value


class Coat(Clothes):

    def calculate(self):
        result = float(self.value) / 6.5 + 0.5
        return "%.2f" % result

class Costume(Clothes):

    def calculate(self):
        result = 2 * float(self.value) + 0.3
        return "%.2f" % result

if __name__ == '__main__':
    coat = Coat(45.0)
    costume = Costume(3)

    print(coat.calculate())  # 7.42
    print(costume.calculate())  # 6.3