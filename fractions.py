from fractions import Fraction

class Rational:
    def __init__(self, n, d=1):
        if isinstance(n, str):
            n, d = n.split('/')
            n, d = int(n), int(d)
        else:
            n, d = int(n), int(d)
        if d == 0:
            raise ValueError("Знаменник не може бути 0")
        g = self.gcd(abs(n), abs(d))
        self.n = n // g
        self.d = d // g
        if self.d < 0:
            self.n = -self.n
            self.d = -self.d

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        return Rational(self.n * other.n, self.d * other.d)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        n = self.n * other.d - other.n * self.d
        d = self.d * other.d
        return Rational(n, d)

    def __str__(self):
        return f"{self.n}/{self.d}"

def main():
    with open('input01.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            tokens = line.replace('*', ' * ').replace('-', ' - ').split()
            result = Rational(tokens[0])
            i = 1
            while i < len(tokens):
                op = tokens[i]
                val = tokens[i + 1]
                r_val = Rational(val)
                if op == '*':
                    result = result * r_val
                elif op == '-':
                    result = result - r_val
                else:
                    print(f"Невідома операція {op}")
                i += 2
            print(f"Результат для рядка: {line} -> {result}")

if __name__ == '__main__':
    main()
