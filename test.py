def reverse_string(s):
    # Base case: if the string is empty or has only one character
    if len(s) <= 1:
        return s

    # Recursive case: reverse the substring starting from the second character
    # and append the first character at the end
    print(s)
    return reverse_string(s[1:]) + s[0]

# Example usage
string = "Hello, World!"

# Reverse the string using recursion
reversed_string = reverse_string(string)
print(reversed_string)