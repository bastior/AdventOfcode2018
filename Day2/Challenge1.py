import ChallengeIf

class Day2Challange1(ChallengeIf.ChallengeIf):
    def __init__(self):
        self.TestInputs = [["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]]
        self.TestOutputs = [12]
        self.Input = open("Input1", 'r').read().split()

    def Run(self, arg):
        twos = 0
        threes = 0
        for word in arg:
            d = {}
            for latter in word:
                if latter in d:
                    d[latter] += 1
                else:
                    d[latter] = 1
            if 2 in d.values():
                twos += 1
            if 3 in d.values():
                threes += 1
        return twos*threes

obj = Day2Challange1()
obj.Test()
obj.Solve()