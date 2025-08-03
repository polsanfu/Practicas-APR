class Operacion:
    def __init__(self, num1, num2, op):
        self.num1 = float(num1)
        self.num2 = float(num2)
        self.op = str(op)
        self.res = float()
    def set_res(self, res):
        pass
    def mostrar_res(self):
        return str(self.num1) + self.op + str(self.num2) + "=" + str(self.res)
    def __str__(self):
        return self.mostrar_res()

class Suma(Operacion):
    def __init__(self, num1, num2):
        Operacion.__init__(self, num1, num2, "+")
        Operacion.set_res(self, self.res)
        self.res = self.num1 + self.num2
class Resta(Operacion):
    def __init__(self, num1, num2):
        Operacion.__init__(self, num1, num2, "-")
        Operacion.set_res(self, self.res)
        self.res = self.num1 - self.num2
class Multiplicacion(Operacion):
    def __init__(self, num1, num2):
        Operacion.__init__(self, num1, num2, "*")
        Operacion.set_res(self, self.res)
        self.res = self.num1 * self.num2
class Division(Operacion):
    def __init__(self, num1, num2):
        Operacion.__init__(self, num1, num2, "/")
        Operacion.set_res(self, self.res)
        self.res = self.num1 / self.num2
