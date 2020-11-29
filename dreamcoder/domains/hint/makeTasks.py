

from dreamcoder.type import *
from dreamcoder.task import Task
from dreamcoder.utilities import eprint, hashable

from random import randint, random, seed
from itertools import product

def make_list_bootstrap_tasks():
    seed(42)

    def suffixes(l):
        if l == []:
            return []
        else:
            return [l[1:]] + suffixes(l[1:])

    def randomList(minValue=0, maxValue=20, len=1):
        return [randint(minValue, maxValue) for _ in range(int(len))]

    def generate_divide_examples ():
        i = 0
        lists = []
        lists.append(((4,8), 0))
        lists.append(((3,7), 0))
        lists.append(((5,28), 0))
        lists.append(((4,47), 0))
        lists.append(((9,6), 1))
        lists.append(((8,7), 1))
        lists.append(((5,3), 1))
        lists.append(((24,16), 1))
        lists.append(((49,27), 1))
        lists.append(((25,23), 1))
        while i < 20:
            a = randomList(len=n_sample*(1-noise))[0]
            b = randomList(minValue=1, len=n_sample*(1-noise))[0]

            if a // b >= 2 and ((a, b), _div(a,b)) not in lists:
                lists.append(((a, b), _div(a,b)))  
                i += 1
        

        return lists

    def generate_noise(n):
        return list(zip(zip(randomList(len=n), randomList(len=n)), randomList(len=n)))

    # Functions to be learnt
    def _add(x, y): return x + y
    def _minus(x, y): return max(0, x - y)
    # def _minus(x, y): return x - y
    def _mul(x, y): return x * y
    def _div(x, y): return x // y

    n_sample = 20
    noise = 0

    operatorBootstrap = [
        Task ("add", arrow(tint, tint, tint),
             generate_noise(n_sample*noise) + 
             [((a, b), _add(a,b)) for a, b in zip(randomList(len=n_sample*(1-noise)), randomList(len=n_sample*(1-noise)))]),
        Task ("minus", arrow(tint, tint, tint),
             generate_noise(n_sample*noise) + 
             [((a, b), _minus(a,b)) for a, b in zip(randomList(len=n_sample*(1-noise)), randomList(len=n_sample*(1-noise)))]),
        Task ("multiply", arrow(tint, tint, tint),
             generate_noise(n_sample*noise) + 
             [((a, b), _mul(a,b)) for a, b in zip(randomList(len=n_sample*(1-noise)), randomList(len=n_sample*(1-noise)))]),
        # Task ("divide", arrow(tint, tint, tint),
        #      generate_noise(n_sample*noise) + 
        #      [((a, b), _div(a,b)) for a, b in zip(randomList(len=n_sample*(1-noise)), randomList(minValue=1, len=n_sample*(1-noise)))]),
        Task ("divide", arrow(tint, tint, tint),
             generate_noise(n_sample*noise) + 
             generate_divide_examples()),
    ]

    return operatorBootstrap


def exportTasks():
    import sys
    import pickle as pickle

    n_examples = 15
    if len(sys.argv) > 1:
        n_examples = int(sys.argv[1])

    eprint("Downloading and generating dataset")
    tasks = sorted(make_list_tasks(n_examples), key=lambda t: t.name)
    eprint("Got {} list tasks".format(len(tasks)))

    with open("data/list_tasks.pkl", "w") as f:
        pickle.dump(tasks, f)
    eprint("Wrote list tasks to data/list_tasks.pkl")