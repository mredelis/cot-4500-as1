import numpy as np

# 64-bit (binary digit) representation of a real number
# First bit denoted as s is a sign representation followed by
# 11-bit exponent denoted by c is called the characteristic
# 52-bit binary fraction denoted by f called the mantissa

EXPONENT_LENGTH = 11
MANTISSA_LENGTH = 52

# Calculate decimal number using double precision (format to 5 decimal places)
def exercise_1(b_num: str):
    sign: int = 1 if b_num[0] == "0" else -1  # s = 0 the number is +
    exponent: float = 0
    mantissa: float = 0
    decimal_number: float = 0

    for i in range(1, EXPONENT_LENGTH + 1):
        exponent += int(b_num[i]) * (2 ** (11 - i))

    for i in range(EXPONENT_LENGTH + 1, len(b_num)):
        mantissa += int(b_num[i]) * (1 / 2) ** (i - 11)

    decimal_number = sign * (2 ** (exponent - 1023)) * (1 + mantissa)
    return decimal_number


def normalized_form(dec_num: float):
    n: int = 0
    # write number in normalized decimal form
    while dec_num >= 1:
        dec_num = dec_num / 10
        n += 1
    return (dec_num, n)


# Exercise 1 using three-digit chopping arithmetic
def exercise_2(fraction: float, exponent: int, digits_to_chopping: int):
    chopped_value = int(fraction * 10**digits_to_chopping) / 10**digits_to_chopping
    return round(chopped_value * 10**exponent, digits_to_chopping - 1)


# Exercise 1 using three-digit rounding arithmetic
def exercise_3(fraction: float, exponent: int, digits_to_rounding: int):
    # add 5 to the (k+1) digit and then chop after the kth digit
    new_fraction = fraction + 5 / 10 ** (digits_to_rounding + 1)
    return exercise_2(new_fraction, exponent, digits_to_rounding)


# Absolute error with the exact value from question 1 and its 3 digit rounding
def absolute_error(precise: float, approximate: float):
    sub_operation = precise - approximate
    return abs(sub_operation)


# Relative error with the exact value from question 1 and its 3 digit rounding
def relative_error(precise: float, approximate: float):
    sub_operation = absolute_error(precise, approximate)
    div_operation = sub_operation / abs(precise)
    return div_operation


binary_number = "010000000111111010111001"
res1 = exercise_1(binary_number)
print(format(res1, ".5f"), "\n")

(fraction, exponent) = normalized_form(res1)
res2 = exercise_2(fraction, exponent, 3)
res3 = exercise_3(fraction, exponent, 3)
res4_1 = absolute_error(res1, res2)
res4_2 = relative_error(res1, res3)

print(res2, "\n")
print(res3, "\n")
print(res4_1)
print(res4_2, "\n")


# # Check one for series: alternating sequence


# def check_for_alternating(function_a: str):
#     return "-1**k" in function_a

# # Check two for series: decreasing sequence


# def check_for_decreasing(function_a: str, x: int):
#     k = 1
#     previous_val = abs(eval(function_a))
#     for k in range(2, INFINITY):
#         result = abs(eval(function_a))
#         if (previous_val <= result):
#             return False
#         previous_val = result
#     return True

# # Now that those two previous checks are complete, calculate minimum terms


# def task_five(error: int):
#     min_terms = 0
#     while ((min_terms + 1) <= 10**(-1 * error / 3)):
#         min_terms += 1

#     print(min_terms, "\n")

# # Determine number of iterations to solve with bisection method


# def task_six_bisection(function_a: str, error: float, left: int, right: int):
#     x = 0
#     i = 0
#     while (abs(right - left) > error and i < INFINITY):
#         x = (left + right) / 2
#         if eval(function_a) < 0 and eval(function_a) > 0 or eval(function_a) > 0 and eval(function_a) < 0:
#             right = x
#         else:
#             left = x
#         i += 1
#     print(i, "\n")

# # Determine number of iterations to solve with Newton method


# def task_six_newton(function_a: str, function_a_der: str, x: float, error: float):
#     i = 0
#     while i < INFINITY:
#         if eval(function_a_der) != 0:
#             x_next = x - eval(function_a) / eval(function_a_der)
#             if (abs(x_next - x) < error):
#                 print(i)
#                 return
#             x = x_next
#             i += 1
#         else:
#             print("Failure: Derivation is 0")
#     print("Failure: Maximum number of iterations")


# # binary_num = "0100000000111011100100011010000000000000000000000000000000000000"
# binary_num = "010000000111111010111001"

# result: float = task_one(binary_num)
# task_two(result)

# rounded_result: float = task_three(result)

# absolute_error_val = task_four_absolute(result, rounded_result)

# task_four_relative(result, absolute_error_val)

# x: int = 1
# function_a: str = "(-1**k) * (x**k) / (k**3)"
# error: int = -4

# if (check_for_alternating(function_a) and check_for_decreasing(function_a, x)):
#     task_five(error)

# function_a = "x**3 + 4*x**2 - 10"
# error = 10**(-4)

# left: int = 4
# right: int = 7

# task_six_bisection(function_a, error, left, right)

# function_a_der = "3*x**2 + 8*x"

# task_six_newton(function_a, function_a_der, abs(right - left), error)
