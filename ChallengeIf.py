from abc import abstractmethod

class ChallengeIf():
    TestInputs = []
    TestOutputs = []
    Input = None

    def __init__(self):
        pass

    @abstractmethod
    def Run(self, arg):
        pass

    def Solve(self):
        print(self.Run(self.Input))

    def Test(self):
        assert (len(self.TestInputs) == len(self.TestOutputs))
        for tc, res in zip(self.TestInputs, self.TestOutputs):
            assert (self.Run(tc) == res)
