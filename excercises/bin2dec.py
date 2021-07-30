def bin_to_dec(binary):
    """Input binary number as a string"""
    binary = binary[::-1]
    result = 0
    count = 0
    for number in binary:
        result += int(number) * 2 ** count
        count += 1
    return result


print(bin_to_dec("100100101001"))