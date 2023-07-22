from math import gcd


def gcd_strings(str1, str2):
    if str1 + str2 == str2 + str1:
        str = str1 + str2
        return str[: gcd(len(str1), len(str2))]
    return ""


str1 = "xyz"
str2 = "xyzxyz"
