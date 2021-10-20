from binaryAndDecimal import binary_to_decimal, decimal_to_binary
from hexAndDecimal import decimal_to_hex, hex_to_decimal

def binary_to_hex(usr_input):

    in_dec_form = binary_to_decimal(usr_input)

    return decimal_to_hex(in_dec_form)


def hex_to_binary(usr_input):

    in_dec_form = hex_to_decimal(usr_input)

    return decimal_to_binary(in_dec_form)