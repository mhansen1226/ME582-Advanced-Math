from math import factorial

from sympy import Symbol


def a(n: complex) -> complex:
    return -(n + 1) / 4 * (1j / 2) ** n


z0 = 1j
z = Symbol("z", complex=True)
n = Symbol("n", positive=True)
f = 1 / (z + 1j) ** 2
for n in range(10):
    fz0 = f.subs(z, z0)
    an = fz0 / factorial(n)
    # print(f"f^({n}) (z) = {f}")
    # print(f"f^({n}) (z0) = {fz0}")
    print(f"a_{n} = {an} = {a(n)}")
    print()
    f = f.diff()
