"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
Mat size must be X . ( is an odd natural number, and is times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.


Sample Designs

Size: 7 x 21
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------
Size: 11 x 33
---------------.|.---------------
------------.|..|..|.------------
---------.|..|..|..|..|.---------
------.|..|..|..|..|..|..|.------
---.|..|..|..|..|..|..|..|..|.---
-------------WELCOME-------------
---.|..|..|..|..|..|..|..|..|.---
------.|..|..|..|..|..|..|.------
---------.|..|..|..|..|.---------
------------.|..|..|.------------
---------------.|.---------------
"""

def door_mat(n,m):
    start_counter = 1
    first_half = (n//2)
    median = (n//2) + 1
    second_half = n - median
    end_counter = n - 2
    for i in range(first_half):
        print((".|."*start_counter).center(m, "-"))
        start_counter +=2
    print("welcome".center(m, "-"))
    for i in range(second_half):
        print((".|."*end_counter).center(m, "-"))
        end_counter -= 2

door_mat(7, 21)
                
