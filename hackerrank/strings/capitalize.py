"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.


Given a full name, your task is to capitalize the name appropriately.
"""

def solve(s):
    l = list()
    for i in s[:].split():
        res = i.capitalize()
        l.append(res)
    return ' '.join(l)
if __name__ == '__main__':
    print(solve("hello world"))
