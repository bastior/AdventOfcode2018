import ChallengeIf
import datetime
import operator

class Day6Challange1(ChallengeIf.ChallengeIf):
    def __init__(self):
        self.TestInputs = [open("Input1T", 'r').read().split("\n")]
        self.TestOutputs = [17]
        self.Input = open("Input1", 'r').read().split("\n")

    def Run(self, arg):
        parsed_args = []
        for i in arg:
            temp = i.split(',')
            parsed_args.append((int(temp[0]), int(temp[1])))
        max_wide = max(parsed_args, key=lambda x: x[0])[0] + 2
        max_deep = max(parsed_args, key=lambda x: x[1])[1] + 2

        matrix = [[0 for x in range( max_wide)] for y in range(max_deep)]

        burned = set()
        for i in range(max_deep):
            for j in range(max_wide):
                mini = 100000
                best_k = -1
                for k in range(len(parsed_args)):
                    point = parsed_args[k]
                    l = abs(i - point[1]) + abs(j-point[0])
                    if l < mini:
                        mini = l
                        best_k = k
                    elif l == mini:
                        best_k = -1 # 2 objects same dist
                matrix[i][j] = best_k
                if i == 0 or j == 0 or i == max_deep-1 or j == max_wide - 1:
                    burned.add(best_k)
        best_size = {}

        for i in range(max_deep):
            for j in range(max_wide):
                if matrix[i][j] not in burned:
                    if matrix[i][j] not in best_size:
                        best_size[matrix[i][j]] = 1
                    else:
                        best_size[matrix[i][j]] += 1
        for i in (matrix):
            print(i)
        return max(best_size.values()) + 1

obj = Day6Challange1()
obj.Test()
#obj.Solve()