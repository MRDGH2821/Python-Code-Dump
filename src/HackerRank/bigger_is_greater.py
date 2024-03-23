"""HackerRank problem: Bigger is Greater.

https://www.hackerrank.com/challenges/bigger-is-greater/problem
"""

# from copy import deepcopy as dpcpy
import os

# Complete the biggerIsGreater function below.


def biggerIsGreater(w: str):  # noqa: N802
    """Return the next lexicographically greater word."""
    new_word = list(w[::-1])
    i = len(new_word) - 2
    new = ""
    """
    for i in range(len(newWrd)-1):
        if newWrd[i]==newWrd[i+1]:
            continue
        elif newWrd[i]>newWrd[i+1]:
            newWrd[i],newWrd[i+1]=newWrd[i+1],newWrd[i]
            break
        new="".join(newWrd[::-1])
        if new>w:
            break
            return new
        else:
            flag=1
    """
    while i > -1:
        new_word[i], new_word[i + 1] = new_word[i + 1], new_word[i]
        new = "".join(new_word[::-1])
        if new > w:
            return new
        else:
            i = i - 1
    return "no answer"


"""
    if flag==1:
        return "no answer"
"""
if __name__ == "__main__":
    file = open(os.environ["OUTPUT_PATH"], "w")  # noqa: PTH123, SIM115
    T = int(input())
    for _ in range(T):
        w = input()
        result = biggerIsGreater(w)
        file.write(result + "\n")
    file.close()
