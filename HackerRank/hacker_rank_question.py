"""
Hackerrank question: The time in words
https://www.hackerrank.com/challenges/the-time-in-words/problem
"""
import os
# Complete the timeInWords function below.


def timeInWords(h, m):
    time = ""
    dt = {
        1: "one",
        2: "two",
        3: "three ",
        4: "four ",
        5: "five ",
        6: "six ",
        7: "seven ",
        8: "eight ",
        9: "nine ",
        10: "ten ",
        11: "eleven ",
        12: "twelve ",
        13: "thirteen ",
        14: "fourteen ",
        15: "quarter ",
        16: "sixteen ",
        17: "seventeen ",
        18: "eighteen ",
        19: "ninteen ",
        20: "twenty ",
        21: "twenty one ",
        22: "twenty two ",
        23: "twenty three ",
        24: "twenty four ",
        25: "twenty five ",
        26: "twenty six ",
        27: "twenty seven ",
        28: "twenty eight ",
        29: "twenty nine ",
        30: "half ",
    }
    if m == 0:
        time = dt[h] + "o' clock "
    elif m <= 30:
        time = dt[m] + "past" + dt[h]
    elif m > 30:
        time = dt[m - 30] + "to" + dt[h + 1]
    return time


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    h = int(input())
    m = int(input())
    result = timeInWords(h, m)
    fptr.write(result + "\n")
    fptr.close()
