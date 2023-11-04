# class Grandparent:
#     height = 170
#     satiety = 100
#     age = 60
#
#
# class Parent(Grandparent):
#     age = 40
#
#
# class Child(Parent):
#     height = 90
#
#     def __init__(self):
#         print(self.height)
#         print(self.satiety)
#         print(self.age)
#
#
# nick = Child()


class Hello_world:
    hello ="Hello"
    _hello = "_Hello"
    __hello = "__Hello"

    def __init__(self):
        self.world = "world"
        self._world = "_world"
        self.__world = "__world"
    def printer(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)
    def _get_printer(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)

class Hi(Hello_world):
    def hi_print(self):
        print(self.hello)
        print(self.world)
        print(self._hello)
        print(self._world)
        print(self.__hello)
        print(self.__world)
hello = Hello_world()
hello.printer()
hello._get_printer()
# hi = Hi()
# hi.hi_print()