import ChallengeIf

class Day1Challange1(ChallengeIf.ChallengeIf):
    def __init__(self):
        self.TestInputs = [[+1, +1, +1], [+1, +1, -2], [-1, -2, -3]]
        self.TestOutputs = [3, 0, -6]
        self.Input = [int(a) for a in open("Input1", 'r').read().split()]

    def Run(self, arg):
        return sum(arg)

obj = Day1Challange1()
obj.Test()
obj.Solve()