# write a simple function called greet that returns the most-famous "hello world!".
# https://www.codewars.com/kata/523b4ff7adca849afe000035/train/python
def greet():
    return "hello world!"


# convert a number to a string
# we need a function that can transform a number into a string.
# https://www.codewars.com/kata/5265326f5fda8eb1160004c8/train/python
def number_to_string(num):
    return str(num)


# code as fast as you can! you need to double the integer and return it.
# https://www.codewars.com/kata/53ee5429ba190077850011d4/train/python
def double_integer(i):
    return i * 2


# Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems.
# It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').
# Ribonucleic acid, RNA, is the primary messenger molecule in cells.
# RNA differs slightly from DNA its chemical structure and contains no Thymine.
# In RNA Thymine is replaced by another nucleic acid Uracil ('U').
# Create a funciton which translates a given DNA string into RNA.
# https://www.codewars.com/kata/5556282156230d0e5e000089/train/python
def dna_to_rna(dna):
    return dna.replace('T', 'U')


# Complete the square sum function so that it squares each number passed into it and then sums the results together.
# https://www.codewars.com/kata/515e271a311df0350d00000f/train/python
def square_sum(numbers):
    squared_nums = []
    for num in numbers:
        squared_nums.append(num ** 2)
    return sum(squared_nums)


# write a function bmi that calcuates body mass index (bmi = weight / height ^ 2).
# https://www.codewars.com/kata/57a429e253ba3381850000fb/train/python
def bmi(weight, height):
    bmi_calc = weight/(height**2)

    if bmi_calc <= 18.5:
        return "Underweight"
    elif bmi_calc <= 25.0:
        return "Normal"
    elif bmi_calc <= 30.0:
        return "Overweight"
    else:
        return "Obese"


# write a function that removes the spaces from the string, then return the resultant string.
# https://www.codewars.com/kata/57eae20f5500ad98e50002c5/train/python
def no_space(x):
    return x.replace(" ", "")


# Build a function that returns an array of integers from n to 1 where n>0.
# https://www.codewars.com/kata/5a00e05cc374cb34d100000d/train/python
def reverse_seq(n):
    arr = []
    for i in range(n, 0, -1):
        arr.append(i)
    return arr


# The first century spans from the year 1 up to and including the year 100,
# The second - from the year 101 up to and including the year 200, etc.
# Task - Given a year, return the century it is in.
# https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097/train/python
def century(year):
    return (year + 99)//100


# Complete the solution so that it reverses the string passed into it.
# https://www.codewars.com/kata/5168bb5dfe9a00b126000018/train/python
def solution(string):
    return string[::-1]







