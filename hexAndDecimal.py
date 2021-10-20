def hex_to_decimal(user_input):

    user_input = str(user_input)

    total = 0.0

    hex_dict = {

        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15

    }

    i = len(user_input) - 1

    for digit in user_input:

        if digit in hex_dict.keys():

            total += hex_dict[digit] * (16 ** i)

        else:

            total += int(digit) * (16 ** i)

        i -= 1

    return total


def decimal_to_hex(user_input):

    user_input = int(user_input)

    hex_string = ""

    hex_dict = {

        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"

    }

    while user_input != 0:

        remainder = user_input % 16

        if remainder in hex_dict.keys():

            hex_string += hex_dict[remainder]

        else:

            hex_string += str(remainder)

        user_input = user_input // 16

    return "0x" + hex_string[::-1]