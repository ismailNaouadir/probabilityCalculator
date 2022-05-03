import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def get_contents(self):
        return self.contents

    def draw(self, number):
        if number > len(self.contents):
            return self.contents
        else:
            drawList = []
            for _ in range(number):
                elem = random.choice(self.contents)
                drawList.append(elem)
                self.contents.pop(self.contents.index(elem))
            return drawList


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    return len(expected_balls)
