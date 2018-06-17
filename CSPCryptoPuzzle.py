from constraint import *

class CSPCryptoPuzzle:
    def __init__(self):
        self.problem = Problem()

    def start(self):
        self.problem.addVariable("T", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.problem.addVariable("W", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.problem.addVariable("O", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.problem.addVariable("F", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.problem.addVariable("U", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.problem.addVariable("R", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.problem.addConstraint(AllDifferentConstraint(), ["T", "W", "O", "F", "U", "R"], )
        self.problem.addVariable("C10", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.problem.addVariable("C100", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.problem.addVariable("C1000", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.problem.addConstraint(lambda O, R, C10: O + O == R + 10*C10, ("O", "R", "C10"))
        self.problem.addConstraint(lambda C10, W, C100, U: C10 + W + W == U + 10*C100, ("C10", "W", "C100", "U"))
        self.problem.addConstraint(lambda C100, T, C1000, O: C100 + T + T == O + 10*C1000, ("C100", "T", "C1000", "O"))
        self.problem.addConstraint(lambda F, C1000: C1000 == F, ("F", "C1000"))
        self.problem.addConstraint(lambda T: T != 0, "T")
        self.problem.addConstraint(lambda F: F != 0, "F")
        print(self.problem.getSolution())

cscPuzzle = CSPCryptoPuzzle()
cscPuzzle.start()