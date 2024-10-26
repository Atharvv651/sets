def is_rightmost_set_bit(n):
    return n & 1 == 1

number = int(input("Enter a number: "))
if is_rightmost_set_bit(number):
    print("The rightmost bit is set.")
else:
    print("The rightmost bit is not set.")
