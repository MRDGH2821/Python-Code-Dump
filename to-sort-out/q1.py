def base10toN(num: "int", base: "int"):
    """Change `num` to given base.
    Upto base 36 is supported."""

    converted_string = ""
    current_num = num
    if not 1 < base < 37:
        raise ValueError("base must be between 2 and 36")
    if not num:
        return '0'
    while current_num:
        mod = current_num % base
        current_num = current_num // base
        converted_string = chr(48 + mod + 7 * (mod > 10)) + converted_string
    return converted_string


number = int(input("Enter number:"))
base = int(input("Enter base:"))

print(base10toN(number, base))
