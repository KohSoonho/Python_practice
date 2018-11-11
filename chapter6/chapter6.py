# 6-1
class Thing :
    pass

example = Thing()

print(Thing)
print(example)

# 6-2
class Thing2 :
    letters = "abc"

example2 = Thing2()
print(example2.letters)

# 6-3
class Thing3 :
    def __init__(self) :
        self.letters = "xyz"

example3 = Thing3()
print(example3.letters)

# 6-4
class Element :
    def __init__(self, name, symbol, number) :
        self.name = name
        self.symbol = symbol
        self.number = number

hydrogen = Element("Hydrogen", "H", 1)
print(hydrogen.name, hydrogen.symbol, hydrogen.number)

# 6-5
element_dict = {"name" : "Hydrogen",
                "symbol" : "H",
                "number" : 1}

hydrogen2 = Element(element_dict["name"], element_dict["symbol"], element_dict["number"])
print(hydrogen2.name, hydrogen2.symbol, hydrogen2.number)

# 6-6
class Element2 :
    def __init__(self, name, symbol, number) :
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self) :
        print("name=%s, symbol=%s, number=%s" %
        (self.name, self.symbol, self.number))

hydrogen3 = Element2("Hydrogen", "H", 1)
hydrogen3.dump()

# 6-7
print(hydrogen3)

class NewElement2 :
    def __init__(self, name, symbol, number) :
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self) :
        return ("name=%s, symbol=%s, number=%s" %
        (self.name, self.symbol, self.number))

new_hydrogen3 = NewElement2("Hydrogen", "H", 2)
print(new_hydrogen3)

#6-8
class Element3 :
    def __init__(self, name, symbol, number) :
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    @property
    def name(self) :
        return self.__name
    @property
    def symbol(self) :
        return self.__symbol
    @property
    def number(self) :
        return self.__number

hydrogen4 = Element3("Hydrogen", "H", 1)
print(hydrogen4.name, hydrogen4.symbol, hydrogen4.number)

# hydrogen.number = 2     # This attribute can be changed
# print(hydrogen.number)
#
# hydrogen4.number = 2    # This is error, property cannot be changed without setter

# 6-9
class Bear :
    def eats(self) :
        return "berries"

class Rabbit :
    def eats(self) :
        return "clover"

class Octothorpe :
    def eats(self) :
        return "campers"

bear = Bear()
print(bear.eats())

rabbit = Rabbit()
print(rabbit.eats())

octothorpe = Octothorpe()
print(octothorpe.eats())

# 6-10
class Laser :
    def does(self) :
        return "disintegrate"

class Claw :
    def does(self) :
        return "crush"

class SmartPhone :
    def does(self) :
        return "ring"

class Robot :
    def __init__(self) :
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()
    def does(self) :
        return """I have many attathments:
        My laser, %s,
        My claw, %s
        My smart_phone, %s""" % (
        self.laser.does(),
        self.claw.does(),
        self.smartphone.does())

robot = Robot()
print(robot.does())
