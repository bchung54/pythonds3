# LogicGate class from PythonDS 1.13

class LogicGate:
    
    def __init__(self,lbl):
        self.name = lbl
        self.output = None

    def getLabel(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self,lbl):
        super().__init__(lbl)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getLabel()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+self.getLabel()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):

    def __init__(self,lbl):
        super().__init__(lbl)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):

    def __init__(self,lbl):
        super().__init__(lbl)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b==1:
            return 1
        else:
            return 0


class UnaryGate(LogicGate):

    def __init__(self,lbl):
        super().__init__(lbl)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getLabel()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):

    def __init__(self,lbl):
        super().__init__(lbl)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1


class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


#Programming Exercises 1.17.10
class NandGate(AndGate):

    def __init__(self, lbl):
        super().__init__(lbl)
    
    def performGateLogic(self):
        if self.performGateLogic() == 0:
            return 1
        else:
            return 0


#Programming Exercises 1.17.10
class NorGate(OrGate):

    def __init__(self, lbl):
        super().__init__(lbl)

    def performGateLogic(self):
        if self.performGateLogic() == 0:
            return 1
        else:
            return 0


#Programming Exercises 1.17.10
class XorGate(BinaryGate):

    def __init__(self, lbl):
        super().__init__(lbl)
    
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a != b:
            return 1
        else:
            return 0

#Programming Exercises 1.17.11
def half_adder():
    g_xor = XorGate("half_adder_xor")
    g_and = AndGate("half_adder_and")
    return g_and.getOutput(), g_xor.getOutput()

if __name__ == '__main__':
    print(half_adder())