import operator


class Polynomial(object):
    def __init__(self, coefs):
        if not isinstance(coefs, list):
            raise Exception("coefs must be list")
        if len(coefs) == 0:
            raise Exception("coefs list must not be empty")
        for coef in coefs:
            if not isinstance(coef, int) and not isinstance(coef, float):
                raise Exception("coefs list should contain values of only int or float types")
        for i, coef in enumerate(coefs):
            if coef != 0:
                self.degree = len(coefs) - i - 1
                break
            else:
                self.degree = 1
        self.coefs = coefs.copy()

    def __add__(self, other):
        if isinstance(other, Polynomial):
            if self.degree > other.degree:
                a1 = self.coefs
                a2 = [0] * (self.degree - other.degree) + other.coefs
            elif other.degree > self.degree:
                a1 = [0] * (other.degree - self.degree) + self.coefs
                a2 = other.coefs
            else:
                a1 = self.coefs
                a2 = other.coefs
            return Polynomial(list(map(operator.add, a1, a2)))
        else:
            result = Polynomial(self.coefs)
            result.coefs[-1] += other
            return result

    def __eq__(self, other):
        return self.coefs == other.coefs

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            result = Polynomial([0] * (self.degree + other.degree + 1))
            for i, self_coef in enumerate(self.coefs):
                for j, other_coef in enumerate(other.coefs):
                    result.coefs[i + j] = result.coefs[i + j] + self_coef * other_coef
            return result
        elif isinstance(other, int) or isinstance(other, float):
            result = Polynomial([coef * other for coef in self.coefs])
            return result
        else:
            raise Exception("a polynomial can only be multiplied by a polynomial and int or float constant")

    def __str__(self):
        result = ""
        for i, coef in enumerate(self.coefs):
            if coef != 0:
                if coef > 0:
                    if self.degree == 0:
                        result += str(coef)
                    else:
                        if i == len(self.coefs) - 1:
                            result += "+" + str(coef)
                        else:
                            if i == len(self.coefs) - 2:
                                if coef == 1:
                                    result += "+x"
                                else:
                                    result += "+" + str(coef) + "x"
                            else:
                                if coef == 1:
                                    result += "+x" + str(len(self.coefs) - i - 1)
                                else:
                                    result += "+" + str(coef) + "x" + str(len(self.coefs) - i - 1)
                else:
                    if self.degree == 0:
                        result += str(coef)
                    else:
                        if i == len(self.coefs) - 1:
                            result += str(coef)
                        else:
                            if i == len(self.coefs) - 2:
                                if coef == -1:
                                    result += "-x"
                                else:
                                    result += str(coef) + "x"
                            else:
                                if coef == -1:
                                    result += "-x" + str(len(self.coefs) - i - 1)
                                else:
                                    result += str(coef) + "x" + str(len(self.coefs) - i - 1)
        if result != "":
            return result if result[0] != '+' else result.replace('+', '', 1)
        else:
            return "0"