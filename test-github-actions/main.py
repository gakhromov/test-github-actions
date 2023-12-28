from tabulate import tabulate 

from strings.addition import add_strings
from numbers.addition import add_integers, add_floats


def main():
    a, b = map(float, input("Give two floats: ").split())
    c_str = add_strings(str(a), str(b))
    c_int = add_integers(int(a), int(b))
    c_flt = add_floats(a, b)

    print(tabulate([
        ["As string", c_str],
        ["As integer", c_int],
        ["As float", c_flt],
    ], tablefmt="outline"))


if __name__ == "__main__":
    main()

