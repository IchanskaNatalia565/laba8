from math import gcd


class Rational:
    def __init__(self, n, d=None):
        if d is None:
            # Якщо один аргумент і це рядок 'n/d'
            if isinstance(n, str):
                parts = n.split('/')
                if len(parts) != 2:
                    raise ValueError("Неправильний формат дробу")
                self.n = int(parts[0])
                self.d = int(parts[1])
            else:
                raise ValueError("Неправильний тип аргументів")
        else:
            # Якщо два аргументи
            self.n = int(n)
            self.d = int(d)

        if self.d == 0:
            raise ZeroDivisionError("Знаменник не може бути 0")
        self._reduce()

    def _reduce(self):
        # Скорочуємо дріб
        g = gcd(self.n, self.d)
        self.n //= g
        self.d //= g
        # Знаменник завжди позитивний
        if self.d < 0:
            self.n = -self.n
            self.d = -self.d

    def __add__(self, other):
        if isinstance(other, Rational):
            n = self.n * other.d + other.n * self.d
            d = self.d * other.d
            return Rational(n, d)
        elif isinstance(other, int):
            return Rational(self.n + other * self.d, self.d)
        else:
            raise TypeError("Підтримуються лише Rational або int")

    def __sub__(self, other):
        if isinstance(other, Rational):
            n = self.n * other.d - other.n * self.d
            d = self.d * other.d
            return Rational(n, d)
        elif isinstance(other, int):
            return Rational(self.n - other * self.d, self.d)
        else:
            raise TypeError("Підтримуються лише Rational або int")

    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(self.n * other.n, self.d * other.d)
        elif isinstance(other, int):
            return Rational(self.n * other, self.d)
        else:
            raise TypeError("Підтримуються лише Rational або int")

    def __truediv__(self, other):
        if isinstance(other, Rational):
            if other.n == 0:
                raise ZeroDivisionError("Ділення на нуль")
            return Rational(self.n * other.d, self.d * other.n)
        elif isinstance(other, int):
            if other == 0:
                raise ZeroDivisionError("Ділення на нуль")
            return Rational(self.n, self.d * other)
        else:
            raise TypeError("Підтримуються лише Rational або int")

    def __call__(self):
        # Повертає десятковий дріб
        return self.n / self.d

    def __getitem__(self, key):
        if key == 'n':
            return self.n
        elif key == 'd':
            return self.d
        else:
            raise KeyError("Ключ має бути 'n' або 'd'")

    def __setitem__(self, key, value):
        if key == 'n':
            self.n = int(value)
            self._reduce()
        elif key == 'd':
            if value == 0:
                raise ZeroDivisionError("Знаменник не може бути 0")
            self.d = int(value)
            self._reduce()
        else:
            raise KeyError("Ключ має бути 'n' або 'd'")

    def __str__(self):
        return f"{self.n}/{self.d}"
