"""
Given an integer, , print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary
The four values must be printed on a single line in the order specified above for each  from  to . Each value should be space-padded to match the width of the binary value of .

Sample Input

10
Sample Output

    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
"""

def formatted_string(number):
    for i in range(1, number-1):
        print(f"{i} {oct(i)[2:]} {hex(i)[2:]} {bin(i)[2:]}", end="")
        print("\n")

if __name__ == "__main__":
    formatted_string(10)
