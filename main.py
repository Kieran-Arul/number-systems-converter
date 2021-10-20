from binaryAndDecimal import binary_to_decimal, decimal_to_binary
from binaryAndHex import binary_to_hex, hex_to_binary
from hexAndDecimal import hex_to_decimal, decimal_to_hex

print("Welcome to the dec, bin, hex converter!")

finished = False

while not finished:

    valid_choice = False

    while not valid_choice:

        print("\nAvailable Number Systems:")
        print("1. Decimal")
        print("2. Binary")
        print("3. Hexadecimal")

        possible_choices = [1, 2, 3]

        src_choice = int(input("\nWhat number system would you like to change from? Enter a number (1/2/3): \n"))

        dest_choice = int(input("\nWhat number system would you like to change to (1/2/3): "))

        if (src_choice not in possible_choices) or (dest_choice not in possible_choices):

            print("Invalid Input")
            continue

        if src_choice == dest_choice:

            print("Invalid Input")
            continue

        if src_choice == 1 and dest_choice == 2:

            dec_num = int(input("Enter your decimal number: "))
            print(decimal_to_binary(dec_num))

        elif src_choice == 2 and dest_choice == 1:

            bin_num = int(input("Enter your binary number: "))
            print(binary_to_decimal(bin_num))

        elif src_choice == 1 and dest_choice == 3:

            dec_num = int(input("Enter your decimal number: "))
            print(decimal_to_hex(dec_num))

        elif src_choice == 3 and dest_choice == 1:

            hex_num = int(input("Enter your hex number: "))
            print(hex_to_decimal(hex_num))

        elif src_choice == 2 and dest_choice == 3:

            bin_num = int(input("Enter your binary number: "))
            print(binary_to_hex(bin_num))

        elif src_choice == 3 and dest_choice == 2:

            hex_num = int(input("Enter your hex number: "))
            print(hex_to_binary(hex_num))

        valid_choice = True

        go_again = input("Do you want to use the converter again (y/n): ")

        if go_again == "y":

            continue

        else:

            finished = True
            print("Thank you for using the converter")
