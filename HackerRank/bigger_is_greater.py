"""
Hacker rank problem: Bigger is Greater
https://www.hackerrank.com/challenges/bigger-is-greater/problem
"""
# from copy import deepcopy as dpcpy
import os
# Complete the biggerIsGreater function below.


def biggerIsGreater(w: str):
    newWrd = list(w[::-1])
    i = len(newWrd) - 2
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
        newWrd[i], newWrd[i + 1] = newWrd[i + 1], newWrd[i]
        new = "".join(newWrd[::-1])
        if new > w:
            return new
        else:
            i = i - 1
    else:
        return "no answer"


"""
    if flag==1:
        return "no answer"
"""
if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    T = int(input())
    for T_itr in range(T):
        w = input()
        result = biggerIsGreater(w)
        fptr.write(result + "\n")
    fptr.close()
