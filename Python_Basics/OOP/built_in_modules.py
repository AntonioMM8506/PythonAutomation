#import math => imports the whole math module and you can access its functions and constants using math.sqrt, math.pi, etc.
from math import sqrt, pi, e
import modules_external.car as car_module

class ModulesDemo():
    def built_in_modules(self):
        print(sqrt(16))
        print(pi)
        print(e)

    def car_description(self):
        car_module.info("BMW", "X5", 2020)

m = ModulesDemo()
m.built_in_modules()
m.car_description()