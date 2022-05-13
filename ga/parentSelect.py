import sys
sys.path.append('.')

from random import randint
from ga.Population import Individua

def parentSelect(lst: list[Individua; ]) -> list[Individua; ]:
  """select parents for crossover

  Args:
      lst (list): list of population
  """
  index = lst.copy()
  rnd1 = randint(1, len(index) - 1)
  index = [i for i in filter(lambda x: x != rnd1, index)]
  rnd2 = randint(1, len(index) - 1)
  index = [i for i in filter(lambda x: x != rnd2, index)]
  rnd3 = randint(1, len(index) - 1)
  index = [i for i in filter(lambda x: x != rnd3, index)]
  rnd4 = randint(1, len(index) - 1)
  index = [i for i in filter(lambda x: x != rnd4, index)]
  p1: None
  p2: None
  if(lst[rnd1].fitness > lst[rnd2].fitness):
    p1 = lst[rnd1]
  else:
    p1 = lst[rnd2]
  if(lst[rnd3].fitness > lst[rnd4].fitness):
    p2 = lst[rnd3]
  else:
    p2 = lst[rnd4]
  return [p1, p2]
