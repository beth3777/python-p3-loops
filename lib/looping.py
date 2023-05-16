#!/usr/bin/env python3

def happy_new_year():
    number = 10
    while number > 0:
        print(number)
        number -= 1
    print("Happy New Year")
    

def square_integers(int_list):
    squared=[]
    for num in int_list:
        if isinstance(num,int):
            squared.append(num**2)
            return squared
    

def fizzbuzz():
    for num in range (1,101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
            elif num % 3 == 0:
                print("Fizz")
                elif num % 5 == 0:
                    print("Buzz")
                    else:
                        print(num)
