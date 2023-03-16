import time
from random import randint
import os

def log(func):
    def decorator_function(*args):
        status = f"{(' '.join(func.__name__.split('_')).title())}"
        user = os.getenv('USER')
        tm = time.time()
        val = func(*args)
        tm = time.time() - tm
        if (float(f"{tm:.3f}") == 0):
            m = "ms"
            tm *= 1000
        else:
            m = "s"
        with open("machine.log", 'a') as opened_file:
            log_message = f"({user})Running: {status:19}[ exec-time = {tm:5.3f} {m:2} ]\n"
            opened_file.write(log_message)
        return (val)
    return (decorator_function)

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
