import json
from fractions import Fraction
from math import comb, factorial, floor, gcd, lcm, prod


def floor_function(value):
    return floor(15 * value) + floor(2 * value) - floor(10 * value) - floor(6 * value) - floor(value)


def separated(number):
    positions = [index for index in range(number.bit_length()) if number & (1 << index)]
    return all(upper - lower >= 4 for lower, upper in zip(positions, positions[1:]))


def binary_valuation(number):
    return (10 * number).bit_count() + (6 * number).bit_count() - (15 * number).bit_count()


def exact_value(number):
    numerator = factorial(15 * number) * factorial(2 * number)
    denominator = factorial(10 * number) * factorial(6 * number) * factorial(number)
    quotient, remainder = divmod(numerator, denominator)
    assert remainder == 0
    return quotient


def polynomial(roots):
    coefficients = [Fraction(1)]
    for root in roots:
        updated = [Fraction(0)] * (len(coefficients) + 1)
        for degree, coefficient in enumerate(coefficients):
            updated[degree] += coefficient * root
            updated[degree + 1] += coefficient
        coefficients = updated
    return coefficients


def sibling_floor(value):
    return floor(12 * value) + floor(value) - floor(6 * value) - floor(4 * value) - floor(3 * value)


def sibling_value(number):
    numerator = factorial(12 * number) * factorial(number)
    denominator = factorial(6 * number) * factorial(4 * number) * factorial(3 * number)
    quotient, remainder = divmod(numerator, denominator)
    assert remainder == 0
    return quotient


def digit_sum(number, base):
    total = 0
    while number:
        number, remainder = divmod(number, base)
        total += remainder
    return total


def valuation(number, prime):
    assert number != 0
    number = abs(number)
    exponent = 0
    while number % prime == 0:
        number //= prime
        exponent += 1
    return exponent


def integer_log(number, base):
    exponent = 0
    while number >= base:
        number //= base
        exponent += 1
    return exponent


