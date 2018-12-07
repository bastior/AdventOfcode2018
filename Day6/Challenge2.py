import ChallengeIf
import datetime
import operator

class Day6Challange1(ChallengeIf.ChallengeIf):
    def __init__(self):
        self.TestInputs = [open("Input1T", 'r').read().split("\n")]
        self.TestOutputs = [16]
        self.Input = open("Input1", 'r').read().split("\n")

    def Run(self, arg):
        parsed_args = []
        for i in arg:
            temp = i.split(',')
            parsed_args.append((int(temp[0]), int(temp[1])))
        max_wide = max(parsed_args, key=lambda x: x[0])[0] + 2
        max_deep = max(parsed_args, key=lambda x: x[1])[1] + 2

        matrix = [[0 for x in range( max_wide)] for y in range(max_deep)]

        for i in range(max_deep):
            for j in range(max_wide):
                for k in range(len(parsed_args)):
                    point = parsed_args[k]
                    l = abs(i - point[1]) + abs(j-point[0])
                    matrix[i][j] += l

        number_of_fields = 0
        for i in range(max_deep):
            for j in range(max_wide):
                if matrix[i][j] < 10000:
                    number_of_fields += 1
        return number_of_fields

obj = Day6Challange1()
#obj.Test()
obj.Solve()