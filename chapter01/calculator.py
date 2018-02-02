#!/usr/bin/env python3

def read_input():
    numbers = []
    prompt = "Please enter a number (Enter or ^D for termination): "

    while True:
        try:
            inp = input(prompt)
            if ("" == inp):
                break
            number = int(inp)
            numbers.append(number*number)
        except ValueError as _:
            print("Error: '{}' is not valid input".format(inp))
            continue
        except EOFError:
            print()
            break
    return numbers

numbers = read_input()
print("Numbers: {}".format(numbers))
if len(numbers) > 0:
    print("Count = {}, Sum = {}, Min = {}, Max = {}, Mean = {}".format(
        len(numbers), sum(numbers), min(numbers), max(numbers), sum(numbers)/len(numbers)))
