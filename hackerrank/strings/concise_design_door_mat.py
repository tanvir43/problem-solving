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
---------------.|.----------

"""

n = int(input())
m = n * 3

pattern = [(".|."*(2*i + 1)).center(m, "-") for i in range(n//2)]
a = "\n".join(pattern + ["WELCOME".center(m, "-")] + pattern[::-1])
print("\n".join(pattern + ["WELCOME".center(m, "-")] + pattern[::-1]))
