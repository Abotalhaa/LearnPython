x = int(input('Enter your age:\n'))

"""
This is a comment
written in
multi lines,
"""
print("You entered: " * x)
if x % 2 == 0:
    print("Even number:")
    print("next line")
    print("3rd line")
elif x > 5:
    print("More than 5")

# This is a comments, not part of code
# Only for documentation.
# شرح تفاضيل ومعلومات عن الكود
# elif 5 < x < 10:
elif x > 5 and x < 10:
    print("Between 5-10")
else:
    print("Odd number")
