# Hello! this program extracts each digit from a given number in a reverse order.

# pseudocode

# Given number
number = 7536
print("Given number is", number)

# Display the Reverse Order of the Given Number
print('Therefore, the reverse order of the Given Number is:')
while number > 0:
    # get the last digit
    digit = number % 10
    # remove the last digit and repeat the loop
    number = number // 10
    print(digit, end=" ")
    