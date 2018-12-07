import ChallengeIf

class Day7Challange1(ChallengeIf.ChallengeIf):
    def __init__(self):
        self.TestInputs = [open("Input1T", 'r').read().split("\n")]
        self.TestOutputs = ["CABDFE"]
        self.Input = open("Input1", 'r').read().split("\n")

    def Run(self, arg):
        arg_parsed = [(x.split()[1], x.split()[7]) for x in arg]
        letters = set()
        for a, b in arg_parsed:
            letters.add(a)
            letters.add(b)
        deps = {}
        for letter in letters:
            deps[letter] = []
        for a,b in arg_parsed:
            deps[b].append(a)
        ready_list = []
        done_list = []
        time_elapsed = 0
        everything_done = False
        free_workers = 5
        busy_workers = {}

        while not everything_done:
            for key in deps:
                if not deps[key]:
                    if key not in ready_list:
                        ready_list.append(key)
            ready_list.sort()

            while ready_list and free_workers > 0:
                free_workers -= 1
                l = ready_list.pop(0)
                deps.pop(l)
                busy_workers[l] = ord(l) - 4

            time_elapsed += 1
            to_rem = []
            for key in busy_workers:
                busy_workers[key] -= 1
                if busy_workers[key] == 0:
                    to_rem.append(key)
                    free_workers += 1
                    for key1 in deps:
                        if key in deps[key1]:
                            deps[key1].remove(key)
            for i in to_rem:
                busy_workers.pop(i)
            if not busy_workers and not deps:
                return time_elapsed


obj = Day7Challange1()
#obj.Test()
obj.Solve()