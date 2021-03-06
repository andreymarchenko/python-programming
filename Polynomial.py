import operator


class Polynomial(object):
    def __init__(self, coeffs):
        if not isinstance(coeffs, list):
            raise TypeError("coeffs must be list or constant")
        if len(coeffs) == 0:
            raise TypeError("coeffs list must not be empty")
        if not all(isinstance(c, (int, float)) for c in coeffs):
            raise TypeError("coeffs list should contain values of only int or float types")
        senior_degree = next((i for i, c in enumerate(coeffs) if c != 0), -1)
        self.coeffs = coeffs[senior_degree:]

    @property
    def degree(self):
        return len(self.coeffs) - 1

    def __radd__(self, other):
        return self + other

    def __add__(self, other):
        if isinstance(other, Polynomial):
            if self.degree > other.degree:
                a1 = self.coeffs
                a2 = [0] * (self.degree - other.degree) + other.coeffs
            elif other.degree > self.degree:
                a1 = [0] * (other.degree - self.degree) + self.coeffs
                a2 = other.coeffs
            else:
                a1 = self.coeffs
                a2 = other.coeffs
            return Polynomial(list(map(operator.add, a1, a2)))
        elif isinstance(other, (int, float)):
            result = Polynomial(self.coeffs)
            result.coeffs[-1] += other
            return result
        else:
            raise TypeError("only int or float constant can be added to the polynomial")

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            if len(self.coeffs) == 1:
                return self.coeffs[0] == other
            else:
                return False
        elif isinstance(other, Polynomial):
            return self.coeffs == other.coeffs
        else:
            raise TypeError("a polynomial can only be compared to a polynomial or constant")

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            result = [0] * (self.degree + other.degree + 1)
            for i, self_coef in enumerate(self.coeffs):
                for j, other_coef in enumerate(other.coeffs):
                    result[i + j] += self_coef * other_coef
            return Polynomial(result)
        elif isinstance(other, (int, float)):
            result = Polynomial([coef * other for coef in self.coeffs])
            return result
        else:
            raise TypeError("a polynomial can only be multiplied by a polynomial and int or float constant")

    def __rmul__(self, other):
        return self * other

    def __str__(self):
        result = ""
        for i, coef in enumerate(self.coeffs):
            if coef != 0:
                if self.degree == 0:
                    result += str(coef)
                elif i == self.degree:
                    result += "{:+}".format(coef)
                elif i == self.degree - 1:
                    if abs(coef) == 1:
                        result += "+x" if coef > 0 else "-x"
                    else:
                        result += "{:+}x".format(coef)
                else:
                    if abs(coef) == 1:
                        result += ("+x" if coef > 0 else "-x") + str(self.degree - i)
                    else:
                        result += "{:+}x{}".format(coef, str(self.degree - i))
        return result.lstrip("+") if result else "0"