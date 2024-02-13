# Numeric Conversion


This **console program** provides a looping menu that invites the user to choose from a menu of number
string decoding options. It provides options to convert hexadecimal and binary into decimal
notation.

```python
def hex_char_decode(digit):
  ``` Decodes a single hexadecimal digit and returns its value.```
```
```python
def hex_string_decode(hex):
  ``` Decodes an entire hexadecimal string and returns its value.```
```
```python
def binary_string_decode(binary):
  ```Decodes a binary string and returns its value.```
```
```python
def binary_to_hex(binary):
  ``` Decodes a binary string, re-encodes it as hexadecimal, and returns the hexadecimal string.```
```

> NOTE: It is common to display hexadecimal numbers with ‘0x’ or ‘0b’ as the prefix (e.g., the number
FFFFFFFF is represented as 0xFFFFFFFF.  It is also common for hex numbers to be typed in lowercase (e.g., 0xffffffff)
