# def even_or_odd(n):
#     if n % 2 == 0:
#         print("even")
#         return
#     print("odd")
#
#
# w = even_or_odd(31)
#
# w is None
#


# calculate ordinal suffixes
def nth_root(radicand, n):
    return radicand ** (1 / n)


# st suffix for 1, nd for 2, rd for 3
def ordinal_suffix(value):
    s = str(value)
    if s.endswith('11'):
        return 'th'
    elif s.endswith('12'):
        return 'th'
    elif s.endswith('13'):
        return 'th'
    elif s.endswith('1'):
        return 'st'
    elif s.endswith('2'):
        return 'nd'
    elif s.endswith('3'):
        return 'rd'
    return 'th'


# define ordinal() / decomposition
def ordinal(value):
    return str(value) + ordinal_suffix(value)


# display function
def display_nth_root(radicand, n):
    root = nth_root(radicand, n)
    message = "The " + ordinal(n) + " root of " + str(radicand) + " is " + str(root)
    print(message)
