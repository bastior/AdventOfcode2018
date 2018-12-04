import ChallengeIf
import datetime
import operator

class Day4Challange2(ChallengeIf.ChallengeIf):
    def __init__(self):
        self.TestInputs = [open("InputT", 'r').read().split("\n")]
        self.TestOutputs = [4455]
        self.Input = open("Input1", 'r').read().split("\n")

    def Run(self, arg):
        formated_lines = []
        # sort by time
        for line in arg:
            split = line.split("]")
            date = datetime.datetime.strptime(split[0][1:], "%Y-%m-%d %H:%M")
            formated_lines.append((date, split[1][1:]))
        formated_lines.sort(key=lambda x: x[0])

        # process data
        guards = {}
        guards_time = {}
        falled_sleep = -1
        guard_no = -1
        for line in formated_lines:
            if "Guard" in line[1]:
                guard_no = line[1].split()[1][1:]
                if guard_no not in guards:
                    guards[guard_no] = []
                    guards_time[guard_no] = 0
            if "falls" in line[1]:
                falled_sleep = int(line[0].strftime("%M"))
                guards[guard_no].append(falled_sleep)
            if "wakes" in line[1]:
                waken_up = int(line[0].strftime("%M"))
                guards[guard_no].append(waken_up)
                guards_time[guard_no] += (waken_up - falled_sleep)
        guard_mins = {}
        for k in guards:
            guard_mins[k] = [0] * 60
            l = guards[k]
            for i in range(len(l))[0::2]:
                for j in range(l[i], l[i+1]):
                    guard_mins[k][j] += 1
        guard_max_mins = {}
        for guard in guard_mins:
            guard_max_mins[guard] = max(guard_mins[guard])

        max_guard = max(guard_max_mins.items(), key=operator.itemgetter(1))[0]
        best_minute = guard_mins[max_guard].index(guard_max_mins[max_guard])
        return (int(max_guard)*int(best_minute))

obj = Day4Challange2()
obj.Test()
obj.Solve()