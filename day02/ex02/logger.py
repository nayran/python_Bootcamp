import time
import os
from random import randint


def log(func):
    def timer(*args, **kwargs):
        start = time.time()
        final = func(*args, **kwargs)
        end = time.time()
        ft = end - start
        if ft > 0.5:
            ft = ("%.4f s" % (end - start))
        else:
            ft = ("%.4f ms" % ((end - start) * 1000))
        name = func.__name__
        name = name.replace('_', ' ')
        t = open("machine.log", "a+")
        t.write(f"({os.getlogin()})Running: {name.ljust(20)}")
        t.write(f"[ exec-time = {ft} ] \n")
        return final
    return timer


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
