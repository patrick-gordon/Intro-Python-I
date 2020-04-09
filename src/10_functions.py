# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def is_even(x):
    if x % 2 == 0:
        print('true')
    else:
        print('False')

is_even(0)

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

num = is_even(num)

if num is True:
    print('Even')
else:
    print('Odd')

