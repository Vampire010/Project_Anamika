# child class
from Inheritance.Bird import Bird


class Penguin(Bird):
    def __init__(self):
        # call super() function

        print("Penguin is ready")

    def whoisThis(self):

        print("Penguin")

    def run(self):

        print("Run faster")


peggy = Penguin()
peggy.whoisThis1()
peggy.whoisThis()
peggy.swim()
peggy.run()

