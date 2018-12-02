import ChallengeIf
import itertools

class Day1Challange1(ChallengeIf.ChallengeIf):
    def __init__(self):
        self.TestInputs = [[+1, -1], [+3, +3, +4, -2, -4], [-6, +3, +8, +5, -6], [+7, +7, -2, -7, -4]]
        self.TestOutputs = [0, 10, 5, 14]
        self.Input = [int(a) for a in open("Input2", 'r').read().split()]

    def Run(self, arg):
        freq = 0
        freq_list = [0]
        for num in itertools.cycle(arg):
            freq += num
            if freq in freq_list:
                return freq
            else:
                freq_list.append(freq)

obj = Day1Challange1()
#obj.Test()
obj.Solve()