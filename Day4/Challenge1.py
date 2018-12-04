import ChallengeIf
import datetime
import operator

class Day4Challange1(ChallengeIf.ChallengeIf):
    def __init__(self):
        self.TestInputs = [open("InputT", 'r').read().split("\n")]
        self.TestOutputs = [240]
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
        max_guard = max(guards_time.items(), key=operator.itemgetter(1))[0]
        l = guards[max_guard]
        mins = [0] * 60
        for i in range(len(l))[0::2]:
            for j in range(l[i], l[i+1]):
                mins[j] += 1
        max_min = mins.index(max(mins))
        return int(max_guard)*int(max_min)

obj = Day4Challange1()
#obj.Test()
obj.Solve()