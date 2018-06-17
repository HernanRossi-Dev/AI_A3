from constraint import *

class CSPWaltz:
    def __init__(self):
        self.problem = Problem()

    def start(self):
        # Labels are 0 = +/P, 1 = -/M ,  2 = ->/R, 3 = <-/A
        A = 0
        R = 1
        M = 2
        P = 3
        self.problem.addVariable("E1", [A, R, M, P])
        self.problem.addVariable("E2", [A, R, M, P])
        self.problem.addVariable("E3", [A, R, M, P])
        self.problem.addVariable("E4", [A, R, M, P])
        self.problem.addVariable("E5", [A, R, M, P])
        self.problem.addVariable("E6", [A, R, M, P])
        self.problem.addVariable("E7", [A, R, M, P])
        self.problem.addVariable("E8", [A, R, M, P])
        self.problem.addVariable("E9", [A, R, M, P])
        self.problem.addVariable("E10", [A, R, M, P])
        self.problem.addVariable("E11", [A, R, M, P])
        self.problem.addVariable("E12", [A, R, M, P])
        self.problem.addVariable("E13", [A, R, M, P])
        self.problem.addVariable("E14", [A, R, M, P])
        self.problem.addVariable("E15", [A, R, M, P])
        # L Shapes

        #J2
        self.problem.addConstraint(FunctionConstraint(self.LShapeConstraint)
                                   , ("E1", "E2"))
        #J6
        self.problem.addConstraint(FunctionConstraint(self.LShapeConstraint)
                                   , ("E5", "E6"))
        #J8
        self.problem.addConstraint(FunctionConstraint(self.LShapeConstraint)
                                   , ("E7", "E8"))

        # Fork shapes
        # J4
        self.problem.addConstraint(FunctionConstraint(self.ForkConstraint)
                                   , ("E4", "E3", "E14"))
        #J9
        self.problem.addConstraint(FunctionConstraint(self.ForkConstraint)
                                   , ("E9", "E11", "E10"))
        #J11
        self.problem.addConstraint(FunctionConstraint(self.ForkConstraint)
                                   , ("E12", "E13", "E15"))
        # Arrow shapes
        #J1
        self.problem.addConstraint(FunctionConstraint(self.ArrowConstraint)
                                   , ("E8", "E9", "E1"))
        #J3
        self.problem.addConstraint(FunctionConstraint(self.ArrowConstraint)
                                   , ("E2", "E10", "E3"))
        #J5
        self.problem.addConstraint(FunctionConstraint(self.ArrowConstraint)
                                   , ("E4", "E15", "E5"))
        #J7
        self.problem.addConstraint(FunctionConstraint(self.ArrowConstraint)
                                   , ("E6", "E13", "E7"))
        #J10
        self.problem.addConstraint(FunctionConstraint(self.ArrowConstraint)
                                   , ("E12", "E14", "E11"))

        print(self.problem.getSolutions())

    def LShapeConstraint(self, x, y):
        A = 0
        R = 1
        M = 2
        P = 3
        if x == R and y == P:
            return True
        elif x == R and y == R:
            return True
        elif x == P and y == R:
            return True
        elif x == A and y == M:
            return True
        elif x == A and y == A:
            return True
        elif x == M and y == A:
            return True
        else:
            return False

    def ArrowConstraint (self, x, y, z):
        A = 0
        M = 2
        P = 3
        if x == A and y == P and z == A:
            return True
        elif x == M and y == P and z == M:
            return True
        elif x == P and y == M and z == P:
            return True
        else:
            return False

    def ForkConstraint(self, x, y, z):
        A = 0
        M = 2
        P = 3
        if x == A and y == A and z == M:
            return True
        elif x == M and y == A and z == A:
            return True
        elif x == A and y == M and z == A:
            return True
        elif x == P and y == P and z == P:
            return True
        elif x == M and y == M and z == M:
            return True
        else:
            return False


cspWaltz = CSPWaltz()
cspWaltz.start()