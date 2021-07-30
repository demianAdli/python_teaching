def dec_to_bin(number):
    binary = []
    while number != 0:
        binary.append(number % 2)
        number //= 2
    binary.reverse()
    return '0b' + ''.join(str(each) for each in binary)


print(dec_to_bin(2345))
print(bin(2345))