def binary_to_decimal(user_input):

    user_input = str(user_input)

    total = 0.0

    if "." in user_input:

        integer_and_decimal_parts = user_input.split(".")

        i = len(integer_and_decimal_parts[0]) - 1

        for ints in integer_and_decimal_parts[0]:

            total += int(ints) * (2 ** i)
            i -= 1

        j = 1

        for decs in integer_and_decimal_parts[1]:

            total += int(decs) * (2 ** (-j))
            j += 1

    else:

        k = len(user_input) - 1

        for nums in user_input:

            total += int(nums) * (2 ** k)
            k -= 1

    return total


def decimal_to_binary(user_input):

    user_input = int(user_input)

    binary_string = ""

    while user_input != 0:

        remainder = user_input % 2
        binary_string += str(remainder)

        user_input = user_input // 2

    return binary_string[::-1]