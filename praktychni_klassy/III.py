class Human:
    pass


class Man(Human):
    pass


class Woman(Human):
    pass


class God:
    @staticmethod
    def create():
        return [Man(), Woman()]

humans = God.create()
print(type(humans[0]))
print(type(humans[1]))