def sibling_checks():
    triples = [(1, 14, 15), (3, 9, 10), (3, 13, 14), (5, 9, 12),
               (5, 11, 14), (6, 11, 13), (7, 9, 14), (7, 10, 13),
               (7, 11, 12), (12, 21, 25), (12, 37, 41)]
    sparse_indices = [number for number in range(1 << 16) if separated(number)]
    for number in sparse_indices:
        for first, second, third in triples:
            assert (first * number) ^ (second * number) == third * number
        for first in range(16):
            for second in range(16):
                assert (first * number) ^ (second * number) == (first ^ second) * number
                assert (first * number) & (second * number) == (first & second) * number
                assert (first * number) | (second * number) == (first | second) * number
        for shift in [4, 5]:
            common = number + (number << shift)
            assert common & (12 * number) == 0
    counts = [sum(number < (1 << width) for number in sparse_indices) for width in range(17)]
    for ordinal, number in enumerate(sparse_indices[1:], start=1):
        exponent = max(width for width, count in enumerate(counts) if count <= ordinal)
        assert number == (1 << exponent) + sparse_indices[ordinal - counts[exponent]]
    grid = [0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1]
    for index, expected in enumerate(grid):
        assert sibling_floor(Fraction(index, 12)) == expected
        assert sibling_floor(Fraction(2 * index + 1, 24)) == expected
    discontinuities = {Fraction(index, multiplier) for multiplier in [12, 1, 6, 4, 3]
                       for index in range(multiplier + 1)}
    assert all((12 * point).denominator == 1 for point in discontinuities)
    for target in [Fraction(1, 3), Fraction(1, 2), Fraction(2, 3), Fraction(1)]:
        assert grid[int(12 * target) - 1] == 1
    assert all(grid[index] == 1 for index in [1, 5, 7, 11])
    for modulus in range(5, 4097):
        if gcd(modulus, 6) != 1:
            continue
        for multiplier in [1, 2, 3]:
            for quotient in range(1, multiplier + 1):
                if (quotient * modulus - 1) % multiplier:
                    continue
                residue = (quotient * modulus - 1) // multiplier
                expected = 0 if ((multiplier == 1 and modulus in [5, 7, 11]) or
                                 (multiplier == 2 and modulus == 5)) else 1
                assert sibling_floor(Fraction(residue, modulus)) == expected
        quotient = next(candidate for candidate in [1, 5, 7, 11]
                        if (candidate * modulus + 1) % 12 == 0)
        assert sibling_floor(Fraction(quotient * modulus + 1, 12 * modulus)) == 1
    least_common = [1]
    for index in range(1, 385):
        least_common.append(lcm(least_common[-1], index))
    values = [sibling_value(number) for number in range(257)]
    for number, value in enumerate(values):
        assert (385 * value) % (number + 1) == 0
        assert (5 * value) % (2 * number + 1) == 0
        assert value % (3 * number + 1) == 0
        assert (770 * value) % ((number + 1) * (2 * number + 1) * (3 * number + 1)) == 0
        assert value % (12 * number - 1) == 0
        assert valuation(value, 2) == (3 * number).bit_count()
        assert 2 * valuation(value, 3) == digit_sum(2 * number, 3)
        assert Fraction(comb(12 * number, 6 * number) * comb(6 * number, 2 * number),
                        comb(3 * number, number)) == value
        assert Fraction(comb(12 * number, 6 * number) * comb(7 * number, 3 * number),
                        comb(7 * number, number)) == value
        for width in range(1, 33):
            constant = 36 * factorial(width - 1) * least_common[12 * width]
            for multiplier in [1, 2, 3]:
                denominator = prod(multiplier * number + index for index in range(1, width + 1))
                assert (constant * value) % denominator == 0
            denominator = prod(12 * number - index for index in range(1, width + 1)
                               if gcd(index, 12) == 1)
            constant = factorial(width - 1) * least_common[width]
            assert (constant * value) % denominator == 0
    for number in range(1, 257):
        numerator = 24 * prod(12 * number - offset for offset in [11, 1, 5, 7])
        denominator = number * (3 * number - 1) * (2 * number - 1) * (3 * number - 2)
        assert Fraction(values[number], values[number - 1]) == Fraction(numerator, denominator)
        assert Fraction(numerator, denominator) == Fraction(27648) * prod(
            number - 1 + Fraction(index, 12) for index in [1, 5, 7, 11]) / prod(
            number - 1 + root for root in [Fraction(1, 3), Fraction(1, 2), Fraction(2, 3), Fraction(1)])
    stress_count = 0
    for prime in [2, 3]:
        for exponent in range(1, 97):
            modulus = prime ** exponent
            for multiplier in [1, 2, 3]:
                for index in range(1, 33):
                    common = gcd(multiplier, modulus)
                    if index % common:
                        continue
                    reduced = modulus // common
                    residue = (-index // common * pow(multiplier // common, -1, reduced)) % reduced
                    for number in [residue, residue + modulus, residue + 3 * modulus]:
                        lower = valuation(multiplier * number + index, prime)
                        actual = ((3 * number).bit_count() if prime == 2 else digit_sum(2 * number, 3) // 2)
                        assert actual >= lower - integer_log(12 * index, prime) - 2
                        stress_count += 1
    return {'xor_triples': 11, 'xor_sparse_indices_below_65536': len(sparse_indices),
            'all_bitwise_masks': [0, 15], 'ordered_recursion_indices': [0, len(sparse_indices) - 1],
            'sibling_floor_intervals': 12, 'residue_moduli': [5, 4096],
            'fixed_divisibilities': 5, 'sibling_exact_range': [0, 256],
            'product_family_R_range': [1, 32], 'product_family_k': [1, 2, 3],
            'small_prime_exponent_range': [1, 96], 'small_prime_stress_cases': stress_count,
            'sibling_binomial_and_coefficient_identities': True}


def main():
    floor_values = [0, 0, 1, 0, 1, 0, 0, 0, 1, 0,
                    0, 0, 0, 0, 1, 0, 1, 1, 1, 1,
                    1, 0, 1, 1, 1, 0, 1, 0, 1, 1]
    breakpoints = {Fraction(index, multiplier) for multiplier in [15, 2, 10, 6, 1]
                   for index in range(multiplier + 1)}
    assert all((30 * point).denominator == 1 for point in breakpoints)
    for index, expected in enumerate(floor_values):
        assert floor_function(Fraction(index, 30)) == expected
        assert floor_function(Fraction(2 * index + 1, 60)) == expected
    assert floor_function(Fraction(1)) == 0
    sparse_rows = [[7, 1, 5, 3, 0], [3, 0, 2, 1, 0], [1, 0, 1, 0, 0]]
    bad_rows = [[11, 1, 7, 4, 0], [9, 1, 6, 3, 0], [8, 1, 5, 3, 0]]
    for distance in range(1, 4):
        sparse_lower = Fraction(1, 2 ** distance)
        sparse_upper = Fraction(16, 15 * 2 ** distance)
        bad_lower = Fraction(2 ** distance + 1, 2 ** (distance + 1))
        bad_upper = bad_lower + Fraction(1, 15 * 2 ** (distance + 1))
        for lower, upper, row in [(sparse_lower, sparse_upper, sparse_rows[distance - 1]),
                                  (bad_lower, bad_upper, bad_rows[distance - 1])]:
            for multiplier, expected in zip([15, 2, 10, 6, 1], row):
                assert expected <= multiplier * lower
                assert multiplier * upper <= expected + 1
    divisibility_rows = [(6, 1, 5, [2, 0, 1, 0, 0]),
                         (6, 5, 5, [12, 1, 8, 4, 0]),
                         (10, 1, 3, [1, 0, 0, 0, 0]),
                         (10, 3, 3, [4, 0, 2, 1, 0]),
                         (10, 7, 3, [10, 1, 6, 4, 0]),
                         (10, 9, 3, [13, 1, 8, 5, 0])]
    for multiplier_base, residue, minimum, row in divisibility_rows:
        lower_endpoint = Fraction(residue, multiplier_base) - Fraction(1, multiplier_base * minimum)
        upper_endpoint = Fraction(residue, multiplier_base)
        for multiplier, expected in zip([15, 2, 10, 6, 1], row):
            assert expected <= multiplier * lower_endpoint
            assert multiplier * upper_endpoint <= expected + 1
    for number in range(1 << 16):
        valuation = binary_valuation(number)
        assert valuation >= 0
        assert (valuation == 0) == separated(number)
        if number < (1 << 12):
            divisor = 2
            floor_sum = 0
            while divisor <= 15 * number:
                floor_sum += floor_function(Fraction(number, divisor))
                divisor *= 2
            assert floor_sum == valuation
    values = []
    for number in range(257):
        value = exact_value(number)
        assert value % 2 == int(separated(number))
        product_divisor = (6 * number + 1) * (10 * number + 1)
        assert value % product_divisor == 0
        assert gcd(6 * number + 1, 10 * number + 1) == 1
        assert (value // product_divisor) % 2 == value % 2
        assert Fraction(comb(15 * number, 5 * number) * comb(2 * number, number), comb(6 * number, number)) == value
        assert Fraction(comb(15 * number, 5 * number) * comb(7 * number, number), comb(7 * number, 2 * number)) == value
        values.append(value)
    counts = [sum(separated(number) for number in range(1 << width)) for width in range(17)]
    assert counts[:4] == [1, 2, 3, 4]
    assert all(counts[width] == counts[width - 1] + counts[width - 4] for width in range(4, 17))
    numerator_roots = [Fraction(index, multiplier) for multiplier in [15, 2] for index in range(1, multiplier + 1)]
    denominator_roots = [Fraction(index, multiplier) for multiplier in [10, 6, 1] for index in range(1, multiplier + 1)]
    for root in numerator_roots[:]:
        if root in denominator_roots:
            numerator_roots.remove(root)
            denominator_roots.remove(root)
    upper = [Fraction(index, 15) for index in [1, 2, 4, 7, 8, 11, 13, 14]]
    lower = [Fraction(1, 10), Fraction(1, 6), Fraction(3, 10), Fraction(1, 2),
             Fraction(7, 10), Fraction(5, 6), Fraction(9, 10), Fraction(1)]
    assert polynomial(numerator_roots) == polynomial(upper)
    assert polynomial(denominator_roots) == polynomial(lower)
    constant = Fraction(15 ** 15 * 2 ** 2, 10 ** 10 * 6 ** 6)
    assert constant == Fraction(61509375, 16384)
    for number in range(256):
        ratio = constant * prod(number + root for root in upper) / prod(number + root for root in lower)
        assert Fraction(values[number + 1], values[number]) == ratio
    result = {
        'status': 'pass',
        'floor_intervals': 30,
        'binary_valuation_range': [0, 65535],
        'floor_sum_range': [0, 4095],
        'exact_factorial_and_product_divisibility_range': [0, 256],
        'hypergeometric_ratio_range': [0, 255],
        'hypergeometric_polynomial_identity': True,
        'binary_floor_rows_rational_bounds': 6,
        'divisibility_floor_rows_rational_bounds': 6,
        'counting_widths': [0, 16],
        'counts': counts,
        'initial_terms': values[:12],
        'sibling_checks': sibling_checks(),
        'coverage': 'Exact finite checks and polynomial identities; the all-input argument is in note.tex.'
    }
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
