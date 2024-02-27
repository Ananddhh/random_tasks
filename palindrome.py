def palindrome(str):
    return str == str[::-1]

my_str = "english"
result = palindrome(my_str)

print(f"the given string {my_str} is a palindrome {result}")