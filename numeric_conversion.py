def main():
    selection = prompt_menu()  # ask user to select an option => return the option
    user_number = prompt_number()  # ask user to enter a number => return the number
    conversion_result = decode(selection, user_number)  # Decodes the number based on the prompt

    print(f"Result: {conversion_result}\n")  # prints result & adds new line for next run
    main()  # Run recursively until the user selects 4


def decode(selection, user_number):
    if int(selection) == 1:
        return hex_string_decode(user_number)
    elif int(selection) == 2:
        return binary_string_decode(user_number)
    elif int(selection) == 3:
        return binary_to_hex(user_number)
    elif int(selection) == 4:
        return quit()


def prompt_menu():
    print("Decoding Menu")
    print("-------------")
    print("1. Decode hexadecimal")
    print("2. Decode binary")
    print("3. Convert binary to hexadecimal")
    print("4. Quit")
    return input("Please enter an option: ")


def prompt_number():
    return input("Please enter the numeric string to convert: ")


def hex_char_decode(digit):
    """Decodes a single hexadecimal digit and returns its value."""
    hex_digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
                  'C': 12, 'D': 13, 'E': 14, 'F': 15}
    return hex_digits[digit]  # reads the dictionary and returns the corresponding value


def hex_string_decode(hex):
    """Decodes an entire hexadecimal string and returns its value."""
    hex_str = hex
    index = len(hex) - 1
    result = 0

    if hex.startswith('0x') or hex.startswith("0b"):
        hex_str = str[2:]  # removes the first two characters from the string

    for char in hex_str:
        conversion = hex_char_decode(char.upper())  # conversion result of the uppercase version of the char
        result += conversion * (16 ** index)  # 16 ** index represents the place value as multiples of  16 (hex)
        index -= 1

    return result


def hex_string_encode(decimal):
    """Encodes an entire decimal string and returns its value."""
    result = 0
    return result


def binary_string_decode(binary):
    """Decodes a binary string and returns its value."""
    binary_str = binary
    index = len(binary) - 1
    result = 0

    for char in binary:
        result += int(char) * (2 ** index)  # 2 ** index represents the place value as multiples of 2 (binary)
        index -= 1

    return result


#
def binary_to_hex(binary):
    """Decodes a binary string, re-encodes it as hexadecimal, and returns the hexadecimal string."""
    decimal = binary_string_decode(binary)
    hexadecimal = hex_string_encode(decimal)
    return hex


if __name__ == '__main__':
    main()
