hex_digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
              'C': 12, 'D': 13, 'E': 14, 'F': 15}
hex_digits_inverse = {v: k for k, v in hex_digits.items()}  # inverts the hex_digits (used for encoding in option 3)


def main():
    user_selection = prompt_menu()  # ask user to select an option => return the option
    user_number = prompt_number()  # ask user to enter a number => return number
    conversion_result = decode(user_selection, user_number)  # Decodes the number based on the prompt

    print(f"Result: {conversion_result}\n")  # prints result & adds new line for next run
    main()  # Run recursively until the user selects 4


def strip(string: str):
    if string.startswith('0x') or string.startswith("0b"):
        return string[2:]  # removes the first two characters from the string
    else:
        return string


def decode(selection: str, user_number: str):
    if int(selection) == 1:
        return hex_string_decode(user_number)
    elif int(selection) == 2:
        return binary_string_decode(user_number)
    elif int(selection) == 3:
        return binary_to_hex(user_number)


def prompt_menu():
    print("Decoding Menu")
    print("-------------")
    print("1. Decode hexadecimal")
    print("2. Decode binary")
    print("3. Convert binary to hexadecimal")
    print("4. Quit")
    user_input = (input("Please enter an option: "))

    if user_input == "4":
        print("Goodbye!")
        quit()
    elif user_input not in ["1", "2", "3"]:
        print("Invalid option. Please try again.\n")
        prompt_menu()  # re-prompt
    else:  # valid options get returned
        return user_input


def prompt_number():
    return input("Please enter the numeric string to convert: ")


def hex_char_decode(digit: str) -> int:
    """Decodes a single hexadecimal digit and returns its value."""
    return hex_digits[digit.upper()]  # reads the dictionary and returns the corresponding value


def hex_string_decode(hexadecimal: str) -> int:
    """Decodes an entire hexadecimal string and returns its value."""
    hex_str = strip(hexadecimal)
    index = len(hex_str) - 1
    result = 0

    for char in hex_str:
        conversion = hex_char_decode(char)  # conversion result of the uppercase version of the char
        result += conversion * (16 ** index)  # 16 ** index represents the place value as multiples of  16 (hex)
        index -= 1

    return result


def hex_num_encode(decimal: int) -> int:
    """Encodes a single decimal digit and returns its value."""
    return hex_digits_inverse[decimal]


def hex_string_encode(decimal: int) -> str:
    """Encodes an entire decimal string and returns its value."""
    result = ""
    quotient = decimal

    while quotient > 0:
        remainder = quotient % 16  # calculate remainder
        quotient = quotient // 16  # set the quotient to the new quotient, so we can carry it over

        result = str(hex_num_encode(remainder)) + result

    return result


def binary_string_decode(binary: str):
    """Decodes a binary string and returns its value."""
    binary_str = strip(binary)
    index = len(binary_str) - 1
    result = 0

    for char in binary_str:
        result += int(char) * (2 ** index)  # 2 ** index represents the place value as multiples of 2 (binary)
        index -= 1

    return result


#
def binary_to_hex(binary: str):
    """Decodes a binary string, re-encodes it as hexadecimal, and returns the hexadecimal string."""
    decimal = binary_string_decode(binary)
    hexadecimal = hex_string_encode(decimal)
    return hexadecimal
    # return hex_string_encode(int(binary))


if __name__ == '__main__':
    main()
