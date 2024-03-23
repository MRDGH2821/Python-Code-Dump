"""Armstrong number determiner."""


def armstrong(x: int) -> str:
    """Return whether a number is Armstrong or not."""
    summed_up = 0
    t = x
    while t > 0:
        d = t % 10
        summed_up += d**3
        t = t // 10
        if summed_up == x:
            return "Armstrong"

    return "not Armstrong"


x = int(input())
print(armstrong(x))
