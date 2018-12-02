import ChallengeIf
from itertools import combinations

class Day2Challange2(ChallengeIf.ChallengeIf):
    def __init__(self):
        self.TestInputs = [["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]]
        self.TestOutputs = ["fgij"]
        # same input as in 1st
        self.Input = open("Input1", 'r').read().split()

    def Run(self, arg):
        for c in combinations(arg, 2):
            if sum(1 for a, b in zip(c[0], c[1]) if a != b) == 1:
                return "".join([a for a, b in zip(c[0], c[1]) if a == b])

obj = Day2Challange2()
obj.Test()
obj.Solve()