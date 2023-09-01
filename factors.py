#!/usr/bin/bash

import sys
def factorize(n):
    for index in range(2, n // 2 + 1):
        if (n % index == 0):
            return (index, n // index)
    return (None, None)

if len(sys.argv) != 2):
    print("Usage: factors <file>")
    sys.exit(1)

input_file = sys.argv[1]

try:
    with open(input_file, "r") as file:
        for line in file:
            num = int(line.strip())
            p, q = factorize(num)
            if p is not None:
                print(f"{num} = {p} * {q}")
    except FileNotFoundError:
        print(f"File not Found: {input_file}")
        sys.exit(1)
    except ValueError:
        print("Invalid input in the file. Please make sure all lines 
                are valid natural numbers greater than 1.")
        sys.exit(1)
