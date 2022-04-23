import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, *args):
    self.contents = []
    for arg in args:
      n = int(arg.split('=')[1])
      for i in range(n):
        self.contents.append(arg.split('=')[0])


  def get_contents(self):
    return self.contents


#def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
