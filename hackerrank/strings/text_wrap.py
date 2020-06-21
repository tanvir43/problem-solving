# SAMPLE INPUT
"""
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
"""

# OUTPUT
"""
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
"""

def text_wrap(string, width):
    for i in range(0,len(string), width):
        print(string[i:i+width])

if __name__ == "__main__":
    string = "ABCDEFGHIJKLMNOPQR"
    text_wrap(string, 4)



